from django.shortcuts import render


def chat_view(request):
    return render(request, 'Chat/chat.html')


def room_view(request, room_name):
    context = {'room_name': room_name}
    return render(request, 'Chat/room.html', context)


def test_view(request):
    pass
