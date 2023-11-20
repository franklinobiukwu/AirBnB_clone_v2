#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Test for user model """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_lastname_value_no_underscores(self):
        """
        Test the lastname for a User instance
        not containing underscores
        """
        new = self.value()
        new.last_name = "\"Jake\""
        new.last_name = __import__("console")\
            .HBNBCommand\
            .find_type(new.last_name)[0]
        self.assertEqual("Jake", new.last_name)

    def test_lastname_value_with_underscores(self):
        """
        Test the lastname for a user instance
        containing underscores
        """
        new = self.value()
        new.last_name = "\"Ann_Ansu\""
        new.last_name = __import__("console")\
            .HBNBCommand\
            .find_type(new.last_name)[0]
        self.assertEqual("Ann Ansu", new.last_name)

    def test_lastname_type(self):
        """ Test the type for lastname attribute """
        new = self.value()
        new.last_name = "\"Kofi\""
        new.last_name = __import__("console")\
            .HBNBCommand\
            .find_type(new.last_name)[0]
        self.assertTrue(type(new.last_name) is str)