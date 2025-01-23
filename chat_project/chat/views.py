from django.shortcuts import render
from .models import Room, Message
from django.shortcuts import render

def room_view(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room)
    return render(request, 'room.html', {'room_name': room_name, 'messages': messages})


def chat_room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})
