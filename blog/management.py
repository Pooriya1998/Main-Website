from django.shortcuts import get_object_or_404
from blog.models import Post
import datetime


def check_status():
    all_posts = Post.objects.all()
    published_posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())

    for post in all_posts:
        if post in published_posts:
            post.status = True
            post.save()
        else:
            post.status = False
            post.save()


def add_counted_views(pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_views += 1
    post.save()