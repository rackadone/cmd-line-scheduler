'''
Date String Parser class

* The datetime object takes care of leap year consideration

'''

import re
import datetime
from global_values import Globals

class DateStringParser:
    @staticmethod
    def parse(date_str, current_year=0, current_month=0, current_day=0):
        """receive date string, parse, return date object
        """
        # Sanity check
        if not date_str:
            return None

        '''Try matching argument to possible valid date_strings
        '''
        match_slash = re.search(r'(\d+/\d+/\d+)', date_str)
        match_dash = re.search(r'(\d+-\d+-\d+)', date_str)

        # Match day (integer)
        try:
            match_day = 1 <= int(date_str) <= 31
        except Exception as e:
            match_day = False

        # Match month (string)
        try:
            match_month_long = (date_str).lower() in Globals.MONTH_SET
        except Exception as e:
            match_month_long = False

        # Match month shorthand (string)
        try:
            match_month_short = (date_str).lower() in Globals.MONTH_SET_ABBREV
        except Exception as e:
            match_month_short = False

        # Match year
        try:
            match_year = len(date_str) == 4 and  1900 < int(date_str) < datetime.MAXYEAR
        except Exception as e:
            match_year = False

        ''' Branch out to determine the date the user wants
        '''
        # CASE 1: date string is in the following format: XX/XX/XX
        if (match_slash):
            date_pattern_list = [
                            "%m/%d/%y",
                            "%m/%d/%Y"
                        ]
            for date_pattern in date_pattern_list:
                try:
                    return DateStringParser.validate_date_string(match_slash.group(1), date_pattern)
                    break
                except Exception as e:
                    continue
            else:
                print "Slash Date Format is Unknown."
                return None
        # CASE 2: date string is in the following format: XX-XX-XX
        elif (match_dash):
            date_pattern_list = [
                            "%m-%d-%y",
                            "%m-%d-%Y"
                        ]
            for date_pattern in date_pattern_list:
                try:
                    return DateStringParser.validate_date_string(match_dash.group(1), date_pattern)
                    break
                except Exception as e:
                    continue
            else:
                print "Dash Date Format is Unknown."
                return None
        # CASE 3: date string is just a simple integer in the range of 1 ~ 31
        elif (match_day):
            try:
                return datetime.datetime(current_year, current_month, int(date_str))
            except Exception as e:
                print "This day is not valid at the year and month"
                return None

        # CASE 4: date string is a month name, such as "january" or "January" or JANUARY"
        elif (match_month_long):
            try:
                return datetime.datetime(current_year, Globals.MONTH_DICT_REVERSE[date_str.lower()], current_day)
            except Exception as e:
                print "This month is not valid at the year and month"
                return None

        # CASE 5: date string is a month name abbreviation, such as "jan" or "Jan" or JAN"
        elif (match_month_short):
            try:
                return datetime.datetime(current_year, Globals.MONTH_DICT_REVERSE_ABBREV[date_str.lower()], current_day)
            except Exception as e:
                print "This month is not valid at the year and day"
                return None

        # CASE 6: date string is a year string such as "1998" or "2014"
        elif (match_year):
            try:
                return datetime.datetime(int(date_str), current_month, current_day)
            except Exception:
                print "This year is not valid at the month and day"
                return None


        # CASE N: Enter other cases here
        else:
            print "Match fails"
            return None

    @staticmethod    
    def validate_date_string(date_str, date_pattern):
        """ On success, returns a valid datetime object
        """
        return datetime.datetime.strptime(date_str, date_pattern)

    @staticmethod
    def get_ordinal(n):
        """ Very terse solution to finding ordinals, from 
            http://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712
        """
        k = n % 10
        return "%d%s" % (n, "tsnrhtdd"[(n/10%10!=1)*(k<4)*k::4])