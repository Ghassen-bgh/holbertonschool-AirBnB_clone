#!/usr/bin/python3
"""Module to make tests"""
import unittest
import os
import uuid
import pep8
from datetime import datetime
from datetime import time
from models.base_model import BaseModel
import models
import json




class Test_BaseModel(unittest.TestCase):
    """ Class to test
    """

    def setUp(self):
        """Function that execute before of each test function
        """
        self.obj = BaseModel()

    def test_createBaseModel(self):
        """Test that is instance
        """
        self.assertIsInstance(self.obj, BaseModel)

    def test_Id_Is_String(self):
        """Id is string
        """
        self.assertEqual(type(self.obj.id), str)

    def test_add_Atrribute(self):
        self.obj.name = "Holberton"
        self.obj.my_number = 89
        self.assertTrue(self.obj.name)
        self.assertTrue(self.obj.my_number)

    def test_docString(self):
        """Test if function and class have docString
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_pep8_base_model(self):
        """ Test for PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_id_uuid_v4(self):
        """Test version 4 of UUID
        """
        test__version = uuid.UUID(self.obj.id).version
        self.assertEqual(test__version, 4, "Error: Different version")

    def test_created_at_Is_datatime(self):
        """Test that created_at is instance of datetime
        """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at_Is_datatime(self):
        """Test that updated_at is instance of datetime
        """
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_str(self):
        """ Test function __str__
        """
        s = "[{}] ({}) {}".format(
            self.obj.__class__.__name__, self.obj.id, self.obj.__dict__)
        self.assertEqual(self.obj.__str__(), s)

    def test_save(self):
        """Test save objects in a json file
        """
        self.obj.save()
        key = self.obj.__class__.__name__+"."+self.obj.id
        self.assertEqual(self.obj, models.storage.all()[key])
        self.assertNotEqual(self.obj.created_at, self.obj.updated_at)
        self.assertTrue(os.path.exists("file.json"))

    def test_save_content(self):
        """Test to compare the saved in json file with to_dic()"""
        self.obj.save()
        dict_to_load = {}
        with open("file.json", 'r') as f:
            dict_to_load = json.loads(f.read())
        self.assertDictEqual(
            self.obj.to_dict(), dict_to_load['BaseModel.' + self.obj.id])

    def test_to_dict(self):
        """Test to compare to two dictonary
        """
        new_dict = self.obj.__dict__.copy()
        new_dict["__class__"] = self.obj.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        self.assertDictEqual(new_dict, self.obj.to_dict())
        self.assertEqual(self.obj.to_dict()['__class__'], "BaseModel")
        self.assertEqual(type(self.obj).__name__, "BaseModel")
