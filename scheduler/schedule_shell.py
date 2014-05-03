from datetime import date

from utils.global_values import Globals
from utils.date_string_parse import DateStringParser
from utils.storage_manager import StorageManager

import os, cmd
from input_check import *

class ScheduleShell(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        # Shell Time Variables. Subject to change on user input
        self.current_date = date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month
        self.day = self.current_date.day

        self.intro = 'Welcome to the scheduler shell. Type help or ? to list commands.\n'
        self.prompt = 'SCH$(' + Globals.MONTH_DICT_ABBREV[self.month] + '-' + str(self.day) + '-' + str(self.year) +')>>'

        # Establish file storage
        self.storage_manager = StorageManager()

    '''COMMANDS
    '''

    def do_go(self, arg):
        # help documentation
        "'go' is a simple command you enter to set the current date.\n"\
        "On initialization the date is set to the current date.\n\n"\

        if not arg:
             print "Usage: go <date>"
        else:
            date_obj = DateStringParser.parse(arg)
            if (date_obj):
                self.set_date(date_obj)
            else:
                print "Invalid date, please enter a date in the following format: \n"
                print "    go mm/dd/yy"
                print "    go mm/dd/YYYY"

    def do_add(self, arg):
        "'add' is a simple command you enter to add an event to the current date."

        # If no arguments, prompt user for each input
        if not arg:
            print "Usage: add <event>"
        else:
            json_root = self.storage_manager.get_json_object()
            target_year = str(self.year)
            target_month = str(self.month)
            target_day = str(self.day)

            print "Before entering in json_root"
            print json_root

            if target_year not in json_root:
                print "need to create new year"
                print json_root

                json_root[target_year] = {}

            if target_month not in json_root[target_year]:
                print "need to create new month"
                print json_root

                json_root[target_year][target_month] = {}

            if target_day not in json_root[target_year][target_month]:
                print "need to create new day"
                print json_root

                json_root[target_year][target_month][target_day] = []

            json_root[target_year][target_month][target_day].append(arg)
            self.storage_manager.store_json_object(json_root)
            print "Event has been added"
            print json_root


    # Exit Command
    def do_exit(self, arg):
        if (arg == "!"):
            # TODO: implement if needed
            return True
        else:
            return True

    '''HELPERS
    '''

    def set_date(self, date_obj):
        self.current_date = date_obj
        self.year = date_obj.year
        self.month = date_obj.month
        self.day = date_obj.day
        self.prompt = 'SCH$(' + Globals.MONTH_DICT[self.month] + '-' + str(self.day) + '-' + str(self.year) +')>>'
