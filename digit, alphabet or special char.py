#Program to check whether Character is an Alphabet,Special Character or a digit

char= input("Enter the Character:")

if char=='a' or char=='b' or char=='c' or char=='d' or char=='e' or char=='f' or char=='g' or char=='h' or char=='i' or char=='j' or char=='k'or char=='l' or char=='m' or char=='n' or char=='o' or char=='p' or char=='q' or char=='r' or char=='s' or char=='t' or char=='u' or char=='v' or char=='w' or char=='x' or char=='y' or char=='z':
    
    print('The given Character {} is an Alphabet'.format(char))

elif char=='-' or char=='@' or char=='_' or char=='=' or char=='+' or char=='!' or char=='%' or char=='*':
    print('The given Character {} is a Special Character'.format(char))
else:
    print('The given Character {} is a Digit'.format(char))