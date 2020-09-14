from django.shortcuts import render
from django.contrib.auth import get_user
from django.core.exceptions import ObjectDoesNotExist


from .services import form_context_for_unauthenticated_users, form_context_for_authenticated_users, post_request


def main(request):
    context = post_request(request)
    user = get_user(request)
    try:
        return render(request, 'main/main.html', form_context_for_authenticated_users(context, user))
    except ObjectDoesNotExist:
        return render(request, 'main/main.html', form_context_for_unauthenticated_users(context))


