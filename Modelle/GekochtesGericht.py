from Modelle.Gericht import Dish

class CookedDish(Dish):
    def __init__(self, id, portion_size, price, prep_time):
        super().__init__(id, portion_size, price)
        self.prep_time = prep_time

    def __str__(self) :
        return f"id:{self.id}, portion size:{self.portion_size}, price:{self.price}, prep_time:{self.prep_time}"

    def __eq__(self, other):
        if not isinstance(other, CookedDish):
            return False

        return (
                self.id == other.id and
                self.portion_size == other.portion_size and
                self.price == other.price and
                self.prep_time == other.prep_time
        )