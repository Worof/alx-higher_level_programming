#!/usr/bin/python3
from ...models.base import Base
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.base import Base
"""
Unit test for the Base class
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class
    """

    def test_something(self):
        """
        Test something about the Base class
        """
        self.assertEqual(True, True)  # Example test

if __name__ == '__main__':
    unittest.main()
