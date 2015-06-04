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


WORD_CLASS_CHOICES = (
    (u'S', u'substantivoj'),
    (u'A', u'adjektivoj'),
    (u'V', u'verboj'),
    (u'N', u'numeraloj'),
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

    name = models.CharField(max_length=128, verbose_name=u'Имя', blank=True)
    description = models.TextField(verbose_name=u'Описание', blank=True)
    slug = models.SlugField(max_length=128, verbose_name=u'Слаг', blank=True, default='')
    image = models.ImageField(verbose_name=u'Изображение', upload_to=get_image, default='', )

    @property
    def thumb(self):
        default_options = {'padding': True, 'quality': 65, 'upscale': False, 'background': "#fff"}
        t = get_thumbnail(self.image, '150x150', **default_options)
        return t.url

    word_class = models.CharField(choices=WORD_CLASS_CHOICES, default=u'S', max_length=10)
    show_main = models.BooleanField(verbose_name=u'Показывать в главном регионе', default=True)
    show_top = models.BooleanField(verbose_name=u'Показывать в верхнем регионе', default=False)

    def save(self, *args, **kwargs):
        if self.id:
            self.date_created = now()
        else:
            self.date_modified = now()
        self.slug = slugify(self.name)
        super(Word, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name or u''


class WordCategory(models.Model):
    category = models.ForeignKey(Word, verbose_name=u'Категория', related_name='categoryword')
    word = models.ForeignKey(Word, verbose_name=u'Категория', related_name='wordcategory')
    word_order = models.IntegerField(default=0, blank=False, null=False, verbose_name=u'Сортировка в группе')

    def __unicode__(self):
        return u'{} {}'.format(self.word.name, self.category.name)

    class Meta:
        unique_together = ('category', 'word')
        verbose_name = u'Связь слов'
        verbose_name_plural = u'Связи слов'
