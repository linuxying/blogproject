#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views
# 加入app_name可以让程序知道命名空间，找到blog位置
app_name = 'comments'

urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
