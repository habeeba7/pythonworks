
# i  0 1 2 3 
arr=[2,3,4,5]
# j  0 1 2 3

sum=int(input("enter sum:"))

for i in range(0,len(arr)-1):
     
     for j in range(i+1,len(arr)):
          
          cur_sum=arr[i]+arr[j]

          if sum==cur_sum:
               
               print(arr[i],arr[j])

               break
          



    