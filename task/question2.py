# Write a Python function named next_prime(number) that takes an integer number
#  as input and returns the next prime number that is greater than number.
#  Function Signature: def next_prime(number: int) -> int:
#  Input: An integer number (where number > 0).
#  Output: The next prime number after number. 
# next_prime(7)  # should return 11
#  next_prime(14) # should return 17

def next_prime(number):


     is_prime=False

     for i in range(2,number):

          if number%i==0:

               next_number=number+1

               if is_prime==True:

                    next_number+=1
                    print(next_number)
        
print(next_prime(7))