from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("item quantity execeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added!!!")
        else:
            print("item not found")
    
    def view_cart(self):
        print("view cart")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t {quantity}")
        print(f"Total price: {self.cart.total_price}")

    def pay_bill(self):
        print(f"total {self.cart.total_price} paid successfully")
        self.cart.clear()






class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee("rahim", "rahim@gmail.com", 1279787, "Dhaka", 23, "Chef", 12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_empoyees(self,restaurant):
        restaurant.view_empoyees()

    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
        
    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

    def view_menu(self, retaurent):
        retaurent.menu.show_menu()



