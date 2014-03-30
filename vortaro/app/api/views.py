from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from vortaro.app.api import serializers
from vortaro.app.models import Word, Category, User


class WordList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Word
    serializer_class = serializers.WordSerializer


class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Category
    serializer_class = serializers.CategorySerializer


class WordDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Word
    serializer_class = serializers.WordSerializer


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