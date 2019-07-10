import importlib
import os
import unittest
from unittest import TestCase, mock
from unittest.mock import patch

devnull = open(os.devnull, 'w')
# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('sys.stdout', devnull):
    with patch('sys.stderr', devnull):
        import code.script


def reload_module(module):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            return importlib.reload(module)


class Task2B(TestCase):
    """
    Task 2.b
    """

    # Reloads the module with the same user input each time
    def setUp(self):
        self.exercise = reload_module(code.script)

    def test_doghouse(self):
        self.assertTrue(hasattr(self.exercise, "dog"), "You must declare 'dog'")
        self.assertTrue(hasattr(self.exercise, "house"), "You must declare 'house'")
        self.assertEqual(self.exercise.dog, "dog", "'dog' value seems wrong")
        self.assertEqual(self.exercise.house, "house", "'house' value seems wrong")


if __name__ == '__main__':
    unittest.main(verbosity=0)
