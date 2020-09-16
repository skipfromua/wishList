from django.contrib.auth.models import User

from wishlist.models import Wishlist, WishObject


def form_context_for_unauthenticated_users(context):
    context.update(
        {
            'message': 'To use api you must login first'
        }
    )
    return context


def form_context_for_authenticated_users(context, user):
    user_id = User.objects.get(username=user).id
    wishlists = Wishlist.objects.filter(wishlistOwnerID=user_id)
    shared_wishlists = _find_shared_wishlists(user_id)
    context.update(
        {
            'username': user,
            'user_id': user_id,
            'your_wishlists': wishlists,
            'shared_wishlists': shared_wishlists,
        }
    )
    return context


def post_request(request):
    context = {}
    if request.method == 'POST':
        needed_object = _find_object_in_selected_wishlist(request)
        if needed_object:
            if request.user.id == _get_wishlist_owner_by_requested_id(request):
                my_new_object = _create_same_object_for_another_wishlist(request, needed_object)
                my_new_object.save()
                context.update({'status_msg': 'You successfully added object into one of your wishlists'})
            else:
                context.update({'status_msg': 'You cant add object into wishlists which is don`t belong to you =('})
        else:
            context.update({'status_msg': 'Cannot find specified object =('})
    return context


def _get_wishlist_owner_by_requested_id(request):
    return Wishlist.objects.filter(id=int(request.POST['wishlist_to'])).values('wishlistOwnerID')[0]['wishlistOwnerID']


def _find_shared_wishlists(user_id):
    return Wishlist.objects.filter(isSharedToOthers=True) & \
           Wishlist.objects.exclude(wishlistOwnerID=user_id)


def _find_object_in_selected_wishlist(request):
    return WishObject.objects.filter(id=int(request.POST['wishObject'])) & \
           WishObject.objects.filter(wishlistId=int(request.POST['wishlist_from']))


def _create_same_object_for_another_wishlist(request, needed_object):
    return WishObject.objects.create(
        objectName=needed_object.values('objectName')[0]['objectName'],
        objectDescription=needed_object.values('objectDescription')[0]['objectDescription'],
        reasonToHave=needed_object.values('reasonToHave')[0]['reasonToHave'],
        objectLocation=needed_object.values('objectLocation')[0]['objectLocation'],
        requirementsToDo=needed_object.values('requirementsToDo')[0]['requirementsToDo'],
        wishlistId=Wishlist.objects.get(id=int(request.POST['wishlist_to']))
    )


