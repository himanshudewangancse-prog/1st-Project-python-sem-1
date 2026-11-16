# Inventory Management System

A simple console app in Python for keeping track of shop inventory. You can add items, look at them, update them, search, delete, and see how much your stock is worth, all from a text menu in the terminal.

I built this as part of my B.Tech Computer Science and Engineering coursework at Rungta International Skills University (Project Statement 14). The goal was to practice the basics: lists, dictionaries, functions, and CRUD operations, without using any external libraries.

## What it can do

- **Add an item** with a name, quantity, and price. Each item automatically gets a unique ID.
- **View all items** in a neat, one-line-per-item format.
- **Update an item** by its ID. Press Enter on any field to keep the old value.
- **Delete an item** by its ID.
- **Search an item** by name (not case-sensitive).
- **Calculate total stock value** (quantity x price for each item, plus the grand total).
- **Low stock report** that lists every item with fewer than 5 units.

## How it works

Everything is stored in memory:

- `inventory` is a list that holds all the items.
- Each item is a dictionary: `{"id": 1101, "name": "Pen", "quantity": 50, "price": 10.0}`
- IDs start at **1101** and go up by one with every item added.
- Each feature lives in its own function (`add_item`, `view_items`, `update_item`, `search_item`, `delete_item`, `total_stock_value`, `low_stock_report`), and a `while True` loop runs the main menu until you choose Exit.

### Input checks

The program doesn't just trust whatever you type:

- Quantity must be a whole number, 0 or more.
- Price must be a number, 0 or more.
- If something is invalid, you get a clear message and nothing is saved.
- Looking up an ID that doesn't exist tells you it wasn't found.

## Requirements

- Python 3 (no extra packages needed)

## How to run

1. Save the code as `inventory.py` (or any name you like).
2. Open a terminal in that folder.
3. Run:

```bash
python inventory.py
```

## Menu

```
--- Inventory Management System ---
1. Add Item
2. View All Items
3. Total Stock Value
4. Delete Item
5. Update Item
6. Low Stock Report
7. Search Item
8. Exit
```

## Sample run

**Adding a normal item**

```
Enter option: 1
Name: Pen
Quantity: 50
Price: 10
Item added.
ID: 1101 | Pen | Qty: 50 | Price: 10
```

**Adding an item with zero stock**

```
Enter option: 1
Name: Eraser
Quantity: 0
Price: 5
Item added.
ID: 1102 | Eraser | Qty: 0 | Price: 5
Low stock alert: Eraser (0)
```

**Invalid input**

```
Enter option: 1
Name: Pencil
Quantity: -5
Invalid quantity. Quantity must be a non-negative whole number. Item not added.

Enter option: 5
Enter ID to update: 1999
Item ID 1999 not found.
```

**Total stock value** (with Pen: 50 x 10 and Notebook: 3 x 40)

```
Pen: 500
Notebook: 120
Total stock value: 620
```

## Test cases covered

| # | Scenario | What it checks |
|---|----------|----------------|
| 1 | Normal input | Adding a regular item works and gets ID 1101 |
| 2 | Boundary input | Quantity 0 is allowed and triggers a low stock alert |
| 3 | Invalid input | Negative quantity is rejected; unknown ID is reported |
| 4 | Different valid scenario | Total stock value, low stock report, and delete all work together |
