

roman_numerals={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

Roman=input("Enter roman number:")  

number=0

for i in range(len(Roman)-1):
                                                  
    if roman_numerals[Roman[i+1]] > roman_numerals[Roman[i]]:

        number=number-roman_numerals[Roman[i]]

    else:

        number=number+roman_numerals[Roman[i]]  

number=number+roman_numerals[Roman[len(Roman)-1]]

print(number)