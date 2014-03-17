from django.views.generic.base import TemplateView, View


class HomeView(TemplateView):
    template_name = 'home.html'


class ErrorView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if 1 / 0 == 0:
            pass


class LogView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        import logging
        logger = logging.getLogger('raven')
        logging.warn({})