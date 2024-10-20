#wap to check leap year

y= int(input("Enter the Year:"))

if y%4==0:
    if y%100==0:
        if y%400==0:
            print("{} is a leap Year".format(y))
        else:
            print("{} is not leap Year".format(y))
    else:
        print("{} is a leap Year".format(y))
else:
    print("{} is not a leap Year".format(y))