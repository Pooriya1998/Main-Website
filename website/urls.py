from django.urls import path
from website.views import *


urlpatterns = [
    path('', index_view),
    path('blog', blog_view)
]
