# begin
# end
# read from user

# print all odd numbers from begin to end

begin=int(input("enter starting limit:"))#50

end=int(input("enter limit:"))#10

# if begin greater than end swap begin and end

if begin>end:
     begin,end=end,begin

i=begin

while(i<=end):

    if i%2!=0:
        
        print(i)
    
    i=i+1