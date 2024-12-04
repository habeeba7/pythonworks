
from re import fullmatch,finditer

f=open("C:\\Users\\Habeeba\\Desktop\\python works\\regexfileworks\\social_post.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())
