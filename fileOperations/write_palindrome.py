
read_path="C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\words.txt"
write_path="C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\palindrome.txt"

f_read=open(read_path,"r")

f_write=open(write_path,"w")

for line in f_read:

    word=line.rstrip("\n")

    reversd_word=word[::-1]

    if word==reversd_word:

        f_write.write(word+"\n")

f_read.close()

f_write.close()

