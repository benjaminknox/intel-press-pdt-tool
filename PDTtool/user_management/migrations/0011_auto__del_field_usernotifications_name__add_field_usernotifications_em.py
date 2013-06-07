# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserNotifications.name'
        db.delete_column(u'user_management_usernotifications', 'name')

        # Adding field 'UserNotifications.emailnotification'
        db.add_column(u'user_management_usernotifications', 'emailnotification',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.countdownnotification'
        db.add_column(u'user_management_usernotifications', 'countdownnotification',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.countdownnotification_2days'
        db.add_column(u'user_management_usernotifications', 'countdownnotification_2days',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.startdatenotification_1day'
        db.add_column(u'user_management_usernotifications', 'startdatenotification_1day',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.countdownnotification_1day'
        db.add_column(u'user_management_usernotifications', 'countdownnotification_1day',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.countdownnotification_3days'
        db.add_column(u'user_management_usernotifications', 'countdownnotification_3days',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.startdatenotification_1week'
        db.add_column(u'user_management_usernotifications', 'startdatenotification_1week',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.startdatenotification'
        db.add_column(u'user_management_usernotifications', 'startdatenotification',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.startdatenotification_2days'
        db.add_column(u'user_management_usernotifications', 'startdatenotification_2days',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.countdownnotification_1week'
        db.add_column(u'user_management_usernotifications', 'countdownnotification_1week',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Adding field 'UserNotifications.startdatenotification_3days'
        db.add_column(u'user_management_usernotifications', 'startdatenotification_3days',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UserNotifications.name'
        db.add_column(u'user_management_usernotifications', 'name',
                      self.gf('user_management.fields.NotificationField')(default=True),
                      keep_default=False)

        # Deleting field 'UserNotifications.emailnotification'
        db.delete_column(u'user_management_usernotifications', 'emailnotification')

        # Deleting field 'UserNotifications.countdownnotification'
        db.delete_column(u'user_management_usernotifications', 'countdownnotification')

        # Deleting field 'UserNotifications.countdownnotification_2days'
        db.delete_column(u'user_management_usernotifications', 'countdownnotification_2days')

        # Deleting field 'UserNotifications.startdatenotification_1day'
        db.delete_column(u'user_management_usernotifications', 'startdatenotification_1day')

        # Deleting field 'UserNotifications.countdownnotification_1day'
        db.delete_column(u'user_management_usernotifications', 'countdownnotification_1day')

        # Deleting field 'UserNotifications.countdownnotification_3days'
        db.delete_column(u'user_management_usernotifications', 'countdownnotification_3days')

        # Deleting field 'UserNotifications.startdatenotification_1week'
        db.delete_column(u'user_management_usernotifications', 'startdatenotification_1week')

        # Deleting field 'UserNotifications.startdatenotification'
        db.delete_column(u'user_management_usernotifications', 'startdatenotification')

        # Deleting field 'UserNotifications.startdatenotification_2days'
        db.delete_column(u'user_management_usernotifications', 'startdatenotification_2days')

        # Deleting field 'UserNotifications.countdownnotification_1week'
        db.delete_column(u'user_management_usernotifications', 'countdownnotification_1week')

        # Deleting field 'UserNotifications.startdatenotification_3days'
        db.delete_column(u'user_management_usernotifications', 'startdatenotification_3days')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'user_management.activateuserdb': {
            'Meta': {'object_name': 'ActivateUserDB'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'user_management.extendeduser': {
            'Meta': {'ordering': "['pk']", 'object_name': 'ExtendedUser'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notifications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['user_management.Notification']", 'symmetrical': 'False', 'blank': 'True'}),
            'phonenumber': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'user_management.forgotpassworddb': {
            'Meta': {'object_name': 'ForgotPasswordDB'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'user_management.notification': {
            'Meta': {'object_name': 'Notification'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'user_management.organization': {
            'Meta': {'object_name': 'Organization'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'user_management.usernotifications': {
            'Meta': {'object_name': 'UserNotifications'},
            'countdownnotification': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'countdownnotification_1day': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'countdownnotification_1week': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'countdownnotification_2days': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'countdownnotification_3days': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'emailnotification': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'extendeduser': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['user_management.ExtendedUser']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'startdatenotification': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'startdatenotification_1day': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'startdatenotification_1week': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'startdatenotification_2days': ('user_management.fields.NotificationField', [], {'default': 'True'}),
            'startdatenotification_3days': ('user_management.fields.NotificationField', [], {'default': 'True'})
        }
    }

    complete_apps = ['user_management']