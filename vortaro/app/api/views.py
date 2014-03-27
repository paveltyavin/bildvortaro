from rest_framework.generics import ListAPIView
from vortaro.app.api import serializers
from vortaro.app.models import Word, Category


class WordList(ListAPIView):
    model = Word
    serializer_class = serializers.WordSerializer


class CategoryList(ListAPIView):
    model = Category
    serializer_class = serializers.CategorySerializer