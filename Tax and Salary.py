#Program to calculate the Total Monthly salary 
basic_pay= int(input("Enter the Basic Pay:"))
da= 30/100*basic_pay
hra= 10/100*basic_pay
ta= 5/100*basic_pay
total_salary= basic_pay+ta+hra+da
print("{} is your Total Salary".format(total_salary))

#Calculate the Tax on Annual Income

annual_income= int(input("Enter Your Annual Income:"))

if annual_income>250000 and annual_income<=500000:
    taxable_amount= annual_income-250000
    tax1= 5/100*taxable_amount
    print("Your Income after taxes=", annual_income-tax1)
elif annual_income>500000 and annual_income<=750000:
    tax1=12500
    taxable_amount2= annual_income-500000
    tax2= 10/100*taxable_amount2
    print("Your Income after taxes=", annual_income-tax1-tax2)
elif annual_income>750000 and annual_income<=1000000:
    tax1=12500
    tax2=25000
    taxable_amount3= annual_income-750000
    tax3= 15/100*taxable_amount3
    print("Your Income after taxes=", annual_income-tax1-tax2-tax3)
elif annual_income>1000000 and annual_income<=1500000:
    tax1=12500
    tax2=25000
    tax3=75000
    taxable_amount4= annual_income-1000000
    tax4= 20/100*taxable_amount4
    print("Your Income after taxes=", annual_income-tax1-tax2-tax3-tax4)
elif annual_income>1500000:
    tax1=12500
    tax2=25000
    tax3=75000
    tax4=100000
    taxable_amount5= annual_income-1500000
    tax5= 30/100*taxable_amount5
    print("Your Income after taxes=", annual_income-tax1-tax2-tax3-tax4-tax5)
else:
    print("Tax Exempted")