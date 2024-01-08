from Repository.DataRepo import DataRepo

class CookedDishRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)
        self.cooked_dishes = self.load()

    def create(self, cooked_dish):
        self.cooked_dishes.append(cooked_dish)
        self.save(self.cooked_dishes)

    def read(self):
        self.cooked_dishes = self.load()
        return self.cooked_dishes

    def update(self, id, new_portion_size=None, new_price=None, new_prep_time=None):
        for cooked_dish in self.cooked_dishes:
            if cooked_dish.id == id:
                if new_portion_size is not None:
                    cooked_dish.portion_size = new_portion_size
                if new_price is not None:
                    cooked_dish.price = new_price
                if new_prep_time is not None:
                    cooked_dish.prep_time = new_prep_time

        self.save(self.cooked_dishes)


    def delete(self, id):
        for cooked_dish in self.cooked_dishes:
            if cooked_dish.id == id:
                self.cooked_dishes.remove(cooked_dish)
        self.save(self.cooked_dishes)

    def convert_to_string(self, list):
        string_list = map(str, list)
        result = ','.join(string_list)
        return result

    def convert_from_string(self, string):
        return map(list, string.strip.split(','))




