from django.test import TestCase
from users.models.user import User


class UsersModelsTestCase(TestCase):
    """ Test Case for User's app models """

    def setUp(self):
        self.user = User.objects.create(
            username='teste',
            email='teste@email.com',
            first_name='Teste',
            last_name='da Silva',
            password='12345678',
        )

    def test_if_user_is_created_correctly(self):
        self.assertEqual(self.user.username, 'teste')
        