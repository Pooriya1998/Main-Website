from django.shortcuts import render


def index_view(requests):
    return render(requests, 'website/index.html')


def blog_view(requests):
    return render(requests, 'blog/blog.html')
