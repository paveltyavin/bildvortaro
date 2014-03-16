from django.conf.urls import patterns, url, include
from vortaro.app.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
)
