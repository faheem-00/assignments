# Program to calculate the Gross Monthly Salary

basic_pay= int(input("Enter the Basic Pay:"))

if basic_pay<=10000:
    da= 80/100*basic_pay
    hra= 20/100*basic_pay
elif basic_pay<=20000:
    da= 90/100*basic_pay
    hra= 25/100*basic_pay
else:
    da= 95/100*basic_pay
    hra= 30/100*basic_pay

Gross_salary= basic_pay+hra+da
print("{} is your Gross Salary".format(Gross_salary))