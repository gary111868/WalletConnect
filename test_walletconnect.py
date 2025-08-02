# test_walletconnect.py
"""
Tests for WalletConnect module.
"""

import unittest
from walletconnect import WalletConnect

class TestWalletConnect(unittest.TestCase):
    """Test cases for WalletConnect class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletConnect()
        self.assertIsInstance(instance, WalletConnect)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletConnect()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
