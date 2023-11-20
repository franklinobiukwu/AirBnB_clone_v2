#!/usr/bin/python3
""" Module to test review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Define Test for The review class """

    def __init__(self, *args, **kwargs):
        """Intitilazing the args """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test the place_id type"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test the thype of the user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the type for text """
        new = self.value()
        self.assertEqual(type(new.text), str)
