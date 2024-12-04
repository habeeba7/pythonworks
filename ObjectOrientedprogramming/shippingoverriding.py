

class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)


class ExpressShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        print(weight*20)


class StandardShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        print(weight*10)


Std_instance=StandardShipping()

Std_instance.calculate_shipping_cost(5)

exp_instance=ExpressShipping()

exp_instance.calculate_shipping_cost(5)




