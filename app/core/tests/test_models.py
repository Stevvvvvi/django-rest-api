from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        "test creating a new user with an email is successful"
        email='test@gmail.com'
        password='test123456'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        "test user email is normalized"
        email='test@GMAIL.com'
        password='test45678'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid_email(self):
        "test creating user with no email raises error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        "test creating a new superuser"
        user=get_user_model().objects.create_superuser(
            'testsuperuser@gmail.com',
            'test10293845'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)