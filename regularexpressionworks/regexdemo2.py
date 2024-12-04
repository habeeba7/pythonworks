
from re import finditer

text="I have 3 cars,2 bike and 1-cycle"

# pattern="[abc]" either a or b or c

# pattern="[a-z]" #chk for all lowercase alphabets

# pattern="[a-zA-Z]" #chk for all alphabets

# pattern="[0-9]" #chk for all digits

# pattern="[a-zA-Z0-9]" #chk for all alphanumerics

# pattern="[^ak]" exclude a,k

pattern="[^akA-Z0-9, ]"

# pattern="[^a-zA-Z0-9]" #chk for all special characters

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),m.group())


