from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(requests):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(requests, 'blog/blog.html', context)
