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


def set_posts_list():
    posts = Post.objects.filter(status=1)
    posts_list = [post for post in posts]
    return posts_list


def get_index_post(my_post):
    posts = Post.objects.filter(status=1)
    posts_list = [post.title for post in posts]
    for post in posts_list:
        if post == my_post:
            return posts_list.index(post)


def has_next_index(index_my_post):
    posts_list = set_posts_list()
    if len(posts_list) > index_my_post + 1:
        return True
    else:
        return False


def has_previous_index(my_post):
    posts_list = set_posts_list()
    if posts_list.index(my_post) == 0:
        return False
    else:
        return True


