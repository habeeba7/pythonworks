
num=int(input("enter number:")) #234

total=0

while(num!=0):#234!=0

    digit=num%10 #234%10=4

    digit_sqr=digit**2

    total=total+digit_sqr 

    num=num//10

print(total)