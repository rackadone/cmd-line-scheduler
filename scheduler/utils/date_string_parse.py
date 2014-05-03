'''
Date String Parser class

* The datetime object takes care of leap year consideration

'''

import re
import datetime

class DateStringParser:
    @staticmethod
    def parse(date_str):
        """receive date string, parse, return date object
        """
        # Sanity check
        if not date_str:
            return None

        # Try match 
        match_slash = re.search(r'(\d+/\d+/\d+)', date_str)
        match_dash = re.search(r'(\d+-\d+-\d+)', date_str)

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