from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from blog.management import *
import datetime


def blog_view(request):

    check_status()

    published_posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())
    all_cats = Category.objects.all()

    context = {'posts': published_posts, 'all_cats': all_cats}
    return render(request, 'blog/blog.html', context)


def blog_single_view(request, pid):

    add_counted_views(pid)

    post = get_object_or_404(Post, pk=pid, status=1)
    all_cats = Category.objects.all()

    context = {'post': post, 'all_cats': all_cats}
    return render(request, 'blog/blog-single.html', context)


def blog_category_view(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)