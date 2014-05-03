from datetime import date

from utils.global_values import Globals
from utils.date_string_parse import DateStringParser

import os, cmd
from input_check import *

class ScheduleShell(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        # Check if schedule file exists. If not, create new schedule
        #if os.path.isfile(Globals.DEFAULT_SCHEDULE_NAME):
        #    self.fp = open(Globals.DEFAULT_SCHEDULE_NAME)


        # Shell Time Variables. Subject to change on user input
        self.current_date = date.today()
        self.year = today_date.year
        self.month = today_date.month
        self.day = today_date.day

        self.intro = 'Welcome to the scheduler shell. Type help or ? to list commands.\n'
        self.prompt = 'SCH$(' + Globals.MONTH_DICT_ABBREV[self.month] + '-' + str(self.day) + '-' + str(self.year) +')>>'
        self.schedule = Schedule(self.year)
        self.ordering = 'middle' # Endian

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

    def do_set(self, arg):
        pass

    def do_add(self, arg):
        'Add event to schedule:' # Documentation

        # If no arguments, prompt user for each input
        if not arg:
            print "Usage: add <event>"


        # Need to Parse Argument
        #self.schedule.add_event('January', 1, '12:30', 'Lunch with Them')

    # Exit Command
    # Save Changes to xml file
    def do_exit(self, arg):
        if (arg == "!"):
            return True
        else:
            self.schedule.write_to_file()
            return True

    '''HELPERS
    '''

    def set_date(self, date_obj):
        self.current_date = date_obj
        self.year = date_obj.year
        self.month = date_obj.month
        self.day = date_obj.day
        self.prompt = 'SCH$(' + Globals.MONTH_DICT[self.month] + '-' + str(self.day) + '-' + str(self.year) +')>>'
