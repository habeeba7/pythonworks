


from re import fullmatch

useR_input=input("Enetr number:")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,useR_input)

if matcher==None:

    print("invalid")

else:

    print("valid")