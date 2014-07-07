import datetime
from django.http.response import HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from vortaro.app.api import serializers
from vortaro.app.api.permissions import OwnerPermisson, IsAdminUser
from vortaro.app.models import Word, User
from django.db import connection


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


class Orders(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        """
        UPDATE "app_word"
        SET "order" = CASE "id"
            WHEN 8 THEN 1
            WHEN 11 THEN 2
        END
        WHERE id IN(7, 8);
        """
        data = request.DATA
        sql_query_1 = 'UPDATE "app_word" SET "order" = CASE "id" '
        sql_query_2 = 'WHERE id IN('
        for word_id in data:
            order = int(request.DATA[word_id][0])
            sql_query_1 += 'WHEN {} THEN {} '.format(word_id, order)
            sql_query_2 += "{}, ".format(word_id)
        sql_query_1 += 'END '
        sql_query_2 = sql_query_2[:-2]
        sql_query_2 += ');'
        sql_query = sql_query_1 + sql_query_2

        cursor = connection.cursor()
        cursor.execute(sql_query)
        cursor.close()
        return HttpResponse('ok')


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