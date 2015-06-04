from django.conf.urls import url
from app.api import views

urlpatterns = [
    url(r'^word/$', views.WordList.as_view()),
    url(r'^word/(?P<pk>\d+)/$', views.WordDigitDetail.as_view()),
    url(r'^word/(?P<slug>[-\w\d]+)/$', views.WordDetail.as_view()),
    url(r'^word/(?P<word_pk>\d+)/category/$', views.WordCategoryList.as_view()),
    url(r'^word/(?P<word_pk>\d+)/category/(?P<wordcategory_pk>\d+)/$', views.WordCategoryDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
]
