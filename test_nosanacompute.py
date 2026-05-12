# test_nosanacompute.py
"""
Tests for NosanaCompute module.
"""

import unittest
from nosanacompute import NosanaCompute

class TestNosanaCompute(unittest.TestCase):
    """Test cases for NosanaCompute class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NosanaCompute()
        self.assertIsInstance(instance, NosanaCompute)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NosanaCompute()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
