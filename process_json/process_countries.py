
from json import load

f=open("C:\\Users\\Habeeba\\Desktop\\python works\\datasets\\countries.json",encoding="UTF-8")

data=load(f)

# print number of countries
# print(len(data))

# print all country names
all_country_name=[country.get("name") for country in data]
# print(all_country_name)

# print all region
all_regions=[country.get("region") for country in data]

print(set(all_regions))
regions_count={region:all_regions.count(region) for region in all_regions  }
print(regions_count)

max_region_count=max(regions_count,key=lambda k:regions_count.get(k))
print(max_region_count)

# capital of india
country_capital=[country.get("capital") for country in data if country.get("name")=="India"]
# print(country_capital)

# countries with most number of borders
country_borders={country.get("name"):len(country.get("borders",[])) for country in data }
# print(country_borders)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)

# most populated country
country_population=max(data,key=lambda country:country.get("population",0)).get("name")
# print(country_population)

alpha_three_code=[country.get("borders") for country in data if country.get("name")=="India"][0]

# for code in alpha_three_code:

#     for country in data:

#         if country.get("alpha3Code")==code:
            # print(country.get("name"))
