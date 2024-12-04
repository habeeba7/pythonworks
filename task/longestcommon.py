
arr=["flower","flow","flight"]

def longest_common(arr):
    
    arr.sort()

    first=arr[0]

    last=arr[-1]

    i=0
    while i<len(first) and i<len(last) and first[i]==last[i]:

        i=i+1

    print(first[0:i])

print(longest_common(arr))

