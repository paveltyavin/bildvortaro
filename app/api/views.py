# coding=utf-8
from rest_framework.generics import ListAPIView
from app.models import Word
from app.api import serializers


class WordList(ListAPIView):
    serializer_class = serializers.WordSerializer

    def get_queryset(self):
        return Word.objects.all()
