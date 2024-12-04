

# starting with KL

# 2digit

# alphabets min1 max2

# 4digit

from re import fullmatch

vehicle_number=input("Enter registration number:")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,vehicle_number)

if matcher==None:

    print("invalid")

else:

    print("valid")

# passport
# aadhar number
# driving licence