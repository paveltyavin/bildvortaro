from rest_framework import serializers
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word, User


class WordImageField(serializers.ImageField):
    def to_native(self, value):
        try:
            return value.url
        except ValueError:
            return ''


class WordSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')
    image = WordImageField(required=False)

    def get_thumb(self, obj):
        try:
            return get_thumbnail(obj.image, '150x150', upscale=True, background="#fff").url
        except ThumbnailError:
            return ''

    def __init__(self, instance, **kwargs):
        request = kwargs['context']['request']
        data = kwargs.get('data')
        if data:
            if instance and instance.user_created:
                data['user_created'] = instance.user_created.id
            else:
                data['user_created'] = request.user.id

            data['user_modified'] = request.user.id

            if 'image' in data and isinstance(data['image'], basestring):
                del data['image']

        super(WordSerializer, self).__init__(instance, **kwargs)

    class Meta:
        model = Word
        fields = (
            'id',
            'name', 'categories', 'word_class',
            'order',
            'user_created',
            'user_modified',
            'show_top', "show_main",
            'thumb',
            'image',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'is_staff',
        )