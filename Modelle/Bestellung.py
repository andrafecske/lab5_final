import functools
from datetime import datetime, timedelta

from Modelle.Identifizierbar import Identifiable
from Repository.CookedDishRepo import CookedDishRepo
from Repository.DrinkRepo import DrinkRepo


class Order(Identifiable):
    def __init__(self, id, customer_id, dishes_ids, drinks_ids, time_of_order):
        super().__init__(id)
        self.customer_id = customer_id
        self.dishes_ids = dishes_ids
        self.drinks_ids = drinks_ids
        self.time_of_order = time_of_order
        self.estimatedTime = 0
        self.total_costs = 0
        self.total_prep_time = 0

    def __str__(self):
        return f"id: {self.id}, customer_id:{self.customer_id}, dishes_ids:{self.dishes_ids}, drinks_ids:{self.drinks_ids}, time of order: {self.time_of_order}, estimated time: {self.estimatedTime}, total costs: {self.total_costs} "


    def calculateCosts(self):
       dish_menu = CookedDishRepo("C:\Coding\lab5_final\cooked_dishes.txt")
       drink_menu = DrinkRepo ("C:\Coding\lab5_final\drinks.txt")
       dishList = dish_menu.load()
       drinkList = drink_menu.load()
       prices = []

       for dish in dishList:
           if dish.id in self.dishes_ids:
               prices.append(int(dish.price))

       for drink in drinkList:
           if drink.id in self.drinks_ids:
               prices.append(int(drink.price))

       self.total_costs = functools.reduce(lambda x, y: x + y , prices)

    def calculatePrepTime(self):
        dish_menu = CookedDishRepo("C:\Coding\lab5_final\cooked_dishes.txt")
        dishList = dish_menu.load()
        time = []

        for dish in dishList:
            if dish.id in self.dishes_ids:
                time.append(dish.prep_time)

        self.total_prep_time = functools.reduce(lambda x, y: x + y, time)

    def calculate_arrival(self):

        self.calculatePrepTime()
        initial_time = datetime.strptime(self.time_of_order, '%H:%M')
        new_time = initial_time + timedelta(minutes=self.total_prep_time)
        self.estimatedTime = new_time.strftime('%H:%M')

        return self.estimatedTime

    def __create_invoice(self):
        dish_menu = CookedDishRepo("C:\Coding\lab5_final\cooked_dishes.txt")
        drink_menu = DrinkRepo("C:\Coding\lab5_final\drinks.txt")
        dishList = dish_menu.load()
        drinkList = drink_menu.load()

        def format_item(item):
            return f"{item}\n"

        dish_invoice = "".join(map(format_item, (dish for dish in dishList if dish.id in self.dishes_ids)))
        drink_invoice = "".join(map(format_item, (drink for drink in drinkList if drink.id in self.drinks_ids)))

        invoice = f"{dish_invoice}{drink_invoice}{self.total_costs}"
        return invoice

    def show_invoice(self):
        invoice = self.__create_invoice()
        print("your invoice for the order:")
        print(invoice)



