
cars=[
    {
        "id":1,"name":"fronx","price":1200000,"brand":"nexa",
     "colors":["red","blue","white"],
     "transmissions":["manuel","amt","cvt"]
     },
    {
        "id":2,"name":"baleno","price":1100000,"brand":"nexa",
        "colors":["grey","blue","white"],
        "transmissions":["manuel","amt","cvt"]
    },
    {
        "id":3,"name":"3xo","price":900000,"brand":"mahindra",
        "colors":["red","white","black"],
        "transmissions":["amt","cvt"]
    },
    {
        "id":4,"name":"punch","price":700000,"brand":"tata",
        "colors":["red","blue","white","green"],
        "transmissions":["manuel","cvt"]
    },
    {
        "id":5,"name":"nexon","price":1400000,"brand":"tata",
        "colors":["red","white"],
        "transmissions":["manuel","amt","cvt"]
    },
    {
        "id":6,"name":"kiger","price":1000000,"brand":"renault",
        "colors":["blue","white"],
        "transmissions":["manuel","cvt","dct"]
    },
    {
        "id":7,"name":"taigun","price":2300000,"brand":"volkswagon",
        "colors":["red","blue","white"],
        "transmissions":["manuel","cvt","torque"]
    },
]

# print count of vehicles

print(f"total number of vehicles=> {len(cars)}")


# print available colors in baleno
colors_baleno=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(colors_baleno)


# print all brands
all_brands=[c.get("brand") for c in cars]
print(set(all_brands))


# print car names available in amt transmission
amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_cars)


# cars available in blue colors
cars_colors=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(cars_colors)


# print all trasmission
all_transmission={t for c in cars for t in c.get("transmissions")}
print(all_transmission)


# print all colors
all_colors={cl for c in cars for cl in c.get("colors")}
print(all_colors)


# most popular color
# popular_color=[c.get("colors") for c in cars]
# print(popular_color)
# color_count={p:popular_color.count(p) for p in popular_color}
# print(color_count)


# costly cars
costly_car=max(cars,key=lambda d:d.get("price"))
print(costly_car.get("name"))


# cars with minimum cost
low_cost_car=min(cars,key=lambda d:d.get("price"))
print(low_cost_car.get("name"))


# sort cars
sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)
sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")]for c in sorted_car}
print(sorted_car_name)



