import datetime
import time
weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']

def solution(a, b):
    day = datetime.date(2016, a, b)
    week = day.weekday() + 1
    return weekday[week]
