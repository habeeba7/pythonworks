
# Write and Read a File:
# Write a program to take input from the user and write it to a file. Then, read the content from the file and display it.

f1=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\read_write.txt","w")
f2=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\read_write.txt","r")

user_input=input("enter:")
for ui in user_input:

    f1.write(ui)

f1.close()
f2.close()
print(user_input)