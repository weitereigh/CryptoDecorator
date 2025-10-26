# test_cryptodecorator.py
"""
Tests for CryptoDecorator module.
"""

import unittest
from cryptodecorator import CryptoDecorator

class TestCryptoDecorator(unittest.TestCase):
    """Test cases for CryptoDecorator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoDecorator()
        self.assertIsInstance(instance, CryptoDecorator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoDecorator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
