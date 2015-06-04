# coding=utf-8
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from sorl.thumbnail.shortcuts import get_thumbnail
from app.models import Word, WordCategory


class WordDetailSerializer(ModelSerializer):
    thumb = SerializerMethodField()

    def get_can_edit(self, obj):
        return True

    can_edit = SerializerMethodField()

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
            'id',
            'name',
            'thumb',
            'description',
            'slug',
            'can_edit',
        ]


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
            'id',
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


class WordCategorySerializer(ModelSerializer):
    category = WordSerializer()

    class Meta:
        model = WordCategory
        fields = [
            'id',
            'category',
            'word_order',
        ]
