from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = []

if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, kwargs={'document_root': settings.MEDIA_ROOT}),
    ]

urlpatterns += [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.urls')),
]