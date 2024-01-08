from Repository.DataRepo import DataRepo

class CustomerRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)
        self.customers = self.load()

    def create(self, customer):
        self.customers.append(customer)
        self.save(self.customers)

    def read(self):
        self.customers = self.load()
        return self.customers

    def update(self, id, new_name=None, new_address=None):
        for customer in self.customers:
            if customer.id == id:
                if new_name is not None:
                    customer.name = new_name
                if new_address is not None:
                    customer.address = new_address
        self.save(self.customers)


    def delete(self, id):
        for customer in self.customers:
            if customer.id == id:
                self.customers.remove(customer)
        self.save(self.customers)

    def search_by_name(self, partial_name):
        matching_customers = filter(lambda customer: partial_name.lower() in customer.name.lower(), self.customers)
        return list(matching_customers)

    def search_by_address(self, partial_address):
        matching_customers = filter(lambda customer: partial_address.lower() in customer.address.lower(), self.customers)
        return list(matching_customers)

    def convert_to_string(self, list):
        string_list = map(str, list)
        result = ','.join(string_list)
        return result

    def convert_from_string(self, string):
        return map(list, string.strip.split(','))\


