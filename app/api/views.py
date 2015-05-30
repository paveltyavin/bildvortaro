# coding=utf-8
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
        qs = Word.objects.all()

        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(name__icontains=search)

        return qs
