from django.urls import path
from Chat.views import *

app_name = 'chat_app'

urlpatterns = [
    path('', chat_view, name='chat'),
    path('<str:room_name>/', room_view, name='room'),
]