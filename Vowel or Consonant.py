#check whether a Alphabet is a Vowel or Consonant

v1= 'a'
v2='e'
v3='i'
v4='o'
v5='u'

char= input("Enter the Alphabet in LowerCase:")

if char==v1 or char==v2 or char==v3 or char==v4 or char==v5:
    print("{} is a Vowel".format(char))
else:
    print("{} is a consonant".format(char))