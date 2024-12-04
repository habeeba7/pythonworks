
number=int(input("enter number:")) #153

original=number

digit_count=len(str(number))

total=0

while(number!=0):

    digit=number%10  #153%10=15

    exponent=digit**digit_count  

    total=total+exponent

    number=number//10 

print("armstrong number" if total==original else "not armstrong number")