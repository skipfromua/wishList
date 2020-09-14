from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from wishlist.models import Wishlist


def main(request):
    user = get_user(request)
    try:
        user_id = User.objects.get(username=user).id
        context = {
            'username': user,
            'user_id': user_id
        }
        return render(request, 'main/main.html', context)
    except ObjectDoesNotExist:
        context = {
            'message': 'To use api you must login first'
        }
        return render(request, 'main/main.html', context)