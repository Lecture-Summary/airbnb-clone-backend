from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import WishList


class WishlistSerializer(ModelSerializer):
    rooms = RoomListSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = ("pk", "name", "rooms")
