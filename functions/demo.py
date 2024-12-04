

#syntax

#def function_name(p1,p2,p3):

      #function definition
       #return value





# def sub(num1,num2):

#     result=num1-num2

#     print(result)

# sub(200,100)


# def multiplication(num1,num2):

#     result=num1*num2

#     print(result)

# multiplication(34,76)


# def div(num1,num2):

#     result=num1/num2

#     print(result)

# div(34,76)





def last_digit_max(num1,num2):

    num1_last_digit=num1%10

    num2_last_digit=num2%10

    print(num1 if num1_last_digit>num2_last_digit else num2)

print(last_digit_max(123,872))

   

