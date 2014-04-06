# -*- coding: utf-8 -*-
from django.core.files.base import File
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):
    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        categories = orm['app.Category'].objects.all()
        for category in categories:
            new_word, created = orm['app.Word'].objects.get_or_create(
                name=category.name,
                show_main=False,
                show_top=True,
                image=category.image,
            )
            f = File(open(category.image.url, "w"))
            new_word.image.save(f)
            new_word.save()

            for word in category.word_set.all():
                word.categories.add(new_word)
            category.delete()

    def backwards(self, orm):
        "Write your backwards methods here."
        words = orm['app.Word'].objects.filter(
            show_main=False,
            show_top=True,
        )
        for word in words:
            category, created = orm['app.Category'].objects.get_or_create(
                name=word.name,
                image=word.image,
            )
            for child_word in word.word_set.all():
                child_word.category = category
                child_word.save()
            word.delete()

    models = {
        u'app.category': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Category'},
            'date_created': (
                'django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 6, 0, 0)'}),
            'date_modified': (
                'django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [],
                             {'default': '1', 'related_name': "'category_created'", 'to': u"orm['app.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [],
                              {'default': '1', 'related_name': "'category_modified'", 'to': u"orm['app.User']"})
        },
        u'app.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                        'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                                  'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'app.word': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Word'},
            'category': ('django.db.models.fields.related.ForeignKey', [],
                         {'default': 'None', 'to': u"orm['app.Category']", 'null': 'True', 'blank': 'True'}),
            'date_created': (
                'django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 6, 0, 0)'}),
            'date_modified': (
                'django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'show_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [],
                             {'default': '1', 'related_name': "'word_created'", 'to': u"orm['app.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [],
                              {'default': '1', 'related_name': "'word_modified'", 'to': u"orm['app.User']"}),
            'word_class': ('django.db.models.fields.CharField', [], {'default': "u'S'", 'max_length': '10'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [],
                           {'to': u"orm['app.Word']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                            {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
                     'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
                'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']
    symmetrical = True
