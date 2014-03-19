# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

from django.db.models.signals import post_delete
from sorl.thumbnail import delete


class User(AbstractUser):
    pass


def get_image_wrap(model):
    def f(instance, filename, **kwargs):
        ar = filename.split('.')
        if len(ar) > 1:
            name, extension = ar[-2:]
        else:
            name = filename
            extension = ''
        return '{model}/{name}.{extension}'.format(
            model=model,
            name=slugify(name),
            extension=extension.lower(),
        )

    return f


class Word(models.Model):
    class Meta:
        verbose_name = u'Слово'
        verbose_name_plural = u'Слова'

    name = models.CharField(max_length=128, verbose_name=u'Имя')
    category = models.ForeignKey('Category', verbose_name=u'Категория', blank=True, null=True, default=None,)
    image = models.ImageField(
        verbose_name=u'Изображение',
        upload_to=get_image_wrap('word'),
        default='',
    )

    def __unicode__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Катеоргии'

    name = models.CharField(max_length=128, verbose_name=u'Имя')
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_image_wrap('category'))
    def __unicode__(self):
        return self.name


def delete_image(instance, **kwargs):
    if instance.image:
        delete(instance.image)


post_delete.connect(delete_image, sender=Word)