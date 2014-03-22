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
        return u'{model}/{name}.{extension}'.format(
            model=model,
            name=slugify(unicode(name)),
            extension=extension.lower(),
        )

    return f


WORD_CLASS_CHOICES = (
    (u'S', u'substantivoj'),
    (u'A', u'adjektivoj'),
    (u'V', u'verboj'),
    (u'N', u'numeraloj'),
)


class Word(models.Model):
    class Meta:
        verbose_name = u'Слово'
        verbose_name_plural = u'Слова'

    name = models.CharField(max_length=128, verbose_name=u'Имя', unique=True,)
    category = models.ForeignKey('Category', verbose_name=u'Категория', blank=True, null=True, default=None, )
    image = models.ImageField(
        verbose_name=u'Изображение',
        upload_to=get_image_wrap('word'),
        default='',
    )
    word_class = models.CharField(choices=WORD_CLASS_CHOICES, default=u'S', max_length=10)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    name = models.CharField(max_length=128, verbose_name=u'Имя')
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_image_wrap('category'))


    def __unicode__(self):
        return self.name


def delete_image(instance, **kwargs):
    if instance.image:
        delete(instance.image)


post_delete.connect(delete_image, sender=Word)