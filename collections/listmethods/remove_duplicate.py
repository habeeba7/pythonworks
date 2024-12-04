# write a python program to remove duplicates from a list


arr=[1,2,2,3,1,4,3,2]

arr.sort()





for i in range(0,len(arr)-1):

    for j in range(1,len(arr)):

        result=arr[j]-arr[i]

        if result==0:

            arr.pop(arr[i])
        

print(arr)








       

    

    


