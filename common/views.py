from django.shortcuts import render
from rest_framework.views import APIView
from common import models
from articles.models import ArticleType
from rest_framework.response import Response
from django.http import JsonResponse

from common.serializers import websiteSerializer, navSerializer


class Nav(APIView):
    def get(self, request):
        obj = models.Nav.objects.order_by("sort")
        # data = navSerializer(obj, many=True).data
        typeObj = ArticleType.objects.filter(isNav=True)
        dataList = []
        for j in typeObj:
            dataType = {}
            dataType['name'] = j.name
            dataType['url'] = '/type?typename='+j.name
            dataType['sort'] = -1
            dataList.append(dataType)
        for i in obj:
            data = {}
            data['name'] = i.name
            data['url'] = i.url
            data['sort'] = i.sort
            dataList.append(data)
        return JsonResponse(dataList, safe=False)


class WebSite(APIView):
    def get(self, request):
        obj = models.WebSite.objects.get(pk=1)
        data = websiteSerializer(obj).data
        return Response(data)
