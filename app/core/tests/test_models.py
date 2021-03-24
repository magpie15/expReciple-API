from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

	def test_create_user_with_email_successful(self):
		"""Test creating a new user with an email is succesful"""
		email = "test@magpie.com"
		password = "TestItUp123"
		user = get_user_model().objects.create_user(
			email=email,
			password=password

		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalized(self):
		"""Test the email for a new user is normalized"""
		email = 'test@MAGPIE.COM'
		user = get_user_model().objects.create_user(email, 'TestItUp123')

		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises error"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'TestItUp123')

	def test_create_new_superuser(self):
		"""Test creating a new superuser"""
		user = get_user_model().objects.create_superuser(
			'testSuper@magpie.com',
			'TestItUp123'

		)

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)