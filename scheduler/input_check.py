#user input_check module

def check_go(arg):
    pass    

# A leap
# returns True if year is a leap year, False if it's not
def check_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

def parse_add(add_arg):
    pass

def month_check(arg):
    # Dictionaries to check input
    pass
    
def date_check(arg):
    pass
def time_check(arg):
    pass

def is_natural_number(str):
    try:
        number = int(str)
        return number >= 0
    except ValueError:
        return False

