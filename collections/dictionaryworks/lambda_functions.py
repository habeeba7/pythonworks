# lambda functions
# lambda function for adding 2 numbers

add=lambda num1,num2:num1+num2

print(add(100,200))

# lambda function for subtracting 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(45,34))

# lambda function for finding cube of a number

cube=lambda num:num**3

print(cube(5))

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("apple","mangos"))

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("hai","morning"))





smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,100))


words=["hello","hai","morning","test","apple"]

# def get_length(word):

#     return len(word)
get_length=lambda word:len(word)

print(max(words,key=get_length))
