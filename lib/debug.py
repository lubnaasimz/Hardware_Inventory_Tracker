# lib/debug.py
from db import session
from models import Item

# Example: Query all items
def show_items():
    items = session.query(Item).all()
    for item in items:
        print(item)

if __name__ == "__main__":
    print("=== Debugging Database ===")
    show_items()
