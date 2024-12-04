

# capitalize()
# casefold()
# isalpha()
# isdigit()
# isalnum()
# startswith(str)
# endswith(str)
# string.split()
# strip(){remove}
# lstrip()
# rstrip()
# replace()

text="helloPython"

# text=text.casefold()

# for ch in text:

#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":

        # print(ch)

    





for ch in text:

    print(ch)

print(text.capitalize())
print(text.casefold())

# print(text.isalpha())

# print(text.isdigit())

# print(text.isalnum())

# print(text.startswith("He"))

# print(text.endswith("on"))



# 

text="hello,world,python"

words=text.split(" ")

print(words)

# 

text="\t this is a line \t"

new_text=text.lstrip("\t")

print(new_text)

text="hello world python"
# o => a

new_text=text.replace("o","a")

print(new_text)

# 

text="python programming"
    # 012345678901234567
# string_object[start:end:step]

print(text[0:6])

# print(text[:6])

# print(text[7:])

# print(text[::2])

# print(text[::-1])

# string="hello"

# reversed_text=string[::-1]

# print(reversed_text)

# 

text="helloworld"
#     0123456789

# index of first o

# text.replace()
# text.index("o") #=>4

# print(text.index("o"))

# 
text="vipinkumar@gmail.com"

find_index=text.index("@")

username=text[0:find_index]

print(username)

print(text[0:text.index("@")])

# 

# text="hellopython"

# o_index=text.index("o")

# reversed_sub_str=text[o_index-1::-1]

# balance_sub_str=text[o_index:]

# result=reversed_sub_str+balance_sub_str

# print(result)

# 


















