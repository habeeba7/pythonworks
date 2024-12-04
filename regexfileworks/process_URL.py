

from re import fullmatch,finditer,findall

f=open("C:\\Users\\Habeeba\\Desktop\\python works\\regexfileworks\\URL.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)


