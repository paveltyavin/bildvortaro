from django.test import TestCase
from vortaro.app.models import User


class ModelsTestCase(TestCase):
    def setUp(self):
        User.objects.create()

    def test_user_create(self):
        self.assertEqual(User.objects.all().count(), 1)