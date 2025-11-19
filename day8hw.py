class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(self.name, self.role)

class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        print(self.name, self.role, self.specialization)

class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(self.name, self.role, self.yoga_style)

class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self, name, role, specialization)
        YogaInstructor.__init__(self, name, role, yoga_style)

    def display(self):
        print(self.name, self.role, self.specialization, self.yoga_style)

employee = Employee("Elisha Cuthbert", "Receptionist")
trainer = Trainer("Megan Fox", "Trainer", "Strength Training")
yoga_instructor = YogaInstructor("Ana de Armas", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("Emilia Clarke", "Senior Trainer", "CrossFit", "Vinyasa Yoga")

employee.display()
trainer.display()
yoga_instructor.display()
multi_trainer.display()
