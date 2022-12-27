from django.test import TestCase, RequestFactory
from users.views import register, login


class UsersUrlsTestCase(TestCase):
    """ Test Case for User's app urls """

    def setUp(self):
        self.factory = RequestFactory()

    def test_if_register_route_utilize_register_view(self):
        request = self.factory.get('register/')
        with self.assertTemplateUsed('users/register.html'):
            response = register(request)
            self.assertEqual(response.status_code, 200)

    def test_if_login_route_utilize_login_view(self):
        request = self.factory.get('login/')
        with self.assertTemplateUsed('users/login.html'):
            response = login(request)
            self.assertEqual(response.status_code, 200)
