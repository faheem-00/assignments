#Maximum b/w two numbers
n1=int(input("Enter First No:"))
n2=int(input("Enter 2nd No:"))

if n1>n2:
    print('{} is greater than {}'.format(n1,n2))
else:
    print('{} is greater than {}'.format(n2,n1))

#Maximum b/w three numbers

num1=int(input("Enter First No:"))
num2=int(input("Enter 2nd No:"))
num3=int(input("Enter 3rd No:"))

if num1>num2 and num1>num2:
    print('{} is greater than {} and {}'.format(num1,num2,num3))
elif num2>num1 and num2>num3:
    print('{} is greater than {} and {}'.format(num2,num1,num3))
else:
    print('{} is greater than {} and {}'.format(num3,num1,num2))