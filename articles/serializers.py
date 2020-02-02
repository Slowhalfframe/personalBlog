from rest_framework import serializers
from articles import models


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        # 返回数据的数据模型
        model = models.Article
        # 返回的数据字段
        fields = "__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        # 返回数据的数据模型
        model = models.Article
        # 返回的数据字段
        fields = ("id", 'title', 'desc', 'read_num', 'like_num', 'cove_img', 'articletype', 'create_time')