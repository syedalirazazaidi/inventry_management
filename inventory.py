# inventory.py

from typing import Dict

# Define the inventory dictionary with specified types for clarity
inventory: Dict[str, Dict[str, str | int | float]] = {}

def add_item(item_id: str, name: str, quantity: int, price: float) -> None:
    inventory[item_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    print(f"Item '{name}' added successfully!")

def update_item(item_id: str, name: str, quantity: int, price: float) -> None:
    if item_id in inventory:
        inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        print(f"Item '{name}' updated successfully!")
    else:
        print("Item not found!")

def view_item(item_id: str) -> None:
    if item_id in inventory:
        item = inventory[item_id]
        print(f"\nItem ID: {item_id}")
        print(f"Name: {item['name']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Price per unit: {item['price']}")
    else:
        print("Item not found!")

def delete_item(item_id: str) -> None:
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully!")
    else:
        print("Item not found!")

def view_all_items() -> None:
    if inventory:
        print("\nCurrent Inventory:")
        for item_id, item in inventory.items():
            print(f"ID: {item_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
    else:
        print("Inventory is empty!")
