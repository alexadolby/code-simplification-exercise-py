
from datetime import datetime
import os

checkout_at = datetime.now().strftime("%M/%d/%Y %I:%m %p")

selected_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
] # FYI: for the purposes of this exercise, you won't need to modify this list at all

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71





now = datetime.now()

subtotal = sum([p["price"] for p in selected_products])

# PRINT RECEIPT
recipt = ""

reciept += "\n---------"
reciept += "\nCHECKOUT AT: " + str(now.strftime("%Y-%M-%d %H:%m:%S"))
reciept += "\n---------"

for p in selected_products:
    reciept += "\nSELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"])

reciept += "\n---------"
reciept += f"\nSUBTOTAL: {to_usd(subtotal)}"
reciept += f"\nTAX: {to_usd(subtotal * 0.0875)}"
reciept += f"\nTOTAL: {to_usd((subtotal * 0.0875) + subtotal)}"
reciept += "\n---------"
reciept += "\nTHANK YOU! PLEASE COME AGAIN SOON!"
reciept += "\n---------"

print(reciept)
# WRITE RECEIPT TO FILE

file_name = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{now.strftime('%Y-%M-%d-%H-%m-%S')}.txt")
with open(file_name, 'w') as f:
    f.write(reciept)

# TODO: SEND RECEIPT VIA EMAIL
