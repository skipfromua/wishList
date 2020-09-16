from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from main.services import form_context_for_unauthenticated_users


class ServicesTest(TestCase):
    def setUp(self):
        self.context = {}

    def test_form_context_for_unauthenticated_users(self):
        valid_output = {
            'message': 'To use api you must login first'
        }
        self.assertEqual(form_context_for_unauthenticated_users(self.context), valid_output)