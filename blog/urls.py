from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single_view, name='single'),
    path('category/<str:cat_name>/', blog_category_view, name='category'),
]