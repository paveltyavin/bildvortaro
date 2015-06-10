# coding=utf-8
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from app.models import Word
from app.api import serializers


class WordPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100


class WordList(ListCreateAPIView):
    serializer_class = serializers.WordSerializer
    pagination_class = WordPagination

    def get_queryset(self):
        qs = Word.objects.all()

        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(name__icontains=search)
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


class WordRelationList(ListAPIView):
    serializer_class = serializers.WordSerializer

    def get_queryset(self):
        try:
            word = Word.objects.get(id=self.kwargs.get('pk'))
        except Word.DoesNotExist:
            raise ParseError()
        return word.word_set.all()

    def post(self, request, **kwargs):
        try:
            word = Word.objects.get(id=self.kwargs.get('pk'))
        except Word.DoesNotExist:
            raise ParseError()

        try:
            related_word = Word.objects.get(id=self.request.data.get('word_id'))
        except Word.DoesNotExist:
            raise ParseError()
        word.word_set.add(related_word)
        return Response()

    def delete(self, request, **kwargs):
        try:
            word = Word.objects.get(id=self.kwargs.get('pk'))
        except Word.DoesNotExist:
            raise ParseError()

        try:
            related_word = Word.objects.get(id=self.request.data.get('word_id'))
        except Word.DoesNotExist:
            raise ParseError()
        word.word_set.remove(related_word)
        return Response()


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
    
    
class UserCurrent(RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user