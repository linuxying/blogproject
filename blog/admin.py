from django.contrib import admin
from blog.models import Post, Category, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']

    class Media:
        js = (
            'blog/js/kindeditor/kindeditor-all.js',
            'blog/js/kindeditor/lang/zh-CN.js',
            'blog/js/kindeditor/config.js',
        )

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
