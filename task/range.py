

def range(num):

    result=[]

    i=0

    while i<len(num):

        start=num[i]

        while i<len(num)-1 and num[i]+1==num[i+1]:

            i=i+1

        if start!=num[i]:

            result.append(str(start)+ '->' +str(num[i]))

        else:

            result.append(str(num[i]))

        i=i+1

    return result

num1=[0,1,2,4,5,7]
print(range(num1))

num2=[0,2,3,4,6,8,9]
print(range(num2))

