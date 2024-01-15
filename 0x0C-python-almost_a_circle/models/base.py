#!/usr/bin/python3
"""
Unit test for the Base class from models.base
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Defines Test Cases for the Base class from models.base
    """

    def test_id_assignment(self):
        """
        Test case for id assignment in Base class
        """
        obj1 = Base()
        obj2 = Base(12)
        self.assertIsNone(obj1.id)
        self.assertEqual(obj2.id, 12)

if __name__ == '__main__':
    unittest.main()
