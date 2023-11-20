#!/usr/bin/python3
""" Module to test state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Define test module for State class """

    def __init__(self, *args, **kwargs):
        """ Initializing function"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the new Type for name """
        new = self.value()
        self.assertEqual(type(new.name), str)
