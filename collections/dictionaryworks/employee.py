

employee={"eid":3045,"name":"Arun","salary":26000,"department":"hr","experience":6}

print(employee["experience"])

# add contact as 33445465

employee["contact"]=343545

print(employee)

# if experience > 5 update employee salary as current_salary+10000
#    else current_salary +5000

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)

# add role as SDE IF EXP>5 else add role as JDE

if employee["experience"]>5:

    employee["role"]="SDE"

else:
    employee["role"]="JDE"

print(employee)