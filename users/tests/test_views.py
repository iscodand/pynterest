from django.test import TestCase, RequestFactory
from users.views import register, login
from users.models import User
from django.urls import reverse


class UserViewsTestCase(TestCase):
    """ Test Case for User's app views """ 

    def setUp(self):
        self.factory = RequestFactory()
        self.username = 'test_username'
        self.email = 'test@email.com'
        self.first_name = 'first'
        self.last_name = 'last'
        self.password = '12345678'

    def test_if_register_view_is_registering_user_correctly(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
        })
        
        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        # self.assertEqual(response.status_code, 200)

    def test_if_login_view_is_logining_correctly(self):
        response = self.client.post(reverse('login'), data={
            'username': 'iscodand',
            'password': '12345678'
        }, follow=True)
        
        self.assertTrue(response.context['request'].user.is_authenticated)
