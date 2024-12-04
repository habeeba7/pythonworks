#  Write a program to count the number of words in a given text file.


f=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\word_count.txt","r")

words=[]
for line in f:

    words.append(line.rstrip("\n"))

print(len(words))


