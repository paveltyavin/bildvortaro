from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^word$', views.WordList.as_view()),
    url(r'^category', views.CategoryList.as_view()),
)