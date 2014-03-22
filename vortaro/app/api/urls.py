from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^word$', views.WordList.as_view()),
)