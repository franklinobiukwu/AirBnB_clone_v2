#!/usr/bin/python3
""" Module to test City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Define tests for city class"""

    def __init__(self, *args, **kwargs):
        """Initializing function """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test the tyoe of state_id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the type f name """
        new = self.value()
        self.assertEqual(type(new.name), str)
