from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.test.client import RequestFactory

from main.services import form_context_for_unauthenticated_users, _get_wishlist_owner_by_requested_id, \
    _find_shared_wishlists, form_context_for_authenticated_users, _find_object_in_selected_wishlist, \
    _create_same_object_for_another_wishlist

from wishlist.models import Wishlist, WishObject


class ServicesTest(TestCase):
    def setUp(self):
        self.context = {}
        self.client = Client()
        data = {
            'wishObject': 500,
            'wishlist_from': 500,
            'wishlist_to': 500,
        }

        self.request = RequestFactory().post('main', data)
        self.user = get_user_model().objects.create_superuser(username='admintest', password='admintest')
        self.client.login(username='admintest', password='admintest')
        self.newWishlist = Wishlist.objects.create(
            id=500,
            wishlistName='TestWishlist',
            wishlistOwnerID=self.user,
            isSharedToOthers=True
        )
        self.newWishObject = WishObject.objects.create(
            id=500,
            objectName='TestName',
            objectDescription='Test Descr',
            reasonToHave='Test Descr',
            objectLocation='Test Descr',
            requirementsToDo='Test Descr',
            wishlistId=self.newWishlist
        )

    def test_form_context_for_unauthenticated_users(self):
        valid_output = {
            'message': 'To use api you must login first'
        }
        self.assertEqual(form_context_for_unauthenticated_users(self.context), valid_output)

    def test_get_wishlist_owner_by_requested_id(self):
        self.assertEqual(_get_wishlist_owner_by_requested_id(self.request), self.user.id)

    def test_find_shared_wishlists(self):
        self.assertEqual(_find_shared_wishlists(self.user.id + 1)[0], self.newWishlist)

    def test_find_object_in_selected_wishlist(self):
        self.assertEqual(_find_object_in_selected_wishlist(self.request)[0], self.newWishObject)

    def test_create_same_object_for_another_wishlist(self):
        wishObject = WishObject.objects.all()
        self.assertEquals(_create_same_object_for_another_wishlist(
                self.request,
                wishObject
            ),
            WishObject.objects.filter(id=1)[0]
        )