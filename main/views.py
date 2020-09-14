from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from wishlist.models import Wishlist, WishObject


def main(request):
    if request.method == 'POST':
        needed_object = WishObject.objects.filter(id=int(request.POST['wishObject'])) & \
                        WishObject.objects.filter(wishlistId=int(request.POST['wishlist_from']))
        needed_object.update(wishlistId=int(request.POST['wishlist_to']))

    user = get_user(request)
    try:
        user_id = User.objects.get(username=user).id
        wishlists = Wishlist.objects.filter(wishlistOwnerID=user_id)
        shared_wishlists = Wishlist.objects.filter(isSharedToOthers=True) & \
                           Wishlist.objects.exclude(wishlistOwnerID=user_id)
        context = {
            'username': user,
            'user_id': user_id,
            'your_wishlists': wishlists,
            'shared_wishlists': shared_wishlists,
        }
        return render(request, 'main/main.html', context)
    except ObjectDoesNotExist:
        context = {
            'message': 'To use api you must login first'
        }
        return render(request, 'main/main.html', context)