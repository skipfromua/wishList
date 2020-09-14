from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse


def main(request):
    user = get_user(request)
    try:
        user_id = User.objects.get(username=user).id
        return HttpResponse('Hello {}, your id is {}'.format(user, user_id))
    except ObjectDoesNotExist:
        return HttpResponse('Hello, to use wishlists you must login first')