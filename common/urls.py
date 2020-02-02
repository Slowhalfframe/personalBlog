from django.conf.urls import url
from common import views

urlpatterns = [
    url(r'^nav/$', views.Nav.as_view(), name='nav'),
    url(r'^website/$', views.WebSite.as_view(), name='website'),
]