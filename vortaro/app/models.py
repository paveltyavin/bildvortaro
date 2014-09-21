# coding=utf-8
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

from django.db.models.signals import post_delete, post_save, pre_save
from sorl.thumbnail import delete
from sorl.thumbnail.shortcuts import get_thumbnail


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


class Word(models.Model):
    class Meta:
        ordering = ('-date_modified',)
        verbose_name = u'Слово'
        verbose_name_plural = u'Слова'


    user_created = models.ForeignKey('User', verbose_name=u'Создатель', default=1,
                                     related_name="%(class)s_created")
    user_modified = models.ForeignKey('User', verbose_name=u'Последний изменивший', default=1,
                                      related_name="%(class)s_modified")
    date_created = models.DateTimeField(verbose_name=u'Время создания', default=datetime.datetime.now())
    date_modified = models.DateTimeField(verbose_name=u'Время изменения', default=datetime.datetime.now())

    name = models.CharField(max_length=128, verbose_name=u'Имя', blank=True)
    image = models.ImageField(
        verbose_name=u'Изображение',
        upload_to=get_image_wrap('word'),
        default='',
    )
    thumb_150 = models.ImageField(
        verbose_name=u'Изображение',
        upload_to=get_image_wrap('word'),
        default='',
    )
    word_class = models.CharField(choices=WORD_CLASS_CHOICES, default=u'S', max_length=10)
    show_main = models.BooleanField(verbose_name=u'Показывать в главном регионе', default=True)
    show_top = models.BooleanField(verbose_name=u'Показывать в верхнем регионе', default=False)

    def __unicode__(self):
        return self.name or u''


class WordCategory(models.Model):
    category = models.ForeignKey(Word, verbose_name=u'Категория', related_name='words')
    word = models.ForeignKey(Word, verbose_name=u'Категория', related_name='categories')
    word_order = models.IntegerField(default=0, blank=False, null=False, verbose_name=u'Сортировка в группе')

    def __unicode__(self):
        return u'{} {}'.format(self.word.name, self.category.name)

    class Meta:
        unique_together = ('category', 'word')
        verbose_name = u'Связь слов'
        verbose_name_plural = u'Связи слов'



def delete_image(instance, **kwargs):
    if instance.image:
        delete(instance.image)


def post_word_save(instance, created, *args, **kwargs):
    now = datetime.datetime.now()
    qs = Word.objects.filter(pk=instance.pk)
    if created:
        qs.update(date_created=now)
    else:
        qs.update(date_modified=now)


def image_word(instance, *args, **kwargs):
    if instance.image and not instance.thumb_150:
        default_options = {'padding': True, 'quality': 65, 'upscale': False, 'background':"#fff"}
        instance.thumb_150 = get_thumbnail(instance.image, '150x150', **default_options).name


post_delete.connect(delete_image, sender=Word)
post_save.connect(post_word_save, sender=Word)
post_save.connect(image_word, sender=Word)
