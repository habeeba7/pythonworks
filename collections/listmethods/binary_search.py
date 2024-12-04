# linear search


# arr=[2,4,6,3,8,7]


# search_element=int(input("enter number:"))

# is_present=False

# for i in range(0,len(arr)):

#     if search_element==arr[i]:

#         is_present=True
#         break

# print(is_present)

# binary search

arr=[10,13,9,21,15,25,23]

arr.sort()

search_element=int(input("enter number:"))

is_present=False

low=0

upp=len(arr)-1

while(low<=upp):

    mid=(low+upp)//2

    if search_element==arr[mid]:

        is_present=True

        break

    elif search_element<arr[mid]:
        upp=mid-1

    elif search_element>arr[mid]:

        low=mid+1

print(is_present)






    



