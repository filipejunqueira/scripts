import datetime as dt
import math

class MyDate:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

# Select the day of the week (mon, tues, wed etc...)
weekDays = {0: "Monday",1: "Tuesday" ,2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday",6: "Sunday"}

week_day_target = 1
start_date = dt.datetime(2016,2,4)
ndates = 12
multiplier = 1



print(weekDays[start_date.weekday()])
print(start_date.weekday())

#TODO FIX the start date!
#Select the start date - FIX THIS


days_diff = (start_date.weekday() - week_day_target)
first_date = start_date + dt.timedelta(7-days_diff)



print(weekDays[first_date.weekday()])

date_array=[]

for i in range(ndates):
    date_array.append(first_date + dt.timedelta(7*i*multiplier))

[print(item.date()) for item in date_array]




