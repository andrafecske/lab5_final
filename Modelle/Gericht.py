from Modelle.Identifizierbar import Identifiable

class Dish(Identifiable):
    def __init__(self, id, portion_size, price):
        super().__init__(id)
        self.portion_size = portion_size
        self.price = price

    def __str__(self) -> str:
        return super().__str__()
