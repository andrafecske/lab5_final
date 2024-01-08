from Modelle.Identifizierbar import Identifiable

class Customer(Identifiable):
    def __init__(self, id, name, address):
        super().__init__(id)
        self.name = name
        self.address = address

    def __str__(self):
        return f"id:{self.id}, name:{self.name}, address:{self.address} "

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return False

        return (
                self.id == other.id and
                self.name == other.name and
                self.address == other.address)