#!/usr/bin/env python
# coding: utf-8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--date1", help="date dd/mm/yy", type=str)
parser.add_argument("--date2", help="date dd/mm/yy", type=str)
args = parser.parse_args()


def is_valid(date):
    try:
        d, m, y = (int(d) for d in date.split('/'))
    except ValueError:
        print("date needs to be of format dd/mm/yyyy")
        
    if m < 1 or m > 12:
        raise ValueError('Month has to be between 1 and 12 (inclusive).')
        
    if d < 1 or d > 31:
        raise ValueError('Day has to be between 1 and 31 (inclusive).')
    
    return d, m, y        


month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def date2num(date):
    d, m, y = is_valid(date)
    # calculate number of days in year:
    year_days = 365 * y
    # number of leap years till year (but not including y)
    leap_years = (y - 1) // 4 + 1 # + 1 because year 0 is a leap year
    year_days += leap_years
    
    this_leap_year = y % 4 == 0
    
    if this_leap_year:
        days = sum(month_leap[:m-1]) + d
    else:
        days = sum(month[:m-1]) + d
        
    return year_days + days

def date_diff(date1, date2):
    diff = abs(date2num(date2) - date2num(date1)) - 1
    return diff

print(date_diff(args.date1, args.date2))