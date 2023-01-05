"""
Tests for models layer.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests for Models."""

    def test_create_user_success(self):
        """Test creating user with username, email and password is successful."""
        username = 'user_name'
        email = 'user@example.com'
        password = 'password123'

        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized_for_new_users(self):
        """Test if email is normalized."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com', 'user1'],
            ['Test2@Example.com', 'Test2@example.com', 'user2'],
            ['TEST3@example.COM', 'TEST3@example.com', 'user3'],
            ['test4@EXAMPLE.COM', 'test4@example.com', 'user4']
        ]

        for email, expected, username in sample_emails:
            user = get_user_model().objects.create_user(
                username=username,
                email=email,
                password='password123'
            )

            self.assertEqual(user.email, expected)

    def test_user_without_username_raises_error(self):
        """Test if user without username raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username='',
                email='user@example.com',
                password='password123'
            )

    def test_user_without_email_raises_error(self):
        """Test if user without email raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username='user_name',
                email='',
                password='password123'
            )

    def test_create_superuser_successful(self):
        """Test if create new superuser if successful."""
        superuser = get_user_model().objects.create_superuser(
            username='superuser',
            email='superuser@example.com',
            password='password123'
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
