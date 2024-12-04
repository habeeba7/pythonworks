


class Animal:

    name:str

    species:str

    def __init__(self,name,species):

        self.name=name

        self.species=species

    def __str__(self):

        return self.name
    
class Lion(Animal):

    def __ini__(self,name,species):

        super().__init__(name,species)

    def sound(self):

        print("grr")

lion_instance1=Lion("lion","carnivorous")

print(lion_instance1)
print(lion_instance1.sound())


class Cat(Animal):

    def __ini__(self,name,species):

        super().__init__(name,species)

    def sound(self):

        print("meow")

cat_instance1=Cat("cat","carnivorous")

print(cat_instance1)
print(cat_instance1.sound())


    

    
    