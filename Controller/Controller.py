from Modelle.GekochtesGericht import CookedDish
from Modelle.Getrank import Drink
from Modelle.Kunde import Customer
from Modelle.Bestellung import Order

from Repository.CookedDishRepo import CookedDishRepo
from Repository.DrinkRepo import DrinkRepo
from Repository.CustomerRepo import CustomerRepo
from Repository.OrderRepo import OrderRepo


class RestaurantController:
    def __init__(self):
        self.cooked_dish_repo = CookedDishRepo('cooked_dishes.txt')
        self.drink_repo = DrinkRepo('drinks.txt')
        self.customer_repo = CustomerRepo('customers.txt')
        self.order_repo = OrderRepo('orders.txt')

    def add_dish_to_repo(self, id, portion_size, price, prep_time):
        new_dish = CookedDish(id, price, portion_size, prep_time)
        self.cooked_dish_repo.create(new_dish)

    def add_drink_to_repo(self, id, portion_size, price, alcohol):
        new_drink = Drink(id, portion_size, price, alcohol)
        self.drink_repo.create(new_drink)

    def add_customer_to_repo(self, id, name, address):
        new_customer = Customer(id, name, address)
        self.customer_repo.create(new_customer)

    def add_order_to_repo(self, id, costumer_id, dishes_ids, drinks_ids, time_of_order):
        new_order = Order(id, costumer_id, dishes_ids, drinks_ids, time_of_order)
        new_order.calculate_arrival()
        new_order.calculateCosts()
        self.order_repo.create(new_order)

    def print_cooked_dishes(self):
        dishList = self.cooked_dish_repo.read()
        for dish in dishList:
            print(dish)

    def print_customers(self):
        customerList = self.customer_repo.read()
        for customer in customerList:
            print(customer)

    def print_drinks(self):
        drinksList = self.drink_repo.read()
        for drink in drinksList:
            print(drink)
    def print_orders(self):
        ordersList = self.order_repo.read()
        for order in ordersList:
            print(order)

    def print_invoice(self , order_id):
        ordersList = self.order_repo.read()
        for order in ordersList:
            if order.id == order_id:
                order.show_invoice()

    def find_customer_by_name(self, partial_name):
        result = self.customer_repo.search_by_name(partial_name)
        return result

    def find_costumer_by_address(self, partial_address):
        result = self.customer_repo.search_by_address(partial_address)
        return result


