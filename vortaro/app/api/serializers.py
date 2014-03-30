from rest_framework import serializers
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word, User


class WordSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')

    def get_thumb(self, obj):
        return get_thumbnail(obj.image, '150x150', upscale=True, background="#fff").url

    class Meta:
        model = Word
        fields = ('name', 'category', 'thumb', 'word_class', 'order')


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