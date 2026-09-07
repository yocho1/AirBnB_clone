#!/usr/bin/python3
"""Unit tests for the HBNB console."""
import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestHBNBCommand_create(unittest.TestCase):
    """Tests for the create command in HBNBCommand."""

    def setUp(self):
        """Reset storage and clear JSON file before each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        storage.all().clear()

    def tearDown(self):
        """Clean up JSON file after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_missing_class(self):
        """Test output when no class name is given."""
        expected = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_create_invalid_class(self):
        """Test output when an invalid class name is given."""
        expected = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create FakeClass")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_create_valid_class(self):
        """Test output and storage side effects for a valid create."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        generated_id = output.getvalue().strip()
        self.assertEqual(len(generated_id), 36)
        key = "BaseModel.{}".format(generated_id)
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
