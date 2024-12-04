
f=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\fruits.txt","r")

fruits=[]
for line in f:

    fruits.append(line.rstrip("\n"))
    
print(fruits)