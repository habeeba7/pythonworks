
year_path="C:\\\\Users\\Habeeba\\Desktop\\python works\\datasets\\year.txt"
century_path="C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\century_year.txt"
leap_path="C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\leap_year.txt"

f_read=open(year_path,"r")
f_century=open(century_path,"w")
f_leapyear=open(leap_path,"w")

for year in f_read:
    year=int(year)

    if year%100==0:
        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        f_leapyear.write(str(year)+"\n")

f_read.close()
f_century.close()
f_leapyear.close()