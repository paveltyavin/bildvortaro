from django.conf.urls import patterns, url, include
from app import views

urlpatterns = patterns(
    '',
    url(r'^api/', include('app.api.urls')),
    url(r'^$', views.HomeView.as_view()),
)