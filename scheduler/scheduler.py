'''
Entry point of the application.

'''

from schedule_shell import ScheduleShell
import os

os.system('clear')
newShell = ScheduleShell()
newShell.cmdloop()