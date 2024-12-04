# SS: Two-character state code
# RR: Two-digit RTO code
# YYYY: Four-digit year of issue
# NNNNNNN: Seven digits 

from re import fullmatch

license_number=input("Enter licence number:")

pattern="(KL)?[0-9]{2}[0-9]{4}[0-9]{7}"

matcher=fullmatch(pattern,license_number)

if matcher==None:

    print("invalid")

else:

    print("valid")