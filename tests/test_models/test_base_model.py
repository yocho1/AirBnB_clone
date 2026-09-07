#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel."""

    def test_id_is_str(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_two_ids_are_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_is_datetime(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_save_updates_updated_at(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_to_dict_contains_class_key(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")

    def test_to_dict_datetimes_are_strings(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
