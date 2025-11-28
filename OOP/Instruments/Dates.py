import datetime

now = datetime.datetime.now()
midnight = datetime.datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
print(now - midnight)

print (now + datetime.timedelta(days = 10, hours = 10)) # We can add time delta