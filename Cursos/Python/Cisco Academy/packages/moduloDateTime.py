# from datetime import date
# import time

# timestamp = time.time()
# print('Timestamp:', timestamp)

# dias = timestamp / 60 / 60 / 24
# meses = dias / 30
# anos = dias / 365
# print(dias, meses, anos)
# d = date.fromtimestamp(timestamp)
# print('Date: ', d)

from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))
