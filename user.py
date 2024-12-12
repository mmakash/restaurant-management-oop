from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

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
        restaurant.menu.add_employee(item)
        
    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self,restaurant,item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            pass
        else:
            print("item not found")
    
    def view_cart(self):
        print("view cart")
        print("Name\tPrice\tQuantity")

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] #it would be our database
        self.menu = FoodItem()
    
    def add_employee(self,employee):
        self.employees.append(employee)

    def view_empoyees(self):
        print("employee list!!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)
        
class Menu:
    def __init__(self):
        self.items = []

    def add_menu_itm(self,item):
        self.items.append(item)
    
    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item deleted")
        else:
            print("item not found")
    def show_menu(self):
        print("***menu***")
        print(f"Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

# ad = Admin("ashik",1234,"aasd@gmail.com","bajitpur")
# ad.add_employee("sagor","sagor@gmail.com",464798,"rajibpur",23,"bussinessman",25000)
mn = Menu()
item = FoodItem("pizza",12.45,10)
mn.add_menu_itm(item)
mn.show_menu()


