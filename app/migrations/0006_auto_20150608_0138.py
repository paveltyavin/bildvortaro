# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150606_1458'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wordcategory',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='wordcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='wordcategory',
            name='word',
        ),
        migrations.RemoveField(
            model_name='word',
            name='show_main',
        ),
        migrations.RemoveField(
            model_name='word',
            name='show_top',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_class',
        ),
        migrations.AddField(
            model_name='word',
            name='word_set',
            field=models.ManyToManyField(related_name='word_set_rel_+', to='app.Word'),
        ),
        migrations.DeleteModel(
            name='WordCategory',
        ),
    ]
