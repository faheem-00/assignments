a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

d= (b*b)-(4*a*c)
root1=-b+(d/2*a)**1/2
root2=-b-(d/2*a)**1/2

if d>0:
    print("The equation has 2 distinct Real Roots", root1, root2)
elif d==0:
    print("The equation has 1 Real Root", root1)
else:
    print("The equation has 2 Complex Roots", root1, root2)

