# coding=utf-8
from django import forms
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from app.models import Word


class HomeView(TemplateView):
    template_name = 'base.html'


class WordForm(forms.ModelForm):
    name = forms.CharField(label=u'Vorto')
    image = forms.ImageField(label=u'Bildo')

    class Meta:
        model = Word
        fields = [
            'name',
            'image',
        ]


class AddWordView(CreateView):
    form_class = WordForm
    template_name = 'add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_created = self.request.user
        self.object.user_modified = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')


class WordView(UpdateView):
    def get_object(self, queryset=None):
        return Word.objects.get(slug=self.kwargs.get('slug'))

    template_name = 'word.html'
    form_class = WordForm

    def save_wc_list(self, form):
        pass

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_modified = self.request.user
        self.object.save()

        self.save_wc_list(form)
        url = reverse('word', kwargs={
            'slug': self.object.slug,
        })
        return HttpResponseRedirect(url)

    class Meta:
        model = Word
