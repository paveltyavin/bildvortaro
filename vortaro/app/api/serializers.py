from rest_framework import serializers
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word


class WordSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')

    def get_thumb(self, obj):
        return get_thumbnail(obj.image, '200x200', upscale=True).url

    image = serializers.SerializerMethodField('get_image')

    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = Word
        fields = ('name', 'category', 'image', 'thumb', 'word_class')