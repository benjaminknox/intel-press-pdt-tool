# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'topic_management_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'topic_management', ['Topic'])

        # Adding M2M table for field documents on 'Topic'
        db.create_table(u'topic_management_topic_documents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('topic', models.ForeignKey(orm[u'topic_management.topic'], null=False)),
            ('document', models.ForeignKey(orm[u'topic_management.document'], null=False))
        ))
        db.create_unique(u'topic_management_topic_documents', ['topic_id', 'document_id'])

        # Adding M2M table for field comments on 'Topic'
        db.create_table(u'topic_management_topic_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('topic', models.ForeignKey(orm[u'topic_management.topic'], null=False)),
            ('comment', models.ForeignKey(orm[u'topic_management.comment'], null=False))
        ))
        db.create_unique(u'topic_management_topic_comments', ['topic_id', 'comment_id'])

        # Adding model 'Document'
        db.create_table(u'topic_management_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_topic', to=orm['topic_management.Topic'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fileName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('checksum', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'topic_management', ['Document'])

        # Adding M2M table for field comments on 'Document'
        db.create_table(u'topic_management_document_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm[u'topic_management.document'], null=False)),
            ('comment', models.ForeignKey(orm[u'topic_management.comment'], null=False))
        ))
        db.create_unique(u'topic_management_document_comments', ['document_id', 'comment_id'])

        # Adding model 'Comment'
        db.create_table(u'topic_management_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('reported', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lastmodified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'topic_management', ['Comment'])

        # Adding M2M table for field comments on 'Comment'
        db.create_table(u'topic_management_comment_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_comment', models.ForeignKey(orm[u'topic_management.comment'], null=False)),
            ('to_comment', models.ForeignKey(orm[u'topic_management.comment'], null=False))
        ))
        db.create_unique(u'topic_management_comment_comments', ['from_comment_id', 'to_comment_id'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'topic_management_topic')

        # Removing M2M table for field documents on 'Topic'
        db.delete_table('topic_management_topic_documents')

        # Removing M2M table for field comments on 'Topic'
        db.delete_table('topic_management_topic_comments')

        # Deleting model 'Document'
        db.delete_table(u'topic_management_document')

        # Removing M2M table for field comments on 'Document'
        db.delete_table('topic_management_document_comments')

        # Deleting model 'Comment'
        db.delete_table(u'topic_management_comment')

        # Removing M2M table for field comments on 'Comment'
        db.delete_table('topic_management_comment_comments')


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
        u'topic_management.comment': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Comment'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['topic_management.Comment']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'reported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'topic_management.document': {
            'Meta': {'object_name': 'Document'},
            'checksum': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['topic_management.Comment']", 'symmetrical': 'False', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fileName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_topic'", 'to': u"orm['topic_management.Topic']"})
        },
        u'topic_management.topic': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Topic'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['topic_management.Comment']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'topic_documents'", 'symmetrical': 'False', 'to': u"orm['topic_management.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publicid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['topic_management']