year=int(input('year:\n'))
month=int(input('mouth:\n'))
day=int(input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <=12:
    sum=months[month -1]
else:
    print('date error')

i = sum + day
print('it is the',str(i)+'th day')

