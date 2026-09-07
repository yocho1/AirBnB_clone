#!/usr/bin/python3
"""Unit tests for User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_inheritance(self):
        """Test User inherits from BaseModel"""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_attributes(self):
        """Test User attributes exist"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_types(self):
        """Test User attribute types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
