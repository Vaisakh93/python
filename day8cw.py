class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id


    def show_details(self):
        print(self.name, self.age, self.employee_id)

class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)
        self.working_hours = working_hours


    def show_details(self):
        print(self.name, self.age, self.working_hours)

class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(self.name, self.age, self.employee_id, self.working_hours, self.project_name)

person = Person("vaisakh", 26)
employee = Employee("suhail khan", 22, "SK23")
part_time = PartTime("suhail", 21, 18.0)
consultant = Consultant("karthikeyan", 21, "MN56", 12.0, "Python Development")

person.show_details()
employee.show_details()
part_time.show_details()
consultant.show_details()
