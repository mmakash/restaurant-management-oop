from menu import Menu
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] #it would be our database
        self.menu = Menu()
    
    def add_employee(self,employee):
        self.employees.append(employee)

    def view_empoyees(self):
        print("employee list!!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)
        