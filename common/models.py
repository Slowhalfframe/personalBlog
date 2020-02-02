from django.db import models


class Nav(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name="导航名称")
    url = models.URLField(verbose_name="导航URL")
    display = models.BooleanField(default=1, verbose_name="显示状态")
    sort = models.IntegerField(default=0, verbose_name="排序", help_text="数值越大越靠前")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '导航'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class WebSite(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=22, verbose_name="网站名称")
    desc = models.CharField(max_length=256, verbose_name="二级名称/个签")
    record_info = models.CharField(max_length=20, verbose_name="备案信息")
    record_url = models.URLField(verbose_name="备案指向链接")
    display = models.BooleanField(default=1, verbose_name="显示状态")

    class Meta:
        verbose_name = '网站信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name