from Modelle.Gericht import Dish

class Drink(Dish):
    def __init__(self, id, portion_size, price, alcohol):
        super().__init__(id, portion_size, price)
        self.alcohol = alcohol

    def __str__(self):
        return f"id:{self.id}, portion size:{self.portion_size}, price:{self.price}, alcohol:{self.alcohol}"
