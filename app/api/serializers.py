# coding=utf-8
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from sorl.thumbnail.shortcuts import get_thumbnail
from app.models import Word


class WordSerializer(ModelSerializer):
    thumb = SerializerMethodField()

    def get_thumb(self, obj):
        if obj.image:
            t = get_thumbnail(obj.image, '200x200')
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(t.url)
            return t.url
        else:
            return None

    class Meta:
        model = Word
        fields = [
            'name',
            'thumb',
            'slug',
        ]


class CategorySerializer(ModelSerializer):
    thumb = SerializerMethodField()

    def get_thumb(self, obj):
        if obj.image:
            t = get_thumbnail(obj.image, '32x32')
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(t.url)
            return t.url
        else:
            return None

    class Meta:
        model = Word
        fields = [
            'name',
            'thumb',
            'slug',
        ]
