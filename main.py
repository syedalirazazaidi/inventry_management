
from menu import display_menu
from inventory import add_item, update_item, view_item, delete_item, view_all_items
from utils import get_item_details

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            item_id, name, quantity, price = get_item_details()
            add_item(item_id, name, quantity, price)
        elif choice == '2':
            item_id = input("Enter item ID to update: ")
            name = input("Enter new item name: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price per unit: "))
            update_item(item_id, name, quantity, price)
        elif choice == '3':
            item_id = input("Enter item ID to view: ")
            view_item(item_id)
        elif choice == '4':
            item_id = input("Enter item ID to delete: ")
            delete_item(item_id)
        elif choice == '5':
            view_all_items()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
