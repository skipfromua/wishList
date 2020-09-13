from django.http.response import HttpResponse
from rest_framework import generics
from .serializers import WishlistDetailSerializer, WishlistListSerializer, \
                            WishObjectDetailSerializer, WishObjectListSerializer
from .models import Wishlist, WishObject
from .permissions import AuthorPermissions
from rest_framework import permissions

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    user = get_user(request)
    try:
        user_id = User.objects.get(username=user).id
        return HttpResponse('Hello {}, your id is {}'.format(user, user_id))
    except ObjectDoesNotExist:
        return HttpResponse('Hello, to use wishlists you must login first')


class WishObjectListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = WishObjectListSerializer
    permission_classes = [AuthorPermissions]

    def get_queryset(self):
        print(self.kwargs)
        return WishObject.objects.filter(wishlistId=self.kwargs['fk'])


class WishObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishObjectDetailSerializer
    queryset = WishObject.objects.all()
    permission_classes = [AuthorPermissions]


class WishlistListView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = WishlistListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.id)
        return Wishlist.objects.filter(wishlistOwnerID=self.request.user.id) | \
               Wishlist.objects.filter(isSharedToOthers=True)


class WishlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishlistDetailSerializer
    queryset = Wishlist.objects.all()
    permission_classes = [AuthorPermissions]

