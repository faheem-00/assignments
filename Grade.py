# WAP to check the result of student

math= float(input("Enter the  Math Marks:"))
chem= float(input("Enter the Chemistry Marks:"))
phy= float(input("Enter the Physics Marks:"))
bio= float(input("Enter the Biology Marks:"))
comp= float(input("Enter the Computer Marks:"))

total_marks= chem+bio+math+comp+ phy

percent= total_marks/500*100


if percent>=90:
    Grade="A" 
elif percent>=80:
    Grade="B" 
elif percent>=70:
    Grade="C" 
elif percent>=60:
    Grade="D" 
elif percent>40:
    Grade="E" 
else:
    Grade='F'

print("Grade {}".format(Grade),"and Total Marks:{}".format(total_marks))
