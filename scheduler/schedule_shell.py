from datetime import date
from schedule import Schedule
import os, cmd, sys
from input_check import *

class ScheduleShell(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        today_date = date.today()

        # Shell Time Variables. Subject to change on user input
        self.year = today_date.year
        self.month = today_date.month
        self.day = today_date.day

        self.intro = 'Welcome to the scheduler shell. Type help or ? to list commands. (' + str(self.year) + '-' + str(self.month) + '-' + str(self.day) + ')\n'
        self.prompt = 'SCH$(' + str(self.year) + '-' + str(self.month) + '-' + str(self.day) +')>>'
        self.schedule = Schedule(self.year)
        self.ordering = 'middle' # Endian

    def do_go(self, arg):
        # help documentation
        "'go' is a simple command you enter to set the current date.\n"\
        "On initialization the date is set to the current date.\n\n"\
        "Format: go <month> <day>\n"\
        "        go <month>\n"\
        "        go <day>\n"\
        "        go <year>\n"\
        "        go <year> <month> <day>\n"\
        "Three combinations may be used: Big endian(year, month day)\n"\
        "                                Little endian (day, month, year)\n"\
        "                                Middle endian (month, day year)\n\n"\
        "If there are three arguments, the script first looks for the\n"\
        "year, month, and day. If any tuple or triple is ambiguous, for\n"\
        "example, if the entered date was '06-07-08', the endian in set\n"\
        "is used. If a tuple is entered, by default, the combination is\n"\
        "assumed to be a combination of a month and a day. If there is only\n"\
        "one argument and it is ambiguous, it is assumed to be a day.\n\n"\
        "Example: go aug 13 (sets date to August 13th of current year)\n"\
        "         go 2015-9-20 (use y-m-d)\n"

        if not arg:
             print "Usage: go <date>"
        else:
            

        

    def do_set(self, arg):
        pass

    def do_test(self, arg):
         print arg

    def do_add(self, arg):
        'Add event to schedule:' # Documentation

        # If no arguments, prompt user for each input
        if not arg:
            print "Enter month:"
            month = raw_input()
            print "Enter day:"
            day = raw_input()
            print "Enter time:"
            time = raw_input()


        # Need to Parse Argument
        self.schedule.add_event('January', 1, '12:30', 'Lunch with Them')




    # Exit Command
    # Save Changes to xml file
    def do_exit(self, arg):
        if (arg == "!"):
            return True
        else:
            self.schedule.write_to_file()
            return True