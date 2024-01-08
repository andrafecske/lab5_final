from Controller.Controller import RestaurantController


class Console:
    def __init__(self):
        self.controller = RestaurantController()

    def menu(self):
        print(""" Hello! What would you like to do?
            1 - register a new order
            2 - print an invoice by the id of the order 
            3 - manage menu
            4 - list the existing dishes, drinks or customers
            5 - list orders
            0 - exit
        
        """)
    def run(self):
        while True:
            self.menu()
            value = int(input("Your option: "))

            if value == 0:
                break

            if value == 1:
                # Option for adding a new order
                id = int(input("ID of the order: "))
                print("""
                        1 - search customer by name
                        2 - search customer by address
                        3 - add new customer
                """)
                choice = int(input())

                if choice == 1:
                    partial_name = input("partial name:")
                    potential_customers = self.controller.find_customer_by_name(partial_name)
                    for customers in potential_customers:
                        print(customers.__str__())

                    client_id = int(input("chosen client id:"))

                if choice == 2:
                    partial_address = input("partial address:")
                    potential_customers = self.controller.find_costumer_by_address(partial_address)
                    for customers in potential_customers:
                        print(customers.__str__())
                    client_id = int(input("chosen client id:"))

                if choice == 3:
                    id = int(input("ID of the client:"))
                    name = input("Name of the client:")
                    address = input("Address of the client:")
                    client_id = id
                    self.controller.add_customer_to_repo(id, name, address)

                dishes_ids = []
                drinks_ids = []
                while True:
                    print("""
                            1 - add dish to order
                            2 - add drink to order
                            0 - exit order
                    """)
                    opt = int(input())
                    if opt == 1:
                        self.controller.print_cooked_dishes()
                        new_id = int(input("id of dish:"))
                        dishes_ids.append(new_id)

                    if opt == 2:
                        self.controller.print_drinks()
                        new_id = int(input("id of drink:"))
                        drinks_ids.append(new_id)

                    if opt == 0:
                        break
                time_of_order = input("Time of order, please use the HH:MM format")
                self.controller.add_order_to_repo(id, client_id, dishes_ids, drinks_ids, time_of_order)


            if value == 2:
                # Option for generating and printing an invoice
                self.controller.print_orders()
                id = int(input("ID of the order you want the invoice for:"))
                self.controller.print_invoice(id)


            if value == 3:
                # Option for managing the menu: you can create, update or delete
                while True:
                    print (""" Managing the menu:
                     1 - add a new dish, a new drink or a new customer
                     2 - update
                     3 - delete
                     0 - exit
                    """)
                    opt = int(input("Your option:"))
                    if opt == 1:
                        while True:
                            print(""" 
                                What would you like to add to the menu?
                                    1 - add new dish
                                    2 - add new drink
                                    3 - add new customer
                                    0 - exit
                            """)
                            add = int(input('Your option: '))
                            if add == 1:
                                print("Create a new cooked dish: ")
                                id = int(input("ID of the cooked dish: "))
                                portion_size = input("Portion of the cooked dish: ")
                                price = int(input("Price of the cooked dish: "))
                                prep_time = int(input("Prep time of the dish: "))

                                self.controller.add_dish_to_repo(id, portion_size, price, prep_time)

                            if add == 2:
                                print("Create a new drink: ")
                                id = int(input("ID of the drink:"))
                                portion_size = input("Portion of the drink:")
                                price = int(input("Price of the drink:"))
                                alcohol = int(input("Alcohol contained in the drink:"))

                                self.controller.add_drink_to_repo(id, portion_size, price, alcohol)

                            if add == 3:
                                id = int(input("ID of the client:"))
                                name = input("Name of the client:")
                                address = input("Address of the client:")
                                self.controller.add_customer_to_repo(id, name, address)

                            if add == 0:
                                break

                    if opt == 2:
                        print("""
                            What would you like to update?
                                1 - dish
                                2 - drink
                                3 - customer
                                
                        """)

                        new_name = None
                        new_address = None
                        new_portion_size = None
                        new_price = None
                        new_prep_time = None
                        new_alcohol = None
                        upd = int(input())
                        if upd == 1:
                            self.controller.print_cooked_dishes()
                            id = int(input("id of the dish you want to change:"))
                            print("""
                            what do you want to change?
                            1 - portion size
                            2 - price
                            3 - prep time
                            """)

                            choice = int(input())
                            if choice == 1:
                                new_portion_size = int(input())
                            if choice == 2:
                                new_price = int(input())
                            if choice == 3:
                                new_prep_time = int(input())

                            self.controller.cooked_dish_repo.update(id, new_portion_size, new_price, new_prep_time)

                        if upd == 2:
                            self.controller.print_drinks()

                            id = int(input("id of the drink you want to change:"))
                            print("""what do you want to change?
                                        1 - portion size
                                        2 - price
                                        3 - alcohol
                            """)

                            choice = int(input())
                            if choice == 1:
                                new_portion_size = int(input("new portion size:"))
                            if choice == 2:
                                new_price = int(input("new price:"))
                            if choice == 3:
                                new_alcohol= int(input("new alcohol content:"))
                            self.controller.drink_repo.update(id, new_portion_size, new_price, new_alcohol)
                        if upd == 3:
                            self.controller.print_customers()

                            id = int(input("id of the customer you want to change:"))
                            print(""" what do you want to change?
                                            1 - name
                                            2 - address
                            """)

                            choice = int(input())
                            if choice == 1:
                                new_name = input("new name:")
                            if choice == 2:
                                new_address = input("new address:")

                            self.controller.customer_repo.update(id, new_name, new_address)

                    if opt == 3:
                        print(""" What do zou want to delete?
                                    1 - dish
                                    2 - drink
                                    3 - customer
                        """)
                        dlt = int(input("your choice:"))
                        if dlt == 1:
                            self.controller.print_cooked_dishes()
                            id = int(input("id of the dish you want to delete:"))
                            self.controller.cooked_dish_repo.delete(id)
                        if dlt == 2:
                            self.controller.print_drinks()
                            id = int(input("id of the drink you want to delete:"))
                            self.controller.drink_repo.delete(id)
                        if dlt == 3:
                            self.controller.print_customers()
                            id = int(input("id of the customer you want to delete:"))
                            self.controller.customer_repo.delete(id)
                    if opt == 0:
                        break

            if value == 4:
                # Option for printing existing lists of dishes, drinks and clients
                while True:
                    print("""What would you like to be listed?
                                1 - the dishes
                                2 - the drinks
                                3 - the customers
                                0 - exit
                    """)
                    lst = int(input("Your option: "))
                    if lst == 1:
                        self.controller.print_cooked_dishes()
                    if lst == 2:
                        self.controller.print_drinks()
                    if lst == 3:
                        self.controller.print_customers()
                    if lst == 0:
                        break

            if value == 5:
                # Option for printing the existing orders
                self.controller.print_orders()


