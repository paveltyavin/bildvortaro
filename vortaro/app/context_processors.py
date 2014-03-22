import datetime
from django.conf import settings
from vortaro.app.models import Category, WORD_CLASS_CHOICES


def base(request):
    return {
        'now': datetime.datetime.now(),
        'categories': Category.objects.all(),
        'word_class_choices': WORD_CLASS_CHOICES,
        'DEBUG': settings.DEBUG,
    }