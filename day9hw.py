class Account:
    def __init__(self, name, balance):
        self._name = name         
        self._balance = balance   
    def __add__(self, other):
        return self._balance + other._balance

    def display(self):
        return f"Account Holder: {self._name}, Balance: {self._balance}"

    def calculate_interest(self):
        return 0.0


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05


class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02

savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)

print("---- Account Details ----")

print(savings.display())
print(f"Interest (SavingsAccount): {savings.calculate_interest()}")

print(current.display())
print(f"Interest (CurrentAccount): {current.calculate_interest()}")

total_balance = savings + current

print("\n---- Total Balance ----")
print(f"Combined Balance (Ravi + Anjali): {total_balance}")
