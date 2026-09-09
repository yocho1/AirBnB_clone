#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def test_init(self):
        """Test BaseModel initialization"""
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test string representation"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_save(self):
        """Test save method updates updated_at and calls storage.save"""
        old_updated = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        dict_rep = self.model.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertIn('__class__', dict_rep)
        self.assertEqual(dict_rep['__class__'], 'BaseModel')
        self.assertIn('created_at', dict_rep)
        self.assertIn('updated_at', dict_rep)
        self.assertIsInstance(dict_rep['created_at'], str)
        self.assertIsInstance(dict_rep['updated_at'], str)

    def test_kwargs_init(self):
        """Test initialization with kwargs from dictionary"""
        dict_rep = self.model.to_dict()
        new_model = BaseModel(**dict_rep)
        self.assertEqual(self.model.id, new_model.id)

    def test_kwargs_skip_class(self):
        """Test that __class__ is skipped in kwargs"""
        dict_rep = self.model.to_dict()
        new_model = BaseModel(**dict_rep)
        self.assertNotIn('__class__', new_model.__dict__)
