from django.shortcuts import render


def chat_view(requests):
    return render(requests, 'Chat/chat.html')


def room_view(requests, room_name):
    context = {'room_name': room_name}
    return render(requests, 'Chat/room.html', context)