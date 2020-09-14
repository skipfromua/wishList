from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from wishlist.models import Wishlist, WishObject


def main(request):
    context = {}
    if request.method == 'POST':
        needed_object = WishObject.objects.filter(id=int(request.POST['wishObject'])) & \
                        WishObject.objects.filter(wishlistId=int(request.POST['wishlist_from']))
        if needed_object:
            print(request.user.id)
            print(Wishlist.objects.filter(id=int(request.POST['wishlist_to'])).values('wishlistOwnerID'))
            if request.user.id == Wishlist.objects.filter(
                    id=int(request.POST['wishlist_to'])).values('wishlistOwnerID')[0]['wishlistOwnerID']:
                my_new_object = WishObject.objects.create(
                    objectName=needed_object.values('objectName')[0]['objectName'],
                    objectDescription=needed_object.values('objectDescription')[0]['objectDescription'],
                    reasonToHave=needed_object.values('reasonToHave')[0]['reasonToHave'],
                    objectLocation=needed_object.values('objectLocation')[0]['objectLocation'],
                    requirementsToDo=needed_object.values('requirementsToDo')[0]['requirementsToDo'],
                    wishlistId=Wishlist.objects.get(id=int(request.POST['wishlist_to']))
                )
                my_new_object.save()
                context.update({'status_msg': 'You successfully added object into one of your wishlists'})
            else:
                context.update({'status_msg': 'You cant add object into wishlists which is don`t belong to you =('})
        else:
            context.update({'status_msg': 'Cannot find specified object =('})

    user = get_user(request)
    try:
        user_id = User.objects.get(username=user).id
        wishlists = Wishlist.objects.filter(wishlistOwnerID=user_id)
        shared_wishlists = Wishlist.objects.filter(isSharedToOthers=True) & \
                           Wishlist.objects.exclude(wishlistOwnerID=user_id)
        context.update(
            {
                'username': user,
                'user_id': user_id,
                'your_wishlists': wishlists,
                'shared_wishlists': shared_wishlists,
            }
        )
        return render(request, 'main/main.html', context)
    except ObjectDoesNotExist:
        context.update(
            {
                'message': 'To use api you must login first'
            }
        )
        return render(request, 'main/main.html', context)