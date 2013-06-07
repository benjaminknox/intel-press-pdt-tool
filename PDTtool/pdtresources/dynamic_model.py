### DYNAMIC ###
#Utilities for creating dynamic models, primarily to support the same model
#in many db's
#################

from django.db import connections
from django.db import models
from django.db.models import fields
from django.db.models.fields.related import RelatedField
from django.db.models import loading
from django.db.models.manager import ManagerDescriptor

def create_model(name, fields=None, app_label='', module='', options=None, admin=None):
    """One example of how to create a model dynamically at run-time. The majority
    of this is taken from code.djangoproject.com/wiki/DynamicModels"""

    class Meta:
        # Using type('Meta', ...) gives a dictproxy error during model creation
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create an Admin inner class if admin options were provided
    if admin is not None:
        class Admin:
            pass
        for key, value in admin:
            setattr(Admin, key, value)
        attrs['Admin'] = Admin

    # Create the class, which automatically triggers ModelBase processing
    return type(name, (models.Model,), attrs)
  
def copy_field(field):
    """Instantiate a new field, with all of the values from the old one, except the
    to and to_field in the case of related fields"""
            
    base_kw = dict([(n, getattr(field,n, '_null')) for n in fields.Field.__init__.im_func.func_code.co_varnames])
    if isinstance(field, fields.related.RelatedField):
        rel = base_kw.get('rel')
        rel_kw = dict([(n, getattr(rel,n, '_null')) for n in rel.__init__.im_func.func_code.co_varnames])
        if isinstance(field, fields.related.ForeignKey):
            base_kw['to_field'] = rel_kw.pop('field_name')
        base_kw.update(rel_kw)
    base_kw.pop('self')

    return field.__class__(**base_kw)
    
def get_names(model, other_db):
    """Get names for the new class and the (dummy) module it will be stored under"""
    name = "%s_%s" % (model.__name__, other_db)
    app_label = "%s.%s" %(other_db, model._meta.app_label)
    return name, app_label

def duplicate_model(model, other_db):
    """Given model and other_db (which is a key in django.db.__init__.connections)
    create a new model called model.__name__ + other_db, where the default_manager's
    db points to the correct connection object. Return the new model and any reverse
    relations that need to be created"""

    meta_opts = ['db_table','db_tablespace','get_latest_by','order_with_respect_to',\
                'ordering','unique_together','verbose_name','verbose_name_plural']
    options = dict([(k, getattr(model._meta, k)) for k in meta_opts])
    
    name, app_label = get_names(model, other_db)
    module = app_label
    
    #Copy the functions, properties and any defined managers
    items = model.__dict__.items()
    #Luckily all of the functions that django adds are called _curried
    funcs = filter(lambda x: x[1].func_name != '_curried', \
                   [i for i in items if i[1].__class__.__name__ == 'function'])
    props = [i for i in items if i[1].__class__ == property]
    managers =  [i for i in items if isinstance(i[1], ManagerDescriptor)]    
    fields = dict(funcs + props + managers)

    #None of the items in fields are *really* fields, they will be dealt with next
    new_cls = create_model(name, fields, app_label, module, options)
    setattr(new_cls, 'db', other_db)
    
    #Reset _meta.pk to None to allow correct functioning of Options.add_field
    new_cls._meta.pk, new_cls._meta.has_auto_field = None, False
    #reset fields to empty to get rid of id field created during model creation
    new_cls._meta.fields = []
    
    new_cls._default_manager.db = connections[other_db]
    fields = dict([(f.name, copy_field(f)) for f in model._meta.fields + model._meta.many_to_many])
    for fld_name, f in fields.items():
        if isinstance(f, RelatedField):
            to = f.rel.to
            if to == model:
                new_to = new_cls
            else:
                new_to = duplicate_model(to, other_db)[0]
            f.rel.to = new_to
        new_cls.add_to_class(fld_name, f)
        
    #Make sure all of the reverse reltionships work too.
    rev_related = []
    for ro in model._meta.get_all_related_objects() \
                            + model._meta.get_all_related_many_to_many_objects():
        rel_model_name = get_names(ro.model, other_db)[0]
        if not loading._app_models[module].has_key(rel_model_name.lower()): #is it already created?
            rev_related.append(ro.model)
            
    return new_cls, rev_related

def duplicate_model_and_rels(model,other_db):
    """This is necessary to prevent infinate recursion within duplicate_model"""
    new_cls, rels = duplicate_model(model,other_db)
    for r in rels:
        duplicate_model(r, other_db)
    return new_cls

def migrate_table_structure(model, new_db_key):
    """Get the CREATE TABLE statement from the existing model and execute
    it on the new db, in the new db's sql dialect"""
    new_db = connections[new_db_key]
    builder = new_db.get_creation_module().builder
    cursor = new_db.connection.cursor()
    new_introspection_mod = new_db.get_introspection_module()
    try:
        assert model._meta.db_table.upper() not in \
               [t.upper() for t in new_introspection_mod.get_table_list(cursor)], \
                'Table %s already exists' % model._meta.db_table
    except AssertionError:
        return #Skip it if this table already exisits
    #A BoundStatement's __str__() is the SQL itself
    create_table = builder.get_create_table(model)
    cursor.execute(create_table[0][0].__str__())