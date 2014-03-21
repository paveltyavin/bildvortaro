import datetime
from vortaro.app.models import Category


def base(request):
    return {
        'now': datetime.datetime.now(),
        'categories': Category.objects.all(),
    }