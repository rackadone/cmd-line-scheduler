class Globals:
    # January February March April May June July August September October November December
    MONTH_DICT = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
    }

    MONTH_DICT_REVERSE = {
        "january" : 1,
        "february" : 2,
        "march" : 3,
        "april" : 4,
        "may" : 5,
        "june" : 6,
        "july" : 7,
        "august" : 8,
        "september" : 9,
        "october" : 10,
        "november" : 11,
        "December" : 12,
    }

    MONTH_DICT_ABBREV = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec",
    }

    MONTH_DICT_REVERSE_ABBREV = {
        "jan" : 1,
        "feb" : 2,
        "mar" : 3,
        "apr" : 4,
        "may" : 5,
        "jun" : 6,
        "jul" : 7,
        "aug" : 8,
        "sep" : 9,
        "oct" : 10,
        "nov" : 11,
        "dec" : 12,
    }

    MONTH_SET = set(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"])
    MONTH_SET_ABBREV = set(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])

    COMMON_YEAR_NUM_DAYS = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,
    }
    DEFAULT_SCHEDULE_NAME = "default.json"