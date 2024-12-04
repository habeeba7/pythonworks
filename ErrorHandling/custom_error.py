

# def review(rating):

#     if rating<0:

#         raise Exception("too low")
    
#     elif rating>10:
#         raise Exception("too high!!")
      
#     else:

#         print("done!")

# try:
#     review(4)


# except Exception as e:
#     print(e)

# print("hello")
# print("hai")




# def poll(age):

#     assert age>18,"invalid age"

#     print("voted")

# try:

#    poll(19)

# except Exception as e:

#     print(e)





# def review(rating):

#     assert rating>0,"too low"

#     assert rating in range(0,11),"too high"

#     print("rated")



def is_leap_year(year):

    if year<0:

        return False

    if year%100!=0 and year%4==0 or year%100==0 and year%400==0:

        return True

    else: 
        return False

def test_is_leap_year():

    assert is_leap_year(2024)==True,"non century year chk failed"

    assert is_leap_year(2025)==False,"invalid noncentury chk failed"

    assert is_leap_year(2000)==True,"century leap year chk failed"

    assert is_leap_year(1900)==False,"invalid century year chk failed"

    assert is_leap_year(-2024)==False,"invalid year chk failed"

try:

    test_is_leap_year()
    print("test case pass")

except Exception as e:
    print("test failed",e)





# def factorial(number):

#     fact=1
#     for i in range(1,number+1):

#         fact=fact*i

#     return fact

# def test_factorial():
    
#     assert test_factorial()
