from rest_framework import serializers
from sorl.thumbnail.helpers import ThumbnailError
from sorl.thumbnail.shortcuts import get_thumbnail
from vortaro.app.models import Word, User, WordCategory


class WordImageField(serializers.ImageField):
    def to_native(self, value):
        try:
            return value.url
        except ValueError:
            return ''


class CategoriesField(serializers.Field):
    def field_to_native(self, obj, field_name):
        return {wc.category_id: wc.word_order for wc in obj.categories.all()}


class WordSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField('get_thumb')
    image = WordImageField(required=False)
    categories = CategoriesField()

    def get_thumb(self, obj):
        if obj.thumb_150:
            return obj.thumb_150.url
        else:
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
            'user_created',
            'user_modified',
            'show_top', "show_main",
            'thumb',
            'image',
        )

    read_only = ('thumb', 'categories')


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