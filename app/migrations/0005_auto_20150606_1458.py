# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_word_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(unique=True, max_length=128, verbose_name='\u0418\u043c\u044f', blank=True),
        ),
    ]
