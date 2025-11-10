import random

price_rice = 45.0
price_sugar = 40.0
price_oil = 130.0

qty_rice = 3.0
qty_sugar = 2.5
qty_oil = 1.8

total_rice = price_rice * qty_rice
total_sugar = price_sugar * qty_sugar
total_oil = price_oil * qty_oil

print("Total price for rice: ₹", total_rice)
print("Total price for sugar: ₹", total_sugar)
print("Total price for oil: ₹", total_oil)

total_bill = total_rice + total_sugar + total_oil
print("\nFinal total bill (float): ₹", total_bill)

total_bill_int = int(total_bill)
print("Final total bill (integer): ₹", total_bill_int)

total_bill_str = str(total_bill)
print("The total bill amount is ₹" + total_bill_str)

delivery_charge = random.randint(5, 10)
final_amount = total_bill + delivery_charge

print("\nDelivery charge: ₹", delivery_charge)
print("Final bill amount (including delivery): ₹", final_amount)
