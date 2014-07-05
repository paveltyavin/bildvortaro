import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from vortaro.app.api import serializers
from vortaro.app.api.permissions import OwnerPermisson
from vortaro.app.models import Word, User


class WordList(generics.ListCreateAPIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (OwnerPermisson,)
    model = Word
    serializer_class = serializers.WordSerializer

    def get_queryset_(self):
        if self.request.QUERY_PARAMS.get('refresh', None):
            last_requested = None
        else:
            last_requested = self.request.session.get('last_requested', None)
        if last_requested and isinstance(last_requested, datetime.datetime):
            result = Word.objects.filter(date_modified__gt=last_requested)
        else:
            result = Word.objects.all()
        self.request.session['last_requested'] = datetime.datetime.now()
        return result


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnerPermisson,)
    model = Word
    serializer_class = serializers.WordSerializer


class UserList(generics.ListAPIView):
    model = User
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = User
    serializer_class = serializers.UserSerializer


class Me(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = serializers.UserSerializer

    def get_object(self, queryset=None):
        return self.request.user


class Auth(APIView):
    def get(self, request, *args, **kwargs):
        return Response(self.request.user.is_authenticated())


class CSRF(APIView):
    def get(self, request, *args, **kwargs):
        from django.middleware.csrf import get_token

        token = get_token(request)
        return Response(token)