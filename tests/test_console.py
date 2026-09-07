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


class TestHBNBCommand_show(unittest.TestCase):
    """Tests for the show command in HBNBCommand."""

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

    def test_show_missing_class(self):
        """Test output when no class name is provided."""
        expected = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_show_invalid_class(self):
        """Test output when an invalid class name is provided."""
        expected = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show FakeClass 123")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_show_missing_id(self):
        """Test output when instance id is missing."""
        expected = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_show_no_instance_found(self):
        """Test output when the instance id does not exist."""
        expected = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel fake-id-123")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_show_valid(self):
        """Test showing a valid existing instance."""
        with patch('sys.stdout', new=StringIO()) as create_out:
            HBNBCommand().onecmd("create BaseModel")
        obj_id = create_out.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as show_out:
            HBNBCommand().onecmd("show BaseModel {}".format(obj_id))

        out_str = show_out.getvalue().strip()
        expected_prefix = "[BaseModel] ({})".format(obj_id)
        self.assertTrue(out_str.startswith(expected_prefix))


class TestHBNBCommand_destroy(unittest.TestCase):
    """Tests for the destroy command in HBNBCommand."""

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

    def test_destroy_missing_class(self):
        """Test output when no class name is provided."""
        expected = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_destroy_invalid_class(self):
        """Test output when an invalid class name is provided."""
        expected = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy FakeClass 123")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_destroy_missing_id(self):
        """Test output when instance id is missing."""
        expected = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_destroy_no_instance_found(self):
        """Test output when the instance id does not exist."""
        expected = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel fake-id-123")
        self.assertEqual(output.getvalue().strip(), expected)

    def test_destroy_valid(self):
        """Test destroying an instance removes it from storage."""
        with patch('sys.stdout', new=StringIO()) as create_out:
            HBNBCommand().onecmd("create BaseModel")
        obj_id = create_out.getvalue().strip()
        key = "BaseModel.{}".format(obj_id)
        self.assertIn(key, storage.all())

        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd("destroy BaseModel {}".format(obj_id))

        self.assertNotIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
