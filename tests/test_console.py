#!/usr/bin/python3
"""
Unittest for console command interpreter

"""

import errno
from tkinter.ttk import Style
from tokenize import String
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):
    """unittest for command Interpreter"""
    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()


    @classmethod
    def tearDownClass(self):
        """Remove temporary file in file.json created as a result """
        try:
            os.remove("file.json")
        except:
            pass

        """Check for pep8 style conformance"""
        def test_pep8_console(self):
            """pep8 test_console.py"""
            style = pep8.StyleGuide(quiet = False)
            errors = 0
            file = (["tests/test_console.py"])
            errors += style.check_files(file).total_errors
            self.assertEqual(errors, 0, 'Need to fix pep8')

            """check for docstring existence"""
            def test_docstrings_in_console(self):
                """Test docstrings existence in console.py"""
                self.assertTrue(len(console.__doc__)>= 1)

            def test_docstrings_in_test_console(self):
                """Test docstrings existence in test_console.py"""
                self.assertTrue(len(console.__doc__)>= 1)

            """Test command interpreter outputs"""
            def test_emptylines(self):

                '''Test no user inputs'''
                with patch('sys.stdout', new = StringIO()) as fake_Output

