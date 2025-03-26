import datetime
todaysdate=datetime.date.today()
print(todaysdate)

currenttime=datetime.datetime.now()
print(currenttime)

currentyear=todaysdate.year
print(currentyear)

currentmonth=todaysdate.month
print(currentmonth)

currentdate=todaysdate.day
print(currentdate)

currenthour=currenttime.hour
print(currenthour)

currentmin=currenttime.minute
print(currentmin)

#currentsec=currenttime.second
#print(currentsec)