# utils.py
from typing import Tuple

def get_item_details() -> Tuple[str, str, int, float]:
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    return item_id, name, quantity, price
