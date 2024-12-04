

employee={"id":100,"name":"vipin","department":"hr","salary":2500}

product={"id":200,"title":"kitkat","price":72,"brand":"nestle"}

print(product["brand"])

# update product price as 50

product["price"]=50

product["brand"]="parle"

print(product)

# add offer as 10 if offer exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)