import datetime


def base(request):
    return {
        'now': datetime.datetime.now()
    }