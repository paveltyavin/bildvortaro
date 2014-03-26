from django.conf import settings
from django.test import TestCase
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import User, Word
from django.core.files import File
import os


class ModelsTestCase(TestCase):
    def setUp(self):
        pass

    def test_model_create(self):
        for model in (User, Word):
            count = model.objects.all().count()
            model.objects.create()
            self.assertEqual(model.objects.all().count(), count + 1)


class WordTestCase(TestCase):
    def setUp(self):
        test_img_path = os.path.abspath(settings.DJANGO_ROOT, 'app/tests/files/1.jpg')
        test_img = open(test_img_path, 'rb')
        self.word = Word.objects.create(
            image=File(test_img)
        )
        test_img.close()

    def test_word_image_thumbnail(self):
        get_thumbnail(self.word.image, '200x200')

