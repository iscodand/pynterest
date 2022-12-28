from django.test import TestCase
from users.validation import Validation
from users.models.user import User


class ValidationTestCase(TestCase):
    """ Test Case for User's app validation """

    def setUp(self):
        self.length_incorrect_password = '123'
        self.spaces_incorrect_password = '        '
        self.correct_password = '12345678'
        self.error_list = {}
        self.username = 'test_username'
        self.email = 'test@email.com'
        self.user = User.objects.create(
            username= 'test_username',
            email= 'test@email.com',
            first_name= 'first',
            last_name= 'last',
            password= '12345678'
        )

    def test_if_password_not_contain_spaces_validation_is_alright(self):
        Validation.validate_password(self.spaces_incorrect_password, 'password', self.error_list)
        self.assertEqual(list(self.error_list.values()), ['Password must not contain spaces!'])

    def test_if_password_lenght_is_higher_then_8(self):
        Validation.validate_password(self.length_incorrect_password, 'password', self.error_list)
        self.assertEqual(list(self.error_list.values()), ['Password lenght must be higher than 8 digits!'])

    def test_if_username_is_unique(self):
        Validation.validate_unique_username(self.username, 'username', self.error_list)
        self.assertEqual(list(self.error_list.values()), ['Username already in use! Change and try again.'])

    def test_if_email_is_unique(self):
        Validation.validate_unique_email(self.email, 'email', self.error_list)
        self.assertEqual(list(self.error_list.values()), ['E-mail already in use! Change and try again.'])
