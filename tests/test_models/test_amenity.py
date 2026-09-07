#!/usr/bin/python3
"""Unit tests for Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_inheritance(self):
        """Test Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_attributes(self):
        """Test Amenity attributes exist"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_type(self):
        """Test Amenity attribute type"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
