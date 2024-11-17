class Restaurant:
    menu_items = []
    customer_orders = []
    book_table = {1: False, 2: False, 3: False, 4: False, 5: False}
    def add_item_to_menu(self, itemname):
        self.menu_items.append(itemname)

    def book_tables(self):
        for i in self.book_table:
            if not self.book_table[i]:
                self.book_table[i] = True
                return
        print("No tables available")

    def customer_order(self, itemName):
        if itemName in self.menu_items:
            self.customer_orders.append(itemName)

    def display_menu_items(self):
        print(self.menu_items)

    def display_customer_orders(self):
        print(self.customer_orders)

    def display_book_table(self):
        for i in self.book_table:
            print(f"Table {i}: {self.book_table[i]}")

obj1 = Restaurant()
obj1.add_item_to_menu("Item1")
obj1.add_item_to_menu("Item2")
obj1.add_item_to_menu("Item3")
obj1.add_item_to_menu("Item4")
obj1.book_tables()
obj1.customer_order("Item1")
obj1.customer_order("Item4")

obj1.display_menu_items()
obj1.display_book_table()
obj1.display_customer_orders()