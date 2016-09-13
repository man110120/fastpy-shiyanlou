#!/usr/bin/python
#coding=utf-8
def leapYear(year,month,day):
    if (month == 2 and day == 29):
        print True
    elif ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4==0)):
        print True
    else:
        print False
