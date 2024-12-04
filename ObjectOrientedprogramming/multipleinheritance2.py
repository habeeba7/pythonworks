# Cusine(cusine_name)
# MealType(name)
# Dish(dish_name) display_dish_info()

# indian,break_fast,gheeroast,
# italian,
# break_fast
# pasta


class Cusine:

    name:str

    def __init__(self,name):

        self.name=name

    def display_cusine_info(self):

        print(self.name)


class MealType:

    name:str

    def __init__(self,meal_name):

        self.meal_name=meal_name


    def display_mealtype_info(self):

        print(self.meal_name)


class Dish(Cusine,MealType):

    def __init__(self,name,meal_name,dish_name):

        Cusine.__init__(self,name)

        MealType.__init__(self,meal_name)

        self.dish_name=dish_name

    def display_dish_info(self):

        self.display_cusine_info()

        self.display_mealtype_info()

        print(self.dish_name)


dish_instance=Dish("indian","breakfast","gheeroast")

dish_instance.display_dish_info()