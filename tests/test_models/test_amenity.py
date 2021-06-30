#!/usr/bin/python3
"""
        import modules of class AmenityTest
"""
import unittest
from models.amenity import Amenity
from datetime import datetime
import os
from models.base_model import BaseModel


class AmenityTest(unittest.TestCase):
    """test cases for class object Amenity"""

    @classmethod
    def setUp(self):
        """test instance"""
        self.t = Amenity()

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, BaseModel)

    def test_unique_id(self):
        """ test if it generate unique id"""
        Amenity1 = Amenity()
        Amenity2 = Amenity()
        self.assertNotEqual(Amenity1, Amenity2)

    def test_doc(self):
        """ test if class has docstring"""
        self.assertIsNotNone(amenity.Amenity.__doc__)
        self.assertIsNotNone(Amenity.__doc__)

if __name__ == "__main__":
    unittest.main()
