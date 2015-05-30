# coding=utf-8
from rest_framework.serializers import ModelSerializer
from app.models import Word


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
