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
        self.employees = [] #it would be our database

    def add_employee(self,name,email,phone,address,age,designation,salary):
        employee = Employee(name,email,phone,address,age,designation,salary)
        self.employees.append(employee)
        print(f"{name} is added!!")

    def view_empoyees(self):
        print("employee list!!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)

ad = Admin("ashik",1234,"aasd@gmail.com","bajitpur")
ad.add_employee("sagor","sagor@gmail.com",464798,"rajibpur",23,"bussinessman",25000)
ad.view_empoyees()

