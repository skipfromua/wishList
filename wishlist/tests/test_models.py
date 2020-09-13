from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from wishlist.models import Wishlist, WishObject


class WishTestlistCase(APITestCase):
    def setUp(self):
        self.TestUser = User.objects.create_user('TestUser')
        self.wishlist_test = Wishlist.objects.create(
            wishlistName='TestWishlist',
            wishlistOwnerID=self.TestUser,
            isSharedToOthers=False
        )
        self.wishObject_test = WishObject.objects.create(
            objectName='Test_object',
            objectDescription='Some description',
            reasonToHave='Some reason',
            objectLocation='Some location',
            requirementsToDo='Some requirements',
            wishlistId=self.wishlist_test
        )

    def test_str_wishObject(self):
        self.assertEqual(self.wishObject_test.__str__(), 'Test_object')

    def test_str_wishlist(self):
        self.assertEqual(self.wishlist_test.__str__(), 'TestWishlist')