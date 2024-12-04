# multi level inheritance


class GrandParent:
    def m1(self):
        print("grand parent class m1 method")

class Parent(GrandParent):

    def m2(self):

        print("parent class m2 method")

class Child(Parent):

    def m3(self):

        print("child class m3 method")


Child_instance=Child()

Child_instance.m3()

Child_instance.m1()

Child_instance.m2()






# multiple inheritance

class GrandParent:
    def m1(self):
        print("grand parent class m1 method")

class Parent:

    def m2(self):

        print("parent class m2 method")

class Child(Parent,GrandParent):

    def m3(self):

        print("child class m3 method")


Child_instance=Child()

Child_instance.m3()

Child_instance.m1()

Child_instance.m2()





class GrandParent:
    def m(self):
        print("grand parent class m1 method")

class Parent:

    def m(self):

        print("parent class m2 method")

class Child(Parent,GrandParent):

    def m3(self):

        print("child class m3 method")


Child_instance=Child()

Child_instance.m3()

Child_instance.m()




