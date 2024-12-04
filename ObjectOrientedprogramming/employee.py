# employee(id,name,department,salary)



class Emloyee:

    id:int

    name:str

    department:str

    salary:int

    def set_employee(self,id,name,department,salary):

        self.id=id

        self.name=name

        self.department=department

        self.salary=salary

    def display(self):

        print(self.id,self.name,self.department,self.salary)

employee_instance1=Emloyee()

employee_instance1.set_employee(1002,"Ajith","HR",25000)

employee_instance1.display()
