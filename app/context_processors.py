import datetime
from django.conf import settings


def base(request):
    return {
        'now': datetime.datetime.now(),
        'DEBUG': settings.DEBUG,
    }
