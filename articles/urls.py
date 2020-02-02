from django.conf.urls import url
from  articles import views

urlpatterns = [
    url(r'^article/$', views.Article.as_view(), name='article'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^like/(\d+)/$', views.like, name='like'),
]