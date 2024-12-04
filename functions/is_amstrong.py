

# is_amstrong_number(number)

def is_amstrong_number(number):

    original=number

    digit_count=len(str(number))

    total=0

    while(number!=0):

        digit=number%10

        exponent=digit**digit_count

        total=total+exponent

        number=number//10

    return "amstrong number" if total==original else "not amstrong number"

print(is_amstrong_number(37))

