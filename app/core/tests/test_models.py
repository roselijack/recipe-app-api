from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = '879655709@qq.com'
        password = 'hkbb090403...'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_nomalize(self):
        email = 'hongzhen.li@QQ.COM'
        password = 'rose123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_email_invalid(self):
        """test creating user with no email will raise error"""
        with self.assertRaises(ValueError):
            password = 'rose123'
            get_user_model().objects.create_user(
                email='',
                password=password
            )

    def test_create_superuser_successful(self):
        email = '879655709@qq.com'
        password = 'hkbb090403...'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertEqual(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)
