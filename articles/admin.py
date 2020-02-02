from django.contrib import admin
from articles.models import Article, ArticleType


class ArticleAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'title', 'create_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-create_time',)

    # 进入编辑界面
    list_display_links = ('id', 'title')

    # list_editable 设置默认可编辑字段
    list_editable = []

    # fk_fields 设置显示外键字段
    # fk_fields = ('',)

    # 筛选器
    list_filter = ('create_time', )  # 过滤器
    search_fields = ('title',)  # 搜索字段
    # date_hierarchy = 'create_time'  # 详细时间分层筛选　


class ArticleTypeAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'create_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-create_time',)

    # 进入编辑界面
    list_display_links = ('id', 'name')

    # list_editable 设置默认可编辑字段
    list_editable = []

    # fk_fields 设置显示外键字段
    # fk_fields = ('',)

    # 筛选器
    # list_filter = ('create_time', )  # 过滤器
    search_fields = ('name',)  # 搜索字段
    # date_hierarchy = 'create_time'  # 详细时间分层筛选　


# 在admin中注册绑定
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
