
# A digit that is not 0 or 1
# Three digits
# An optional space or dash
# Four digits
# An optional space or dash
# Three digits
# The final digit, which is the check digit

from re import fullmatch

Aadhar_number=input("Enter aadhar number:")

pattern="[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}"

matcher=fullmatch(pattern,Aadhar_number)

if matcher==None:

    print("invalid")

else:

    print("valid")