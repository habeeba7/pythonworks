

def findclosest(nums):
    closest=nums[0]

    for num in nums:
         if abs(num)<abs(closest) or abs(num)==abs(closest):
              closest=num

    return closest

nums=[-4,-2,1,4,8]

result=findclosest(nums)
print(result)
        

nums=[-4,-2,1,4,8]

closest=0


for i in nums:
     
    if abs(i) <abs(closest) :
         closest=i
         
    elif abs(i)==abs(closest) and i>closest:
         closest=i
       
print(closest)
    

