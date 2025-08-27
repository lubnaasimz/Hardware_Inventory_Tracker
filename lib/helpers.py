# lib/helpers.py
from models import Item, session  # make sure models.py has Item + session setup
from tabulate import tabulate


# ------------------ Add Item ------------------
def add_item():
    name = input("Enter item name: ")
    category = input("Enter category: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Quantity must be an integer and price must be a number.")
        return

    item = Item(name=name, category=category, quantity=quantity, price=price)
    session.add(item)
    session.commit()
    print(f"Added {item.name} to inventory.")

# ------------------ View Items ------------------
def view_items():
    items = session.query(Item).all()
    if items:
        table = [[item.id, item.name, item.quantity, item.category] for item in items]
        headers = ["ID", "Name", "Quantity", "Category"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))
    else:
        print("No items in inventory.")

# ------------------ Update Stock ------------------
def update_stock():
    try:
        item_id = int(input("Enter item ID to update: "))
    except ValueError:
        print("Please enter a valid number for the item ID.")
        return

    item = session.query(Item).get(item_id)
    if item:
        try:
            new_qty = int(input(f"Enter new quantity for {item.name}: "))
        except ValueError:
            print("Quantity must be a number.")
            return

        item.quantity = new_qty
        session.commit()
        print(f"Updated {item.name} to {new_qty} in stock.")
    else:
        print("Item not found.")

# ------------------ Delete Item ------------------
def delete_item():
    try:
        item_id = int(input("Enter item ID to delete: "))
    except ValueError:
        print("Please enter a valid number for the item ID.")
        return

    item = session.query(Item).get(item_id)
    if item:
        session.delete(item)
        session.commit()
        print(f"Deleted {item.name}.")
    else:
        print("Item not found.")

# ------------------ Exit Program ------------------
def exit_program():
    print("Goodbye!")
    exit()
