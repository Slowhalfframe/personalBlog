from django.shortcuts import render
from rest_framework.views import APIView
from articles import models
from rest_framework.response import Response
from django.http import JsonResponse

from articles.serializers import ArticleListSerializer
from articles.serializers import ArticleSerializer
import markdown


class Article(APIView):
    # 查询单篇文章详情
    def get(self, request):
        typename = request.GET.get('typename')
        print(typename)
        if typename:
            print('111')
            typeObj = models.ArticleType.objects.get(name=typename)
            articleList = models.Article.objects.filter(articletype=typeObj)
        else:
            print('222')
            articleList = models.Article.objects.all()
        # data = ArticleListSerializer(articleList, many=True).data
        dataList = []
        for i in articleList:
            data = {}
            data['id'] = i.id
            data['title'] = i.title
            data['desc'] = i.desc
            data['read_num'] = i.read_num
            data['like_num'] = i.like_num
            data['cove_img'] = str(i.cove_img)
            articleTypeObj = models.ArticleType.objects.get(pk=i.articletype_id)
            data['articletypename'] = articleTypeObj.name
            data['articletypeurl'] = "/type?typename=" + articleTypeObj.name
            data['create_time'] = i.create_time
            dataList.append(data)
        return JsonResponse(dataList, safe=False)


def detail(request, id):
    try:
        article = models.Article.objects.get(pk=id)
        article.read_num += 1
        article.save()
        article.content = markdown.markdown(article.content.replace("\r\n", "\n"), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ],safe_mode=True, enable_attributes=False)
        articleType = models.ArticleType.objects.get(pk = article.articletype.id)
        data = {
            "id": article.id,
            "title": article.title,
            'desc': article.desc,
            "content": article.content,
            "create_time": article.create_time,
            "read_num": article.read_num,
            "like_num": article.like_num,
            "articleTypeName": articleType.name,
            "articletypeurl": "/type?typename=" + articleType.name
        }
        return JsonResponse(data)
    except:
        return Response(status=404)


def like(request, id):
    articleObj = models.Article.objects.get(pk=id)
    articleObj.like_num += 1
    articleObj.save()
    return JsonResponse({"code": 0})