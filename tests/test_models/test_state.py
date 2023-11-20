#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test for state model """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_value_no_underscores(self):
        """
        Test the value for a state instance
        not containing underscores
        """
        new = self.value()
        new.name = "\"California\""
        new.name = __import__("console")\
            .HBNBCommand\
            .find_type(new.name)[0]
        self.assertEqual("California", new.name)

    def test_name_value_with_underscores(self):
        """
        Test the value for a state instance
        containing underscores
        """
        new = self.value()
        new.name = "\"Sing_me_a_song\""
        new.name = __import__("console")\
            .HBNBCommand\
            .find_type(new.name)[0]
        self.assertEqual("Sing me a song", new.name)

    def test_name_type(self):
        """ Test the type for name attribute """
        new = self.value()
        new.name = "\"Caliornia\""
        new.name = __import__("console")\
            .HBNBCommand\
            .find_type(new.name)[0]
        self.assertTrue(type(new.name) is str)