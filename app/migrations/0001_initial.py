# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('name', models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('image', models.ImageField(default=b'', upload_to=app.models.get_image, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('word_class', models.CharField(default='S', max_length=10, choices=[('S', 'substantivoj'), ('A', 'adjektivoj'), ('V', 'verboj'), ('N', 'numeraloj')])),
                ('show_main', models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u043c \u0440\u0435\u0433\u0438\u043e\u043d\u0435')),
                ('show_top', models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0432 \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u0440\u0435\u0433\u0438\u043e\u043d\u0435')),
                ('user_created', models.ForeignKey(related_name='word_created', verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(related_name='word_modified', verbose_name='\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u0438\u0437\u043c\u0435\u043d\u0438\u0432\u0448\u0438\u0439', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_modified',),
                'verbose_name': '\u0421\u043b\u043e\u0432\u043e',
                'verbose_name_plural': '\u0421\u043b\u043e\u0432\u0430',
            },
        ),
        migrations.CreateModel(
            name='WordCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_order', models.IntegerField(default=0, verbose_name='\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0432 \u0433\u0440\u0443\u043f\u043f\u0435')),
                ('category', models.ForeignKey(related_name='words', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='app.Word')),
                ('word', models.ForeignKey(related_name='categories', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='app.Word')),
            ],
            options={
                'verbose_name': '\u0421\u0432\u044f\u0437\u044c \u0441\u043b\u043e\u0432',
                'verbose_name_plural': '\u0421\u0432\u044f\u0437\u0438 \u0441\u043b\u043e\u0432',
            },
        ),
        migrations.AlterUniqueTogether(
            name='wordcategory',
            unique_together=set([('category', 'word')]),
        ),
    ]
