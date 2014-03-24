# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Word.user_created'
        db.add_column(u'app_word', 'user_created',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='word_created', to=orm['app.User']),
                      keep_default=False)

        # Adding field 'Word.user_modified'
        db.add_column(u'app_word', 'user_modified',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='word_modified', to=orm['app.User']),
                      keep_default=False)

        # Adding field 'Word.date_created'
        db.add_column(u'app_word', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 25, 0, 0)),
                      keep_default=False)

        # Adding field 'Word.date_modified'
        db.add_column(u'app_word', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 25, 0, 0)),
                      keep_default=False)

        # Adding field 'Word.order'
        db.add_column(u'app_word', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Category.user_created'
        db.add_column(u'app_category', 'user_created',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='category_created', to=orm['app.User']),
                      keep_default=False)

        # Adding field 'Category.user_modified'
        db.add_column(u'app_category', 'user_modified',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='category_modified', to=orm['app.User']),
                      keep_default=False)

        # Adding field 'Category.date_created'
        db.add_column(u'app_category', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 25, 0, 0)),
                      keep_default=False)

        # Adding field 'Category.date_modified'
        db.add_column(u'app_category', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 25, 0, 0)),
                      keep_default=False)



    def backwards(self, orm):
        # Deleting field 'Word.user_created'
        db.delete_column(u'app_word', 'user_created_id')

        # Deleting field 'Word.user_modified'
        db.delete_column(u'app_word', 'user_modified_id')

        # Deleting field 'Word.date_created'
        db.delete_column(u'app_word', 'date_created')

        # Deleting field 'Word.date_modified'
        db.delete_column(u'app_word', 'date_modified')

        # Deleting field 'Word.order'
        db.delete_column(u'app_word', 'order')

        # Deleting field 'Category.user_created'
        db.delete_column(u'app_category', 'user_created_id')

        # Deleting field 'Category.user_modified'
        db.delete_column(u'app_category', 'user_modified_id')

        # Deleting field 'Category.date_created'
        db.delete_column(u'app_category', 'date_created')

        # Deleting field 'Category.date_modified'
        db.delete_column(u'app_category', 'date_modified')


    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 25, 0, 0)'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'category_created'", 'to': u"orm['app.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'category_modified'", 'to': u"orm['app.User']"})
        },
        u'app.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'app.word': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Word'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['app.Category']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 25, 0, 0)'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'word_created'", 'to': u"orm['app.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'word_modified'", 'to': u"orm['app.User']"}),
            'word_class': ('django.db.models.fields.CharField', [], {'default': "u'S'", 'max_length': '10'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']