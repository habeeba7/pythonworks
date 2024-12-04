
# create a function max_two with two parameter num1,num2 return largest number

# def max_two(num1,num2):

#     return num1 if num1>num2 else num2

# print(max_two(4,3))



# create a function min_two with two parameter num1,num2 return smallest number


# def min_two(num1,num2):


#     return num1 if num1<num2 else num2

# print(min_two(43,23))



# def multiplication_table(number,n=10):

#     for i in range(1,n+1):

#         print(f"{i} * {number} = {i*number} ")

# multiplication_table(3)




#create a function exponent with two parameter num1,n

# def exponent(number,n=2):

#     return number**n

# print(exponent(4))




#
#
#

def smart_sub(num1,num2,reverse=False):

    return num2-num1 if reverse==True else num1-num2


print(smart_sub(10,20))


#create a function random_numbers(start,end,step)


def random_numbers(start,end,step=1):

    while(start<=end):

        print(start)

        start=start+step

print(random_numbers(10,100))



        