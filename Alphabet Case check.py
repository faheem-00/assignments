#Program to check whether Alphabet is an Lowercase or Uppercase

char= input("Enter the Alpahbet (A-Z or a-z):")

if char=='a' or char=='b' or char=='c' or char=='d' or char=='e' or char=='f' or char=='g' or char=='h' or char=='i' or char=='j' or char=='k'or char=='l' or char=='m' or char=='n' or char=='o' or char=='p' or char=='q' or char=='r' or char=='s' or char=='t' or char=='u' or char=='v' or char=='w' or char=='x' or char=='y' or char=='z':
    
    print('The given Character {} is a Lowercase Alphabet'.format(char))
else:
    print('The given Character {} is a Uppercase Alphabet'.format(char))