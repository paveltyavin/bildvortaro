from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^auth$', views.Auth.as_view()),
    url(r'^csrf$', views.CSRF.as_view()),
    url(r'^user$', views.UserList.as_view()),
    url(r'^user/me$', views.Me.as_view()),
    url(r'^word$', views.WordList.as_view()),
    url(r'^word/(?P<pk>\d+)$', views.WordDetail.as_view()),
)