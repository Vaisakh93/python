from abc import ABC, abstractmethod
from datetime import datetime

CURRENT_YEAR = 2025

class User(ABC):
    def __init__(self, name, year_joined):
        self.name = name
        self.year_joined = year_joined
    
    def years_on_platform(self):
        return CURRENT_YEAR - self.year_joined
    
    @abstractmethod
    def role(self):
        """Return the role of the user (implemented by subclasses)."""
        pass
    
    def __str__(self):
        return f"{self.name} - {self.role()} for {self.years_on_platform()} years"


class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"



c = Customer("leodas", 2020)
v = Vendor("Benz", 2018)

print(c) 
print(v) 
