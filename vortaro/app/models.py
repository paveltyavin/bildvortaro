# coding=utf-8
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

from django.db.models.signals import post_delete, post_save, pre_save
from sorl.thumbnail import delete


class User(AbstractUser):
    pass


class OwnerModel(models.Model):
    class Meta:
        abstract = True

    user_created = models.ForeignKey('User', verbose_name=u'Создатель', default=1,
                                     related_name="%(class)s_created")
    user_modified = models.ForeignKey('User', verbose_name=u'Последний изменивший', default=1,
                                      related_name="%(class)s_modified")
    date_created = models.DateTimeField(verbose_name=u'Время создания', default=datetime.datetime.now())
    date_modified = models.DateTimeField(verbose_name=u'Время создания', default=datetime.datetime.now())


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
            # extension='jpg',
            extension=extension.lower(),
        )

    return f


WORD_CLASS_CHOICES = (
    (u'S', u'substantivoj'),
    (u'A', u'adjektivoj'),
    (u'V', u'verboj'),
    (u'N', u'numeraloj'),
)


class Word(OwnerModel):
    class Meta:
        ordering = ('order',)
        verbose_name = u'Слово'
        verbose_name_plural = u'Слова'

    order = models.IntegerField(default=0, blank=False, null=False, verbose_name=u'Сортировка')

    name = models.CharField(max_length=128, verbose_name=u'Имя', blank=True )
    category = models.ForeignKey('Category', verbose_name=u'Категория', blank=True, null=True, default=None, )
    image = models.ImageField(
        verbose_name=u'Изображение',
        upload_to=get_image_wrap('word'),
        default='',
    )
    word_class = models.CharField(choices=WORD_CLASS_CHOICES, default=u'S', max_length=10)

    def __unicode__(self):
        return self.name


class Category(OwnerModel):
    class Meta:
        ordering = ('order',)
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    order = models.IntegerField(default=0, blank=False, null=False, verbose_name=u'Сортировка')
    name = models.CharField(max_length=128, verbose_name=u'Имя')
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_image_wrap('category'))


    def __unicode__(self):
        return self.name


def delete_image(instance, **kwargs):
    if instance.image:
        delete(instance.image)


def post_OwnerModel_save(instance, created, *args, **kwargs):
    if hasattr(instance, 'saved'):
        return
    if created:
        instance.date_created = datetime.datetime.now()
    else:
        instance.date_modified = datetime.datetime.now()
    instance.saved = True
    instance.save()


post_delete.connect(delete_image, sender=Word)
post_save.connect(post_OwnerModel_save, sender=Word)
post_save.connect(post_OwnerModel_save, sender=Category)
