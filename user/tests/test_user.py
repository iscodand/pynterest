"""
Test for user's app.
"""

from django.test import (
    TestCase,
    Client
)
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


REGISTER_USER_URL = reverse('user:register')
LOGIN_USER_URL = reverse('user:login')
# PROFILE_USER_URL = reverse('user:profile')

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserTest(TestCase):
    """Tests for user's public requests."""

    def setUp(self):
        self.client = Client()
        self.user = {
            'name': 'User Name',
            'username': 'user_name',
            'email': 'user@example.com',
            'password': 'password123'
        }

    def test_register_user_successful(self):
        """Test user is being registered successful."""
        response = self.client.post(REGISTER_USER_URL, self.user)

        user_exists = get_user_model().objects.get(
            username=self.user['username']
        )

        self.assertRedirects(response, LOGIN_USER_URL)
        self.assertEqual(user_exists.username, self.user['username'])
        self.assertEqual(user_exists.email, self.user['email'])
        self.assertTrue(user_exists.check_password(self.user['password']))

    def test_register_user_with_existent_data_raises_error(self):
        """Test email and username is unique."""
        create_user(**self.user)

        with self.assertRaises(IntegrityError):
            response = self.client.post(REGISTER_USER_URL, self.user)

    def test_register_user_with_password_too_short(self):
        """Test register user with password less than 8 chars."""
        self.user = {
            'name': 'User Name',
            'username': 'user_name',
            'email': 'user@example.com',
            'password': 'pass'
        }
        response = self.client.post(REGISTER_USER_URL, self.user)
        error_message = "Password too short."

        self.assertContains(response, error_message)


    def test_retrieve_unauthorized_user(self):
        """Test authentication is required for users."""
        pass
