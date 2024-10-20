#ELectricity Bill with the surcharge of 20% on Bill

units= int(input("Enter the Total Units:"))

if units<=50:
    bill= units* 0.50
    surcharge= 20/100*bill
    total_bill= bill+surcharge
    print("{} is your total bill with surchage".format(total_bill))

elif units<=150:
    first_50= 25

    units_2nd=(units-50)*(0.75)
    bill2= units_2nd+first_50
    surcharge2= 20/100*bill2
    total_bill2= bill2+surcharge2
    print("{} is your total bill with surchage".format(total_bill2))

elif units<=250:
    first_50= 25
    second_100= 75

    units_3rd=(units-150)*(1.20)
    bill3= units_3rd+ first_50+second_100
    surcharge3= 20/100*bill3
    total_bill3= bill3+surcharge3
    print("{} is your total bill with surchage".format(total_bill3))

elif units>250:
    first_50= 25
    second_100= 75
    third_100= 120

    units_4rd=(units-250)*(1.50)
    bill4= units_4rd+ first_50+second_100+ third_100
    surcharge4= 20/100*bill4
    total_bill4= bill4+surcharge4
    print("{} is your total bill with surchage".format(total_bill4))

else:
    print("Invalid Input")