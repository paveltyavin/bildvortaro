from django.conf import settings
from django.test import TestCase
from app.models import User, Word

class ModelsTestCase(TestCase):
    def setUp(self):
        pass

    def test_model_create(self):
        for model in (User, Word):
            count = model.objects.all().count()
            model.objects.create()
            self.assertEqual(model.objects.all().count(), count + 1)
