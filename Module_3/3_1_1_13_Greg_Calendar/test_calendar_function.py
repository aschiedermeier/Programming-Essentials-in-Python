#######################################
# gregorian calendar
# test function
# input: year
# return: year type
#######################################

import unittest
from calendar_function import calendar

class TaxTestCase(unittest.TestCase):
    """Tests for "calendar_function.py"."""

    def test_year(self):
        """Test all years"""
        self.assertEqual(calendar(2000),"Leap year")
        self.assertEqual(calendar(2015),"Common year")
        self.assertEqual(calendar(1999),"Common year")
        self.assertEqual(calendar(1996),"Leap year")
        self.assertEqual(calendar(1580),"Not within the Gregorian calendar period")
unittest.main()