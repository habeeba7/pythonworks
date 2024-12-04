


start=int(input("enter starting limit:"))

end=int(input("enter ending limit:"))

for num in range(start,end+1):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break
    
    if is_prime==True:

        print(num)
