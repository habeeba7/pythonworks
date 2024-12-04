
number=int(input("enter number:")) #234

total=0

while(number!=0): #234!=0 23!=0 2!=0

    digit=number%10 #234%10=4 23%10=3 2%10=2
    
    total=total+digit #0+4=4 4+3=7 7+2=9

    number=number//10 #234//10=23 23//10=2 2//10=0

print(total)