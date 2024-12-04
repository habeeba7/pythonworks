#   - Create a program that appends user input to an existing file and then displays the entire content of the file.

f1=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\appendandDisplay.txt","a")


names=["abi","raj","mathu","thanu","sana"]

for n in names:
    
    f1.write(n+"\n")

f1.close()
