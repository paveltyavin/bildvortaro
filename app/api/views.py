# coding=utf-8
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from app.models import Word, WordCategory
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
        category_slug = self.request.query_params.get('category')
        if category_slug:
            qs = qs.filter(wordcategory__category__slug=category_slug)
        return qs


class WordCategoryList(ListAPIView):
    serializer_class = serializers.WordCategorySerializer
    parser_classes = (JSONParser,)

    def get_queryset(self):
        return WordCategory.objects.filter(
            word_id=self.kwargs.get('word_pk'),
        )

    def post(self, request):
        pass


class WordCategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WordCategorySerializer

    def get_queryset(self):
        return WordCategory.objects.filter(
            word_id=self.kwargs.get('word_pk'),
        )


class WordDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WordDetailSerializer
    lookup_field = 'slug'

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_queryset(self):
        qs = Word.objects.filter(show_main=True)
        return qs


class WordDigitDetail(WordDetail):
    lookup_field = 'pk'


class CategoryList(ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return Word.objects.filter(show_top=True)
