from django.conf.urls import url
from app.api import views

urlpatterns = [
    url(r'^word/$', views.WordList.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
]