from Repository.DataRepo import DataRepo

class DrinkRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)
        self.drinks = self.load()

    def create(self, drink):
        self.drinks.append(drink)
        self.save(self.drinks)

    def read(self):
        self.drinks = self.load()
        return self.drinks

    def update(self, id, new_portion_size=None, new_price=None, new_alcohol=None):
        for drink in self.drinks:
            if drink.id == id:
                if new_portion_size is not None:
                    drink.portion_size = new_portion_size
                if new_price is not None:
                    drink.price = new_price
                if new_alcohol is not None:
                    drink.alcohol = new_alcohol
        self.save(self.drinks)

    def delete(self, id):
        for drink in self.drinks:
            if drink.id == id:
                self.drinks.remove(drink)
        self.save(self.drinks)

    def convert_to_string(self, list):
        string_list = map(str, list)
        result = ','.join(string_list)
        return result

    def convert_from_string(self, string):
        return map(list, string.strip.split(','))
