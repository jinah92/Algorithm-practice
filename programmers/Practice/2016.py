import datetime

weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']

def solution(a, b):
    day = datetime.date(2016, a, b)
    week = day.weekday()
    return weekday[week]

TEST = solution(1, 1)
print(TEST)