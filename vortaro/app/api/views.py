from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from vortaro.app.api import serializers
from vortaro.app.models import Word, Category, User


class WordList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Word
    serializer_class = serializers.WordSerializer


class WordAdd(generics.CreateAPIView):
    parser_classes = (FileUploadParser,)
    model = Word
    serializer_class = serializers.WordAddSerializer


class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Category
    serializer_class = serializers.CategorySerializer


class WordDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Word
    serializer_class = serializers.WordSerializer

    def pre_save(self, obj):
        obj.user_modified = self.request.user


class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Category
    serializer_class = serializers.CategorySerializer


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