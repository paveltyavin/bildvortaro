# coding=utf-8
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from sorl.thumbnail.shortcuts import get_thumbnail
from app.models import Word, User

default_thumb_options = {'padding': True, 'quality': 65, 'upscale': False, 'background': "#fff"}


def get_get_thumb(size):
    def get_thumb(self, obj):
        if obj.image:
            t = get_thumbnail(obj.image, size, **default_thumb_options)
            request = self.context.get('request', None)
            if request is not None:
                return request.build_absolute_uri(t.url)
            return t.url
        else:
            return None

    return get_thumb


class WordDetailSerializer(ModelSerializer):
    thumb = SerializerMethodField()
    can_edit = SerializerMethodField()
    get_thumb = get_get_thumb('300x300')

    def get_can_edit(self, obj):
        return self.context['request'].user.is_authenticated()

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


class WordImageSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = [
            'image',
        ]


class WordSerializer(ModelSerializer):
    thumb = SerializerMethodField()
    get_thumb = get_get_thumb('200x200')

    class Meta:
        model = Word
        fields = [
            'id',
            'name',
            'thumb',
            'slug',
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
        ]
