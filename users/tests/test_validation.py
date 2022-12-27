from django.test import TestCase
from users.validation import Validation


class ValidationTestCase(TestCase):
    """ Test Case for User's app validation """

    def setUp(self):
        self.length_incorrect_password = '123'
        self.spaces_incorrect_password = '        '
        self.correct_password = '12345678'
        self.error_list = {}

    def test_if_password_not_contain_spaces_validation_is_alright(self):
        Validation.validate_password(self.spaces_incorrect_password, 'password', self.error_list)
        self.assertEqual(list(self.error_list.values()), ['Password must not contain spaces!'])

    def test_if_password_lenght_is_higher_then_8(self):
        Validation.validate_password(self.length_incorrect_password, 'password', self.error_list)
        self.assertEqual(list(self.error_list.values()), ['Password lenght must be higher than 8 digits!'])
