
f=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\frame_works.txt","a")

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:

    f.write(fw+"\n")

f.close()