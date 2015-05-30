# coding=utf-8
from django_filters.filters import CharFilter
from django_filters.filterset import FilterSet
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from app.models import Word
from app.api import serializers


class WordPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100


class WordList(ListAPIView):
    serializer_class = serializers.WordSerializer
    pagination_class = WordPagination

    def get_queryset(self):
        qs = Word.objects.filter(show_main=True)

        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(name__icontains=search)
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(categories__category__slug=category)

        return qs


class CategoryList(ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return Word.objects.filter(show_top=True)
