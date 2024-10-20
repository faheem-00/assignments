num=int(input("Enter the Number:"))

if num%5==0:
    if num%11==0:
        print("{} is divisible by 5 and 11".format(num))
    else:
        print("{} is divisible by 5 but not by  11".format(num))
else:
    print("{} is not divisible by 5 or 11".format(num))