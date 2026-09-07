#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_inheritance(self):
        """Test State inherits from BaseModel"""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_attributes(self):
        """Test State attributes exist"""
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_type(self):
        """Test State attribute type"""
        state = State()
        self.assertIsInstance(state.name, str)
