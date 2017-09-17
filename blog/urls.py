#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from .feeds import AllPostsRssFeed
from django.views.static import serve
from blogproject import settings

# 加入app_name可以让程序知道命名空间，找到blog位置
app_name = 'blog'

urlpatterns = [
    # name使用方法可以看Post类下get_absolute_url方法说明
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^about/$', views.about, name='about'),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', views.upload_image, name='upload_image'),
    url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
