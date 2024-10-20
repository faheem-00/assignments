# check whether the triangle is valid through its angles

a1=int(input("Enter the Length of Side 1:"))
a2=int(input("Enter the Length of Side 2:"))
a3=int(input("Enter the Length of Side 3:"))

all_angles= a1+a2+a3

if all_angles==180:
    print("Triangle is valid.")
else:
    print("Not a Valid Triangle")

# check whether a shape is triangle or not

sides=int(input("Enter the Total Sides of Shape:"))
if sides==3:
    print(" Your shape is a Valid Triangle")
else:
    print("Not a Triangle")