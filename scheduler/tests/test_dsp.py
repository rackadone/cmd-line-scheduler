import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from utils.date_string_parse import DateStringParser

class TestDateStringParser (unittest.TestCase):
    def test_slash_format(self):
        # Test mm/dd/yy
        self.assertTrue(DateStringParser.parse("12/12/98"))
        # Test mm/dd/YYYY
        self.assertTrue(DateStringParser.parse("12/12/2014"))

        # Should Fail
        self.assertFalse(DateStringParser.parse("12/12/1"))
        self.assertFalse(DateStringParser.parse("12/12/988"))

    def test_dash_format(self):
        # Test mm-dd-yy
        self.assertTrue(DateStringParser.parse("12-12-98"))
        # Test mm-dd-YYYY
        self.assertTrue(DateStringParser.parse("12-12-2014"))

        # Should Fail
        self.assertFalse(DateStringParser.parse("12-12-1"))
        self.assertFalse(DateStringParser.parse("12-12-988"))            

    def test_extra_strings(self):
        self.assertFalse(DateStringParser.parse("This is a date string"))
        self.assertFalse(DateStringParser.parse(""))
        self.assertFalse(DateStringParser.parse(None))

    def test_leap_year(self):
        self.assertFalse(DateStringParser.parse("2-29-2014"))
        self.assertTrue(DateStringParser.parse("2-29-2016"))

    def test_get_ordinal(self):
        self.assertEqual(DateStringParser.get_ordinal(1), "1st")
        self.assertEqual(DateStringParser.get_ordinal(2), "2nd")
        self.assertEqual(DateStringParser.get_ordinal(3), "3rd")
        self.assertEqual(DateStringParser.get_ordinal(4), "4th")

if __name__ == '__main__' :
    unittest.main()