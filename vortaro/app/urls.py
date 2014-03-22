from django.conf.urls import patterns, url, include
from vortaro.app import views

urlpatterns = patterns(
    '',
    url(r'^api/', include('vortaro.app.api.urls')),
    url(r'^$', views.HomeView.as_view()),
    url(r'^error$', views.ErrorView.as_view()),
    url(r'^log$', views.LogView.as_view()),
)