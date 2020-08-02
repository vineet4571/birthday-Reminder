import datetime

current_time = datetime.datetime.now()

file = open('F:/birthdays.txt','r')
for each in file:
    if "/" in each :
        k = each.index('/')
        day = int(each[k-2:k])
        month = int(each[k+1:k+3])
        if day == current_time.day and month == current_time.month:
            print("wish",each[:each.index('-')],"a happy birthday")