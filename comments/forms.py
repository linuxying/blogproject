#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # model = Comment表明这个表单对应的数据模型是一个类
        model = Comment
        # fields指定了表单要显示的字段
        fields = ['name', 'email', 'url', 'text']
