s1=int(input("Enter the length of Side 1:"))
s2=int(input("Enter the length of Side 2:"))
s3=int(input("Enter the length of Side 3:"))

if s1 == s2 and s1==s3:
    print("The Triangle is Equilateral")
elif s1==s2 or s1==s3:
    print("The Triangle is Isosceles")
else:
    print("The Triangle is Scalene")