from django.db import models

from django.contrib.auth.models import User


class Wishlist(models.Model):
    wishlistName = models.CharField(verbose_name='Name of wishlist', max_length=255)
    wishlistOwnerID = models.ForeignKey(User, on_delete=models.CASCADE)
    isSharedToOthers = models.BooleanField(verbose_name='Others can see current wishlist')

    def __str__(self):
        return self.wishlistName


class WishObject(models.Model):
    objectName = models.CharField(verbose_name='Name of the object', max_length=200)
    objectDescription = models.TextField(verbose_name='Describe of the object')
    reasonToHave = models.TextField(verbose_name='Why do you need this object')
    objectLocation = models.TextField(verbose_name='Where you can find this object')
    requirementsToDo = models.TextField(verbose_name='What you need to do for getting this object')
    wishlistId = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.objectName
