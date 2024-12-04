


# rule 10 digit
# validate mobile number

from re import fullmatch

pattern="(91)?[0-9]{10}"  #?optional

mobile_number=input("enter mobilr number:")

matcher=fullmatch(pattern,mobile_number)

if matcher==None:

    print("invalid")

else:

    print("valid")