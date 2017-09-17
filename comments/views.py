from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.
def post_comment(request, post_pk):
    # 通过post_pk获取文章，以为需要把评论和文章关联起来
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中，这是一个类字典对象
        # 我们利用这些数据构造CommentForm实例，这样django表单就生成了
        form = CommentForm(request.POST)
        # 当调用is_valid()时，django自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
            # 如果符合格式要求，调用表单的save方法保存数据到数据库
            # commit=False 的作用是仅仅利用表单的数据生成comment模型类的实例，但不保存评论数据到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            # 最终保存到数据库
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
