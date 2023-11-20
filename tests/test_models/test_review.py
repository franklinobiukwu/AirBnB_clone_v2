#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test for review model """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_text_value_no_underscores(self):
        """
        Test the text for a review instance
        not containing underscores
        """
        new = self.value()
        new.text = "\"Good\""
        new.text = __import__("console")\
            .HBNBCommand\
            .find_type(new.text)[0]
        self.assertEqual("Good", new.text)

    def test_text_value_with_underscores(self):
        """
        Test the text for a state instance
        containing underscores
        """
        new = self.value()
        new.text = "\"Such_a_great_place.\""
        new.text = __import__("console")\
            .HBNBCommand\
            .find_type(new.text)[0]
        self.assertEqual("Such a great place.", new.text)

    def test_text_type(self):
        """ Test the type for text attribute """
        new = self.value()
        new.text = "\"Caliornia\""
        new.text = __import__("console")\
            .HBNBCommand\
            .find_type(new.text)[0]
        self.assertTrue(type(new.text) is str)