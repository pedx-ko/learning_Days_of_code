import random


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("")
                return True
            else:
                # print("not leap year. ")
                return False
        else:
            # print("not leap year. ")
            return True
    else:
        # print("not leap year. ")
        return False


def day_in_month(year, month):

    year = year

    leap = is_leap(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = month

    if month > 12 and month < 1:
        return 'Invalid month number'
    if leap and month == 2:
        return 29
    return month_days[month - 1]


start = 1900
stop = 2040

for i in range(start, stop):
    # print(i)
    year = int(i)  # enter a year
    month = int(2)  # enter a month
    days = day_in_month(year, month)
    if days > 28:
        print(i)
        print(days)


# -----------------simpler method

# import calendar


# def is_leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     return False


# for year in range(1990, 2024):
#     if is_leap_year(year):
#         print(f"Leap year: {year}")
#         for month in range(1, 13):
#             days = calendar.monthrange(year, month)[1]
#             if days == 29:
#                 print(f"{month} has 29 days in {year}")
