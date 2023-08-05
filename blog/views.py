from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.management import *
import datetime


def blog_view(request, **kwargs):
    check_status()

    posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    all_cats = Category.objects.all()
    context = {'posts': posts, 'all_cats': all_cats}
    return render(request, 'blog/blog.html', context)


def blog_single_view(request, pid):
    # In this section, a number is added to the view variable for each view.
    add_counted_views(pid)
    # In this section, a complete list of posts is prepared
    posts_list = set_posts_list()
    # Post, previous post and next post are defined in the same way by default.
    post = get_object_or_404(Post, pk=pid, status=1)
    next_post = get_object_or_404(Post, pk=pid, status=1)
    previous_post = get_object_or_404(Post, pk=pid, status=1)
    # In this section, the has_previous_post and has_next_post variables are defined as false by default.
    has_previous_post = False
    has_next_post = False
    # In this section, the exact location of the post can be found in the list of all posts
    index_post = get_index_post(post.title)

    # In this section, it is determined whether there is a next post or not.
    if has_next_index(index_post):
        ''' 
            If there is, the has_next_post variable is declared true and
            the post whose position is 1 higher in the list from the complete list of posts
            is stored in the next_post variable.
        '''
        has_next_post = True
        next_post = posts_list[index_post+1]

    # In this section, it is determined whether there is a previous post or not.
    if has_previous_index(post):
        '''
            If present, the has_previous_post variable is declared true and
            A post whose position in the list is 1 lower than the complete list of posts
            It is stored in the previous_post variable.
        '''
        has_previous_post = True
        previous_post = posts_list[index_post-1]

    all_cats = Category.objects.all()
    context = {'post': post, 'all_cats': all_cats,
               'next_post': next_post, 'has_next_post': has_next_post,
               'previous_post': previous_post, 'has_previous_post': has_previous_post}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)