# Socratica tutorial
# Datetime module

import datetime

d = datetime.date(2016, 7, 29)
print(d)
t = datetime.time(11, 34, 40)
print(t)
dt = datetime.datetime(2016, 7, 29, 11, 55, 15, 10000)
print(dt)

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)

now = datetime.datetime.today()
print(now)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))
