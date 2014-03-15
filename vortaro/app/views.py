from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        pass
        return super(HomeView, self).get(request, *args, **kwargs)
