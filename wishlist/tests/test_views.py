from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from rest_framework import status
import json

from wishlist.models import Wishlist, WishObject


WISHLIST_URL = reverse('wishlist:all_wishlists')


class WishlistViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(username='admintest', password='admintest')
        self.client.login(username='admintest', password='admintest')
        self.payload = {
            'id': 500,
            'wishlistName': 'Test name',
            'wishlistOwnerID': self.user.id,
            'isSharedToOthers': True,
        }
        self.client.post(WISHLIST_URL, self.payload)

    def test_create(self):
        response = self.client.post(WISHLIST_URL, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        response = self.client.get(WISHLIST_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateWishlistTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='admintest', password='admintest')
        self.client.login(username='admintest', password='admintest')
        self.wishlist = Wishlist.objects.create(
            wishlistName='TestName', wishlistOwnerID=self.user, isSharedToOthers=True)
        self.valid_payload = {
            'wishlistName': 'TestName2',
            'wishlistOwnerID': self.user.id,
            'isSharedToOthers': True
        }

    def test_update_data(self):
        response = self.client.put(
            reverse('wishlist:current_wishlist', kwargs={'pk': self.wishlist.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteWishlistTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='admintest', password='admintest')
        self.client.login(username='admintest', password='admintest')
        self.wishlist = Wishlist.objects.create(
            wishlistName='TestName', wishlistOwnerID=self.user, isSharedToOthers=True)

    def test_delete_data(self):
        response = self.client.delete(
            reverse('wishlist:current_wishlist', kwargs={'pk': self.wishlist.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GetCreateWishObjectsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='admintest', password='admintest')
        self.client.login(username='admintest', password='admintest')
        self.wishlist = Wishlist.objects.create(
            wishlistName='TestName', wishlistOwnerID=self.user, isSharedToOthers=True)
        self.WISHOBJECTS_URL = reverse('wishlist:all_wishObjects', kwargs={'fk': self.wishlist.pk})
        self.payload = {
            'id': 500,
            'objectName': 'TestName',
            'objectDescription': 'Test Descr',
            'reasonToHave': 'Test Descr',
            'objectLocation': 'Test Descr',
            'requirementsToDo': 'Test Descr',
            'wishlistId': self.wishlist.pk
        }


    def test_create_wishObject(self):
        response = self.client.post(self.WISHOBJECTS_URL, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_wishObject(self):
        response = self.client.get(self.WISHOBJECTS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateDeleteWishObjectsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='admintest', password='admintest')
        self.client.login(username='admintest', password='admintest')
        self.wishlist = Wishlist.objects.create(
            wishlistName='TestName', wishlistOwnerID=self.user, isSharedToOthers=True)
        self.WISHOBJECTS_URL = reverse('wishlist:all_wishObjects', kwargs={'fk': self.wishlist.pk})
        self.valid_payload = {
            'id': 500,
            'objectName': 'TestName',
            'objectDescription': 'Test Descr',
            'reasonToHave': 'Test Descr',
            'objectLocation': 'Test Descr',
            'requirementsToDo': 'Test Descr',
            'wishlistId': self.wishlist.pk
        }
        self.wishObject = WishObject.objects.create(
            objectName='TestName',
            objectDescription='Test Descr',
            reasonToHave='Test Descr',
            objectLocation='Test Descr',
            requirementsToDo='Test Descr',
            wishlistId=self.wishlist
        )

        self.CURRENT_WISHOBJECT_URL = reverse(
            'wishlist:current_wishObject',
            kwargs={'pk': self.wishObject.pk, 'fk': self.wishlist.pk}
        )

    def test_put_wishObject(self):
        response = self.client.put(
            self.CURRENT_WISHOBJECT_URL,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_wishObject(self):
        response = self.client.delete(self.CURRENT_WISHOBJECT_URL)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)