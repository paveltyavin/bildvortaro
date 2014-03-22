from rest_framework import serializers
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word, WORD_CLASS_CHOICES


class WordSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')

    def get_thumb(self, obj):
        return get_thumbnail(obj.image, '150x150', upscale=True, background="#333333").url

    class Meta:
        model = Word
        fields = ('name', 'category', 'thumb', 'word_class')