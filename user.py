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

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] #it would be our database
    
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

ad = Admin("ashik",1234,"aasd@gmail.com","bajitpur")
ad.add_employee("sagor","sagor@gmail.com",464798,"rajibpur",23,"bussinessman",25000)
ad.view_empoyees()

