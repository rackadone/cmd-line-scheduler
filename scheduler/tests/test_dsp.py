import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from utils.date_string_parse import DateStringParser

class TestDateStringParser (unittest.TestCase):
    def test_slash_format(self):
        # Test mm/dd/yy
        date_obj = DateStringParser.parse("12/12/98")
        self.assertEqual(date_obj.year, 1998)
        self.assertEqual(date_obj.month, 12)
        self.assertEqual(date_obj.day, 12)
        # Test mm/dd/YYYY
        date_obj = DateStringParser.parse("12/12/2014")
        self.assertEqual(date_obj.year, 2014)
        self.assertEqual(date_obj.month, 12)
        self.assertEqual(date_obj.day, 12)
        # Should Fail
        self.assertFalse(DateStringParser.parse("12/12/1"))
        self.assertFalse(DateStringParser.parse("12/12/988"))

    def test_dash_format(self):
        # Test mm-dd-yy
        date_obj = DateStringParser.parse("12-12-98")
        self.assertEqual(date_obj.year, 1998)
        self.assertEqual(date_obj.month, 12)
        self.assertEqual(date_obj.day, 12)
        # Test mm-dd-YYYY
        date_obj = DateStringParser.parse("12-12-2014")
        self.assertEqual(date_obj.year, 2014)
        self.assertEqual(date_obj.month, 12)
        self.assertEqual(date_obj.day, 12)

        # Should Fail
        self.assertFalse(DateStringParser.parse("12-12-1"))
        self.assertFalse(DateStringParser.parse("12-12-988"))            

    def test_extra_strings(self):
        self.assertFalse(DateStringParser.parse("This is a date string"))
        self.assertFalse(DateStringParser.parse(""))
        self.assertFalse(DateStringParser.parse(None))

    def test_leap_year(self):
        self.assertFalse(DateStringParser.parse("2-29-2014"))
        date_obj = DateStringParser.parse("2-29-2016")
        self.assertEqual(date_obj.year, 2016)
        self.assertEqual(date_obj.month, 2)
        self.assertEqual(date_obj.day, 29)

    def test_get_ordinal(self):
        self.assertEqual(DateStringParser.get_ordinal(1), "1st")
        self.assertEqual(DateStringParser.get_ordinal(2), "2nd")
        self.assertEqual(DateStringParser.get_ordinal(3), "3rd")
        self.assertEqual(DateStringParser.get_ordinal(4), "4th")

    def test_parse_day(self):
        """ Test cases where the user enters only a day.
        """
        # Not leap year, so 2/29/2014 doesn't exist
        self.assertFalse(DateStringParser.parse("29", current_month=2, current_year=2014, current_day=0))

        # Leap year, so 2/29/2016 exists.
        date_obj = DateStringParser.parse("29", current_month=2, current_year=2016, current_day=0)
        self.assertEqual(date_obj.year, 2016)
        self.assertEqual(date_obj.month, 2)
        self.assertEqual(date_obj.day, 29)

    def test_parse_month_long(self):
        """ Test cases where user enter a month string
        """
        self.assertFalse(DateStringParser.parse("February", current_month=1, current_year=2014, current_day=29))
        self.assertFalse(DateStringParser.parse("february", current_month=1, current_year=2014, current_day=29))
        self.assertFalse(DateStringParser.parse("FebRuaRy", current_month=1, current_year=2014, current_day=29))
        self.assertFalse(DateStringParser.parse("February", current_month=1, current_year=2014, current_day=29))

        date_obj = DateStringParser.parse("February", current_month=1, current_year=2016, current_day=29)
        self.assertEqual(date_obj.year, 2016)
        self.assertEqual(date_obj.month, 2)
        self.assertEqual(date_obj.day, 29)

    def test_parse_month_short(self):
        """ Test cases where user enter a month string
        """
        self.assertFalse(DateStringParser.parse("Feb", current_month=1, current_year=2014, current_day=29))
        self.assertFalse(DateStringParser.parse("feb", current_month=1, current_year=2014, current_day=29))
        self.assertFalse(DateStringParser.parse("fEb", current_month=1, current_year=2014, current_day=29))
        self.assertFalse(DateStringParser.parse("FEB", current_month=1, current_year=2014, current_day=29))

        date_obj = DateStringParser.parse("Feb", current_month=1, current_year=2016, current_day=29)
        self.assertEqual(date_obj.year, 2016)
        self.assertEqual(date_obj.month, 2)
        self.assertEqual(date_obj.day, 29)

    def test_parse_year(self):
        self.assertFalse(DateStringParser.parse("2014", current_month=2, current_year=2010, current_day=29))
        self.assertFalse(DateStringParser.parse("1899", current_month=2, current_year=2010, current_day=29))
        self.assertFalse(DateStringParser.parse("10000", current_month=2, current_year=2010, current_day=29))
        self.assertFalse(DateStringParser.parse("201", current_month=2, current_year=2010, current_day=29))
        self.assertFalse(DateStringParser.parse("98", current_month=2, current_year=2010, current_day=29))

        date_obj = DateStringParser.parse("2016", current_month=2, current_year=2014, current_day=29)
        self.assertEqual(date_obj.year, 2016)
        self.assertEqual(date_obj.month, 2)
        self.assertEqual(date_obj.day, 29)



if __name__ == '__main__' :
    unittest.main()