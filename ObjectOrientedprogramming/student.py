# student()
# set student()
# display student()



class Student:
# optional
    name:str

    rollnumber:int

    age:int

    course:str
# initializing attributes of student
    def set_student(self,name,rollnumber,age,course):

        self.name=name

        self.rollnumber=rollnumber

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.rollnumber,self.age,self.course)

    # reference name=className()

student_instance=Student()



student_instance.set_student("Abhi",10,23,"django")

student_instance.display()

    
        
        
       

