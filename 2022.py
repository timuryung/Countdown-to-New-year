import datetime

newyear = datetime.date(2022, 1, 1)
currentdate = datetime.date.today()
currenttime = datetime.time()
lefttonewyear = newyear - currentdate



while True:
    if newyear == currentdate:
        print('Happy New year!')
    else:
        print(lefttonewyear)
