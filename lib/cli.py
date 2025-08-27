from helpers import add_item, view_items, update_stock, delete_item, exit_program

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_item()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Try again.")

def menu():
    print("\n====== Hardware Inventory Tracker ======")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Stock")
    print("4. Delete Item")
    print("0. Exit")

if __name__ == "__main__":
    main()
