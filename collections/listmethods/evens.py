# write a program to find the all even numbers in a list

arr=[1,3,2,5,6,8,4,10]

arr.sort()

for i in range(0,len(arr)):

    if arr[i]%2==0:

        print(arr[i])