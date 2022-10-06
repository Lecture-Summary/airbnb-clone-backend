from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {"rooms": rooms, "title": "Hello! this title comes from django!"},
    )


def see_one_rooms(request, room_id, room_name):
    return HttpResponse(f"see room with id: {room_id} {room_name}")
