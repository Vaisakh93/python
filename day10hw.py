from abc import ABC, abstractmethod

CURRENT_YEAR = 2025

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return CURRENT_YEAR - self.account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"[Admin] {self.name} • Account Age: {self.account_age()} years"


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"[Guest] {self.name} • Account Age: {self.account_age()} years"


admin_user = Admin("Izuku", 2019)
guest_user = Guest("Midoriya", 2023)

print("Admin Role:", admin_user.get_role())
print("Admin Age:", admin_user.account_age())
print(admin_user)

print("\nGuest Role:", guest_user.get_role())
print("Guest Age:", guest_user.account_age())
print(guest_user)
