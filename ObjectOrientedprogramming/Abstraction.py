
from abc import ABC,abstractmethod

class Bike(ABC): #abstract class


    @abstractmethod
    def start(self):   #abstract methods
        pass
    
    @abstractmethod
    def accelerated(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class Hunter(Bike):

    def start(self):
        print("hunter start method")

    def accelerated(self):
        print("hunter accelerate method ")

    def stop(self):
        print("hunter stop method")


hunter_instance=Hunter()

hunter_instance.stop()












