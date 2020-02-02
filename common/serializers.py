from rest_framework import serializers
from common import models


class websiteSerializer(serializers.ModelSerializer):
    class Meta:
        # 返回数据的数据模型
        model = models.WebSite
        # 返回的数据字段
        fields = "__all__"


class navSerializer(serializers.ModelSerializer):
    class Meta:
        # 返回数据的数据模型
        model = models.Nav
        # 返回的数据字段
        fields = "__all__"
