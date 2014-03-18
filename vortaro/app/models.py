# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Word(models.Model):
    class Meta:
        verbose_name = u'Слово'
        verbose_name_plural = u'Слова'

    name = models.CharField(max_length=128, verbose_name=u'Имя')