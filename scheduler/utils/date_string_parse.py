'''
Date String Parser class
'''

import re
import datetime

class DateStringParser:
    @staticmethod
    def parse(date_str):
        """receive date string, parse, return date object
        """

        # CASE 1: date string is in the following format: XX/XX/XX
        match_slash = re.search(r'(\d+/\d+/\d+)', date_str)
        match_dash = re.search(r'(\d+-\d+-\d+)', date_str)
        if (match_slash):
            date_pattern_list = [
                            "%m/%d/%y",
                            "%m/%d/%Y"
                        ]

            for date_pattern in date_pattern_list:
                try:
                    DateStringParser.validate_date_string(match_slash.group(1), date_pattern)
                    break
                except Exception as e:
                    continue
            else:
                print "Slash Date Format is Unknown."
        elif (match_dash):
            date_pattern_list = [
                            "%m-%d-%y",
                            "%m-%d-%Y"
                        ]

            for date_pattern in date_pattern_list:
                try:
                    DateStringParser.validate_date_string(match_dash.group(1), date_pattern)
                    break
                except Exception as e:
                    continue
            else:
                print "Dash Date Format is Unknown."
        else:
            print "Match fails"

    @staticmethod    
    def validate_date_string(date_str, date_pattern):
        parsed_date = datetime.datetime.strptime(date_str, date_pattern)
        print "Parsed year is " + str(parsed_date.year)