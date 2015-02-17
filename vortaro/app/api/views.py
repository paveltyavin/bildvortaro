import datetime
import json
from django.http.response import HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from vortaro.app.api import serializers
from vortaro.app.api.permissions import OwnerPermisson, IsAdminUser
from vortaro.app.models import Word, User, WordCategory
from django.db import connection


class WordList(generics.ListCreateAPIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (OwnerPermisson,)
    model = Word
    serializer_class = serializers.WordSerializer

    def get_queryset(self):
        qs = Word.objects.all()
        qs = qs.select_related().prefetch_related('categories')
        return qs


class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnerPermisson,)
    model = Word
    serializer_class = serializers.WordSerializer

    def _post_save(self, obj, created=False):
        categories_str = self.request.DATA['categories']
        categories = {int(key): value for key, value in categories_str.iteritems()}
        category_ids = categories.keys()
        word_id = self.request.DATA['id']
        wc_qs = WordCategory.objects.filter(category_id__in=category_ids, word_id=word_id)
        for wc in wc_qs:
            if wc.word_order != categories[wc.category_id]:
                wc.word_id = categories[wc.category_id]
                wc.save()
            del categories[wc.category_id]
        word_categories = []
        for category_id, word_order in categories.iteritems():
            word_categories.append(WordCategory(
                word_id=word_id,
                category_id=category_id,
                word_order=word_order
            ))
        if word_categories:
            WordCategory.objects.bulk_create(word_categories)


class Orders(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        """
        UPDATE "app_wordcategory"
        SET "word_order" = CASE "word_id"
            WHEN 8 THEN 1
            WHEN 11 THEN 2
        END
        WHERE word_id IN(7, 8) AND category_id = 4;
        """
        data = request.DATA
        category_id = data['category']
        sql_query_1 = 'UPDATE "app_wordcategory" SET "word_order" = CASE "word_id" '
        sql_query_2 = 'WHERE word_id IN('
        for word_id, order in data['orders'].iteritems():
            sql_query_1 += 'WHEN {} THEN {} '.format(word_id, order)
            sql_query_2 += "{}, ".format(word_id)
        sql_query_1 += 'END '
        sql_query_2 = sql_query_2[:-2]
        sql_query_2 += ') AND category_id = {};'.format(category_id)
        sql_query = sql_query_1 + sql_query_2

        cursor = connection.cursor()
        cursor.execute(sql_query)
        rowcount = cursor.cursor.rowcount
        cursor.close()
        return HttpResponse(json.dumps({'rowcount': rowcount}), mimetype='application/json')


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