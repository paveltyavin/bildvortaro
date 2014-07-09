# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word


class Command(BaseCommand):
    help = u'Создание миниатюр'

    def handle(self, *args, **options):
        images_broken = 0
        images_ok = 0
        images_value_error = 0
        default_options = {'padding': True, 'quality': 65, 'upscale': False, 'background': '#fff',}
        for w in Word.objects.filter(image__isnull=False):
            try:
                w.thumb_150 = get_thumbnail(w.image, '150x150', **default_options).name
                w.save()
                images_ok += 1
                if images_ok % 100 == 0:
                    print u'images_ok amount:', images_ok
            except IOError:
                images_broken += 1
                if images_broken % 100 == 0:
                    print u'images_broken amount:', images_broken
            except ValueError:
                images_value_error += 1
                if images_value_error % 100 == 0:
                    print u'images_value_error amount:', images_value_error

        print u'images_ok amount:', images_ok
        print u'images_value_error amount:', images_value_error
        print u'images_broken amount:', images_broken