from django.http.response import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from vortaro.app.models import Word


class HomeView(ListView):
    template_name = 'home.html'
    model = Word


class ErrorView(View):
    def get(self, request, *args, **kwargs):
        if 1 / 0 == 0:
            pass
        return HttpResponse('ok')


class LogView(View):
    def get(self, request, *args, **kwargs):
        import logging
        logger = logging.getLogger('raven')
        logger.warn('Murr!', extra={
            'stack': True,
        })
        return HttpResponse('ok')