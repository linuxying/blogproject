#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 脚本描述：自定义模板标签，我们只要在模板中写入 {% get_recent_posts as recent_post_list %}，
# 那么模板中就会有一个从数据库获取的最新文章列表，并通过 as 语句保存到 recent_post_list 模板变量里。
# 这样我们就可以通过 {% for %} {% endfor%} 模板标签来循环这个变量，显示最新文章列表了，这和我们在编
# 写博客首页面视图函数是类似的，用于获取最新文章，分类等，使用可以参考base.html模板中相应的标签。


from django import template
from blog.models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag()
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag()
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag()
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

