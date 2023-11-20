#!/usr/bin/python3
""" Module to test user class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Define the test for User class"""

    def __init__(self, *args, **kwargs):
        """Initialzing function """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test for the first_name type """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test for the last_name type """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test for the email type """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test for the value type"""
        new = self.value()
        self.assertEqual(type(new.password), str)
