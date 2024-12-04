
# 3alphabets in uppercase
# 4th place alphabet[PCAFHT]
# 1alphabet
# 4digits
# 1alphabets
# 







from re import fullmatch

pancard_number=input("Enter pancard number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:

    print("invalid")

else:

    print("valid")





