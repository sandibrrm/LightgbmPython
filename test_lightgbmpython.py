# test_lightgbmpython.py
"""
Tests for LightgbmPython module.
"""

import unittest
from lightgbmpython import LightgbmPython

class TestLightgbmPython(unittest.TestCase):
    """Test cases for LightgbmPython class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LightgbmPython()
        self.assertIsInstance(instance, LightgbmPython)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LightgbmPython()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
