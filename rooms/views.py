from django.http import HttpResponse


def see_all_rooms(request):
    return HttpResponse("see all rooms")


def see_one_rooms(request, room_id, room_name):
    return HttpResponse(f"see room with id: {room_id} {room_name}")
