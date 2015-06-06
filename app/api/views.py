# coding=utf-8
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from app.models import Word, WordCategory
from app.api import serializers


class WordPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100


class WordList(ListCreateAPIView):
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            user_created=user,
            user_modified=user,
        )


class WordCategoryList(ListAPIView):
    serializer_class = serializers.WordCategorySerializer

    def get_queryset(self):
        return WordCategory.objects.filter(
            word_id=self.kwargs.get('pk'),
        )

    def post(self, request, **kwargs):
        try:
            category = Word.objects.get(id=self.request.data.get('category_id'))
        except Word.DoesNotExist:
            return ParseError()
        try:
            word = Word.objects.get(id=self.kwargs.get('pk'))
        except Word.DoesNotExist:
            return ParseError()
        WordCategory.objects.get_or_create(
            word=word,
            category=category,
        )
        return Response()


class WordCategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WordCategorySerializer

    def get_queryset(self):
        return WordCategory.objects.all()


class WordDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WordDetailSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_queryset(self):
        return Word.objects.all()


class WordSlugDetail(WordDetail):
    lookup_field = 'slug'


class WordImage(UpdateAPIView):
    parser_classes = (FileUploadParser,)
    serializer_class = serializers.WordImageSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_queryset(self):
        return Word.objects.all()


class CategoryList(ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        qs = Word.objects.filter(show_top=True)
        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(name__icontains=search)
        return qs
