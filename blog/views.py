from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime


def blog_view(requests):
    all_posts = Post.objects.all()
    published_posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())
    unpublished_posts = Post.objects.filter(published_date__gt=datetime.datetime.now())

    for post in all_posts:
        if post in published_posts:
            post.status = True
            post.save()
        else:
            post.status = False
            post.save()

    context = {'published_posts': published_posts, 'unpublished_posts': unpublished_posts}
    return render(requests, 'blog/blog.html', context)


def blog_single_view(requests, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(requests, 'blog/blog-single.html', context)


def test_view(requests):
    all_posts = Post.objects.all()
    published_posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())
    unpublished_posts = Post.objects.filter(published_date__gt=datetime.datetime.now())

    for post in all_posts:
        if post in published_posts:
            post.status = True
            post.save()
        else:
            post.status = False
            post.save()

    context = {'published_posts': published_posts, 'unpublished_posts': unpublished_posts}
    return render(requests, 'test.html', context)
