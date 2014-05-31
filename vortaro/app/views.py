from django.http.response import HttpResponse
from django.views.generic.base import TemplateView, View


class HomeView(TemplateView):
    template_name = 'base.html'


class LogView(View):
    def get(self, request, *args, **kwargs):
        import logging
        logger = logging.getLogger('raven')
        logger.warn('Murr!', extra={
            'stack': True,
        })
        return HttpResponse('ok')