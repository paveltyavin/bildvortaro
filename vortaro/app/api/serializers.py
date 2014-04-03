from rest_framework import serializers
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word, User


class UserField(serializers.Field):
    def field_from_native(self, *args, **kwargs):
        request = self.context.get('request', None)
        return request.user

    def to_native(self, value):
        return value.id


class WordImageField(serializers.ImageField):
    def to_native(self, value):
        try:
            return value.url
        except ValueError:
            return ''


class WordSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')
    user_created = UserField()
    user_modified = UserField()
    image = WordImageField()

    def get_thumb(self, obj):
        try:
            return get_thumbnail(obj.image, '150x150', upscale=True, background="#fff").url
        except ThumbnailError:
            return ''

    class Meta:
        model = Word
        fields = (
            'id', 'name', 'category', 'thumb', 'word_class', 'order', 'user_created', 'user_modified',
            'image',
        )


class CategorySerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')

    def get_thumb(self, obj):
        return get_thumbnail(obj.image, '24x24', upscale=True, background="#fff").url

    class Meta:
        model = Word
        fields = ('name', 'id', 'thumb')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
        )