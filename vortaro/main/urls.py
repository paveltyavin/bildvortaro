from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = []

if not settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', kwargs={'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns(
        'django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', kwargs={'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('social_auth.urls')),
    url(r'^', include('vortaro.app.urls')),
)