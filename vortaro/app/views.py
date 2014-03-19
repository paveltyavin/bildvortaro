from django.http.response import HttpResponse
from django.views.generic.base import TemplateView, View


class HomeView(TemplateView):
    template_name = 'home.html'


class ErrorView(View):
    def get(self, request, *args, **kwargs):
        if 1 / 0 == 0:
            pass
        return HttpResponse('ok')


class LogView(View):
    def get(self, request, *args, **kwargs):
        import logging
        logger = logging.getLogger('raven')
        logging.warn({})
        return HttpResponse('ok')