# decorator is a normal function
# recieve parameter as a another function
# there is a another inner fn 
# 

# def swap_decorator(fn):

#     def wrapper(n1,n2):

#         if n1<n2:
#             (n1,n2)=(n2,n1)

#         return fn(n1,n2)
#     return wrapper


# @swap_decorator
# def smart_sub(num1,num2):

#     return num1-num2

# @swap_decorator
# def smart_div(num1,num2):

#     return num1/num2

# print(smart_sub(10,2))

# print(smart_sub(-10,-2))
# print(smart_div(2,10))


    
def swap_dec(fn):

    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    
    return wrapper



def round_dec(fn):

    def wrapper(num1,num2):

        num1=round(num1)
        num2=round(num2)

        return fn(num1,num2)
    
    return wrapper


@round_dec
@swap_dec
def add_number(num1,num2):

    return num1+num2

@round_dec
@swap_dec
def subtraction(num1,num2):

    return num1-num2

@round_dec
@swap_dec
def division(num1,num2):
    
    return num1/num2

print(division(2,10))
print(add_number(2.5,3.6))







