from django.contrib import admin
from common.models import Nav, WebSite


class NavAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name', 'create_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('sort',)

    # 进入编辑界面
    list_display_links = ('id', 'name')

    # list_editable 设置默认可编辑字段
    list_editable = []

    # fk_fields 设置显示外键字段
    # fk_fields = ('',)

    # 筛选器
    list_filter = ()  # 过滤器
    search_fields = ('title',)  # 搜索字段
    # date_hierarchy = 'create_time'  # 详细时间分层筛选　


class WebSiteAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'name')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)

    # 进入编辑界面
    list_display_links = ('id', 'name')

    # list_editable 设置默认可编辑字段
    list_editable = []

    # fk_fields 设置显示外键字段
    # fk_fields = ('',)

    # 筛选器
    # list_filter = ()  # 过滤器
    search_fields = ('name',)  # 搜索字段
    # date_hierarchy = 'create_time'  # 详细时间分层筛选　

    def has_add_permission(self, request):
        # 禁用添加按钮
            return False

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False



# 在admin中注册绑定
admin.site.register(Nav, NavAdmin)
# 在admin中注册绑定
admin.site.register(WebSite, WebSiteAdmin)