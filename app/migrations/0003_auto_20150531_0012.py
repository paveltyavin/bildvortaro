# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_word_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('-date_modified',), 'verbose_name': 'Vorto', 'verbose_name_plural': 'Vorti'},
        ),
        migrations.AlterField(
            model_name='wordcategory',
            name='category',
            field=models.ForeignKey(related_name='categoryword', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='app.Word'),
        ),
        migrations.AlterField(
            model_name='wordcategory',
            name='word',
            field=models.ForeignKey(related_name='wordcategory', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='app.Word'),
        ),
    ]
