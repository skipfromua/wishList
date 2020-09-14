from django.http.response import HttpResponse
from rest_framework import generics
from .serializers import WishlistDetailSerializer, WishlistListSerializer, \
                            WishObjectDetailSerializer, WishObjectListSerializer
from .models import Wishlist, WishObject
from .permissions import AuthorPermissions
from rest_framework import permissions


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


def WishObjectReserveView(request, to_wishlist_id):
    print('i am here')
    if str(request.user) != 'AnonymousUser':
        pk = 5
        to_wishlist = Wishlist.objects.filter(id=to_wishlist_id)
        current_wishObject = WishObject.objects.filter(id=pk)
        new_wishObject = WishObject(
            objectName=current_wishObject.objectName,
            objectDescription=current_wishObject.objectDescription,
            reasonToHave=current_wishObject.reasonToHave,
            objectLocation=current_wishObject.objectLocation,
            requirementsToDo=current_wishObject.requirementsToDo,
            wishlistId=to_wishlist.wishlistId
        )
        new_wishObject.save()
        return HttpResponse('Complete')
    else:
        HttpResponse('incomplete')
