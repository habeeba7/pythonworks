

from re import findall

f=open("C:\\Users\\Habeeba\\Desktop\\python works\\regexfileworks\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

date=findall(pattern,content)

for data in date:

    print(data)