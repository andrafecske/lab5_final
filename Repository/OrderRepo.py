from Repository.DataRepo import DataRepo

class OrderRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)
        self.orders = self.load()

    def create(self, order):
        self.orders.append(order)
        self.save(self.orders)

    def read(self):
        self.orders = self.load()
        return self.orders

    def convert_to_string(self, list):
        string_list = map(str, list)
        result = ','.join(string_list)
        return result

    def convert_from_string(self, string):
        return map(list, string.strip.split(','))
