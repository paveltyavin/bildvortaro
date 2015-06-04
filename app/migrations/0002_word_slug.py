# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='slug',
            field=models.SlugField(default=b'', max_length=128, verbose_name='\u0421\u043b\u0430\u0433', blank=True),
        ),
    ]
