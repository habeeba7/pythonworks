

from re import fullmatch

user_input=input("enter variable name:")

# start with an alphabets(lowercase,uppercase)
# any number of alphabets,digits,_

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:


    print("valid")