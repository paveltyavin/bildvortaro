# coding=utf-8
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from app.models import Word


class HomeView(TemplateView):
    template_name = 'home.html'


class AddWordView(TemplateView):
    template_name = 'add.html'


class WordView(DetailView):
    def get_object(self, queryset=None):
        return Word.objects.get(slug=self.kwargs.get('slug'))

    template_name = 'word.html'
