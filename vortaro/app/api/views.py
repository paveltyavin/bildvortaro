from rest_framework.generics import ListAPIView
from vortaro.app.api import serializers
from vortaro.app.models import Word


class WordList(ListAPIView):
    model = Word
    serializer_class = serializers.WordSerializer