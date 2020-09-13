from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from rest_framework import status


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
