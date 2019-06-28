#######################################
# income tax 
# function
# input: income
# return: tax
#######################################

import unittest
from tax_function import income_tax

class TaxTestCase(unittest.TestCase):
    """Tests for "tax_function.py"."""

    def test_income_tax_10000(self):
        """Test 10.000"""
        self.assertAlmostEqual(income_tax(10000),1244)
    
    def test_income_tax_100000(self):
        """Test 100.000"""
        self.assertEqual(income_tax(100000),19470)

    def test_income_tax_1000(self):
        """Test 1.000"""
        self.assertEqual(income_tax(1000),0)
    
    def test_income_tax_minus_100(self):
        """Test 10000-100"""
        self.assertEqual(income_tax(-100),0)

unittest.main()