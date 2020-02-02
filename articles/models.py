from django.db import models
from mdeditor.fields import MDTextField


class ArticleType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="分类名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    isNav = models.BooleanField(default=0, verbose_name="是否显示在导航栏")

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, verbose_name="文章标题")
    desc = models.CharField(max_length=256, null=True, blank=True, verbose_name="文章摘要")
    # content = models.TextField(verbose_name="文章内容")
    content = MDTextField(verbose_name="文章内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    read_num = models.IntegerField(default=0, verbose_name="阅读量")
    like_num = models.IntegerField(default=0, verbose_name="喜欢量")
    cove_img = models.ImageField(upload_to='static/media/cover', null=True, blank=True, verbose_name="封面图片")
    articletype = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name="分类")

    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

