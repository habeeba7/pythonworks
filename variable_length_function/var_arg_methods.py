

# def add_numbers(*args):

#     print(args)

# add_numbers(10,20)
# add_numbers(10,20,30)


# create a function that accept any number of arguments and return second maximum number

def second_max_number(*args):

    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]

print(second_max_number(10,11,12,13))



def display_mobile_data(**kwargs):

    print(kwargs.get("name"))

    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price=32000,display="amoled")




def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)

    if kwargs.get("operation")=="*":

        result=1
        for num in args:

            result=result*num
        return result

print(calculator(10,20,30,operation="*"))



def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)

    if kwargs.get("operation")=="total":

        return sum(args)

print(student_info(45,43,44,operation="total"))




def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="False":

        return sorted(args)
print(sort_numbers(1,2,6,4,15,11,reverse="False"))