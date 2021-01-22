year = int(input("Please input year but 4 digits: "))
month = int(input("Please input month but only number: "))
# Number od days per month, first value placeholder for indexing purposes.
month_day = [0, 31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """" Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """ Return number of days in that month in that year."""

    if not 1 <=  month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_day[month]
print(days_in_month(year,month))

