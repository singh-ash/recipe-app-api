from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_ceste_user_with_email_successful(self):
        """Test Create user with email"""
        email = 'test@ashsinghdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """New user is normalized"""
        email = 'test@ASHSINGDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_username_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser('test@ASHSINGDEV.COM', 'test123')
        self.assertTrue(user.is_superuser)


