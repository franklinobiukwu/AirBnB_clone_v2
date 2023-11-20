#!/usr/bin/python3
"""Module to test amenity ckass """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """Defines Test Class for Amenity class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test if name is string"""
        new = self.value()
        self.assertEqual(type(new.name), str)
