# test_aiconverse.py
"""
Tests for AIConverse module.
"""

import unittest
from aiconverse import AIConverse

class TestAIConverse(unittest.TestCase):
    """Test cases for AIConverse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AIConverse()
        self.assertIsInstance(instance, AIConverse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AIConverse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
