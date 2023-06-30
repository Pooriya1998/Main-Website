from django.shortcuts import render
from blog.models import Post


def index_view(requests):
    return render(requests, 'website/index.html')

