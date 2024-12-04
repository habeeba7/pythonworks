

text="hello"
#index012345678
# len 123456789
length=len(text)-1 #9-1

reversed_string=""

for i in range(4,-1,-1):

    reversed_string+=text[i]

print(reversed_string)