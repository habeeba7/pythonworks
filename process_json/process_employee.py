from json import load

f=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\employee.json")
data=load(f)

for emp in data:
    print(emp)