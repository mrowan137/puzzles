"""
Q: You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

A: 171
"""

# days in months, not accounting leap years
month_to_days = {
    0: 31,  # jan
    1: 28,  # feb
    2: 31,  # mar
    3: 30,  # apr
    4: 31,  # may
    5: 30,  # jun
    6: 31,  # jul
    7: 31,  # aug
    8: 30,  # sep
    9: 31,  # oct
    10: 30,  # nov
    11: 31,  # dec
}


def count_sundays():
    # count Sundays on [1-1-1901, 12-31-2000]

    day_of_the_week = 1  # days of week: 0 (Sunday) -- 6 (Saturday)
    month = 0  # months: 0 (January) -- 11 (December)
    year = 1900

    # count number of Sundays
    cnt = 0

    while year <= 2000 and month <= 11:
        is_leap_year = (year % 4 == 0) * (year % 100 != 0) + (year % 400 == 0)
        days_in_month = month_to_days[month] + (month == 1) * is_leap_year

        # tick day
        for day_of_the_month in range(days_in_month):
            if day_of_the_week == 0 and day_of_the_month == 0 and year >= 1901:
                cnt += 1

            day_of_the_week += 1
            day_of_the_week %= 7

        # tick month
        month += 1
        month %= 12

        # tick year
        if month == 0:
            year += 1

    return cnt


if __name__ == "__main__":
    print("Sundays from 1 Jan 1900 to 31 Dec 2000: {}".format(count_sundays()))
