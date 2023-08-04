from django.contrib import messages


def messages_success():
    messages.add_message(request, messages.SUCCESS, 'seccess')