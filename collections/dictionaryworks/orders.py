

orders=["tea","coffee","tea","coffee","gheeroat","plainroast","porotta","tea"]

summary_dictionary={}

for item in orders:

    if item in summary_dictionary:

        summary_dictionary[item]+=1

    else:

        summary_dictionary[item]=1

print(summary_dictionary)