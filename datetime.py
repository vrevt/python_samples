d = datetime.date(2020, 1, 1)
print(d.year) # 2020
print(d.day)  # 1
print(d.month) # 1


print(datetime.date.today())
# 2020-04-23

Time.sleep(xx)
# Hello, Yan!


print(time.ctime())
# Thu Apr 23 01:11:00 2020

print(time.ctime(1384112639))
# Sun Nov 10 22:43:59 2013


print(datetime.datetime.now())
print(datetime.datetime.today())
# 2020-04-23 01:06:11.705315


d = datetime.datetime(2020, 04, 23, 1, 2, 3)
print(d.second) # 3
print(d.year) # 2020


today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '04/23/2020'


x = time.time()
print(x)
# 1587593598.8145456


