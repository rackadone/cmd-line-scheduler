# =====================================
# file name: schedule_shell.py
#
# Holds ScheduleShell class, which inherits
# from cmd.Cmd
# =====================================

# Standard Libraries
from datetime import date
from cmd import Cmd

# Custom libraries
from utils.global_values import Globals
from utils.date_string_parse import DateStringParser
from utils.storage_manager import StorageManager

class ScheduleShell(Cmd):
    def __init__(self):
        Cmd.__init__(self)

        # Shell Time Variables. Subject to change on user input
        self.current_date = date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month
        self.day = self.current_date.day

        self.intro = '\nWelcome to the scheduler shell. Type help or ? to list commands.\n'
        self.prompt = 'Scheduler-$(' + Globals.MONTH_DICT_ABBREV[self.month] + '-' + str(self.day) + '-' + str(self.year) +')>>'

        # Establish file storage
        self.storage_manager = StorageManager()

    # =====================================
    # Commands
    # =====================================

    def do_go(self, arg):
        """\
        'go' is a simple command you enter to set the current date.
        On initialization the date is set to the current date.\
        """
        if not arg:
             print "Usage: go <date>"
        else:
            date_obj = DateStringParser.parse(arg, self.year, self.month, self.day)
            if (date_obj):
                self.set_date(date_obj)
            else:
                print "Invalid date, please enter a date in the following format: \n"
                print "    go mm/dd/yy"
                print "    go mm/dd/YYYY"

    def do_add(self, arg):
        """\
        'add' is a simple command you enter to add an event to the current date.
        Usage: add <event>\
        """
        # If no arguments, prompt user for each input
        if not arg:
            print "Usage: add <event>"
        else:
            json_root = self.storage_manager.get_json_object()
            target_year = str(self.year)
            target_month = str(self.month)
            target_day = str(self.day)

            # Add the event to the json file
            if target_year not in json_root:
                json_root[target_year] = {}

            if target_month not in json_root[target_year]:
                json_root[target_year][target_month] = {}

            if target_day not in json_root[target_year][target_month]:
                json_root[target_year][target_month][target_day] = []

            json_root[target_year][target_month][target_day].append(arg)
            self.storage_manager.store_json_object(json_root)
            print "Event has been added"

    def do_ls(self, arg):
        """\
        List events of the day.
        """
        json_root = self.storage_manager.get_json_object()
        target_year = str(self.year)
        target_month = str(self.month)
        target_day = str(self.day)
        try:
            event_list = json_root[target_year][target_month][target_day]
            print "These are the events of " + Globals.MONTH_DICT[self.month] + " " + DateStringParser.get_ordinal(self.day) + ", " + target_year + ":"
            for i, val in enumerate(event_list):
                print "        - " + val

        except Exception:
            print "There are no events on this day."

    def do_exit(self, arg):
        """\
        Exit scheduler program.
        """
        if (arg == "!"):
            # TODO: implement if needed
            return True
        else:
            return True

    # =====================================
    # Helpers
    # =====================================

    def set_date(self, date_obj):
        self.current_date = date_obj
        self.year = date_obj.year
        self.month = date_obj.month
        self.day = date_obj.day
        self.prompt = 'Scheduler-$(' + Globals.MONTH_DICT_ABBREV[self.month] + '-' + str(self.day) + '-' + str(self.year) +')>>'
