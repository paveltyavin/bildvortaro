# coding=utf-8
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.timezone import now
from sorl.thumbnail.shortcuts import get_thumbnail


class User(AbstractUser):
    pass


def get_image(instance, filename, **kwargs):
    ar = filename.split('.')
    if len(ar) > 1:
        name, extension = ar[-2:]
        extension = extension.lower()
    else:
        name = filename
        extension = ''
    return u'word/{name}.{extension}'.format(
        name=slugify(unicode(name)),
        extension=extension,
    )


class Word(models.Model):
    class Meta:
        ordering = ('-date_modified',)
        verbose_name = u'Vorto'
        verbose_name_plural = u'Vorti'

    user_created = models.ForeignKey('User', verbose_name=u'Создатель', related_name="word_created")
    user_modified = models.ForeignKey('User', verbose_name=u'Последний изменивший', related_name="word_modified")
    date_created = models.DateTimeField(verbose_name=u'Время создания', default=now)
    date_modified = models.DateTimeField(verbose_name=u'Время изменения', default=now)

    name = models.CharField(max_length=128, verbose_name=u'Имя', blank=True, unique=True, )
    description = models.TextField(verbose_name=u'Описание', blank=True)
    slug = models.SlugField(max_length=128, verbose_name=u'Слаг', blank=True, default='')
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_image, default='', )
    word_set = models.ManyToManyField('Word', symmetrical=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.date_created = now()
        else:
            self.date_modified = now()
        self.slug = slugify(self.name)
        super(Word, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name or u''