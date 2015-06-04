from django.conf.urls import url
from app.api import views

urlpatterns = [
    url(r'^word/$', views.WordList.as_view()),
    url(r'^word/(?P<pk>\d+)/$', views.WordDetail.as_view()),
    url(r'^word/(?P<slug>[-\w\d]+)/$', views.WordSlugDetail.as_view()),
    url(r'^word/(?P<pk>\d+)/image/$', views.WordImage.as_view()),
    url(r'^word/(?P<pk>\d+)/category/$', views.WordCategoryList.as_view()),

    url(r'^wordcategory/(?P<pk>\d+)/$', views.WordCategoryDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
]
