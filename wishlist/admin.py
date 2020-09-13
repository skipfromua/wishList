from django.contrib import admin

from .models import Wishlist, WishObject


admin.site.register(WishObject)
admin.site.register(Wishlist)
