# Hardware Inventory Tracker CLI

A simple **command-line application** to manage a hardware store’s inventory using **Python** and **SQLAlchemy ORM**.

---

## Features

* Add new items (name, category, quantity, price).
* View all items in inventory (formatted tables with **tabulate**).
* Update stock levels.
* Delete items.
* Persistent storage with **SQLite database**.

---

## Setup

Clone the repository and install dependencies with **Pipenv**:

```sh
pipenv install
pipenv shell
python lib/cli.py
```

---

## Dependencies

* [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database modeling.
* [Alembic](https://alembic.sqlalchemy.org/) – Database migrations.
* [tabulate](https://pypi.org/project/tabulate/) – Pretty-printing tables in CLI.
* [colorama](https://pypi.org/project/colorama/) *(optional)* – For colored CLI messages.

---

## Project Structure

```
hardware-inventory-cli/
│── lib/
│   ├── cli.py          # Main CLI entry point
│   ├── helpers.py      # CLI functions (add, view, update, delete)
│   ├── models.py       # SQLAlchemy ORM models
│   └── db.py           # Database setup
│── migrations/         # Alembic migration files
│── Pipfile             # Dependencies
│── Pipfile.lock
│── README.md
```

---

## Usage

Run the app:

```sh
python lib/cli.py
```

Menu options:

```
=== Hardware Inventory Tracker ===
1. Add Item
2. View All Items
3. Update Item
4. Delete Item
5. Exit
```

---

## Example Workflow

1. **Add Item**

   ```
   Enter name: Drill
   Enter category: Tools
   Enter quantity: 5
   Enter price: 40.00
   Item added successfully!
   ```

2. **View Items**

   ```
   ╒════╤═════════════╤═══════════╤═════════════╤══════════╕
   │ ID │ Name        │ Quantity  │ Category    │ Price    │
   ╞════╪═════════════╪═══════════╪═════════════╪══════════╡
   │ 1  │ Drill       │ 5         │ Tools       │ 40.00    │
   ╘════╧═════════════╧═══════════╧═════════════╧══════════╛
   ```

3. **Update Item**

   ```
   Enter item ID to update: 1
   Enter new quantity: 10
   Item updated successfully!
   ```

4. **Delete Item**

   ```
   Enter item ID to delete: 1
   Item deleted successfully!
   ```

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

