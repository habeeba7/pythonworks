
# dictionary methods

# get(key)
# pop(key)
# keys()=>fetch all keys
# values()=>return all values
# items()=>return all keys and values



# employee id,name,department,age,salary

employee={"emp_id":234,"name":"rahul","department":"hr","age":24,"salary":25000}

# print(employee.get("department")) #get(key)
# inavlid key return none

# pop(key) remove

# employee.pop("salary")

# print(employee)


# return all keys=>keys()
for k in employee.keys():
    print(k)


# fetch all values=>values()
for v in employee.values():
    print(v)

#
# fetch key and valus=>items()
for k,v in employee.items():
    print(k,v)
