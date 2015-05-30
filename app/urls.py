from django.conf.urls import patterns, url, include
from app import views

urlpatterns = [
    url(r'^api/', include('app.api.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^aldoni/$', views.AddWordView.as_view(), name='add'),
    url(r'^(?P<slug>[-_\d\w]+)/$', views.WordView.as_view(), name='word'),
]
