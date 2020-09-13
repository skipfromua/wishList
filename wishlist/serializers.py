from rest_framework import serializers
from .models import Wishlist, WishObject


class WishObjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishObject
        fields = '__all__'


class WishObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishObject
        fields = '__all__'


class WishlistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class WishlistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'