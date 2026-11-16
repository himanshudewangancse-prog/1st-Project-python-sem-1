# Project Summary: Inventory Management System

**Project Statement:** 14
**Language:** Python 3
**Course:** B.Tech Computer Science and Engineering, Rungta International Skills University

## What this project is

A console-based inventory manager written in one Python file. It uses a **list** to hold all items, a **dictionary** for each item (`id`, `name`, `quantity`, `price`), and a **separate function** for every feature. A menu loop keeps the program running until the user chooses Exit.

The first item ID is **1101**, and every new item gets the next number.

## Menu

```
1. Add Item
2. View All Items
3. Update Item
4. Delete Item
5. Total Stock Value
6. Low Stock Report
7. Search Item
8. Exit
```

## Test results

I ran all four test cases from the problem statement, in order, in the same run of the program. Every one gave the expected output.

### Test Case 1: Normal Input

**Input:** Option 1 (Add), Name: Pen, Quantity: 50, Price: 10

**Output:**
```
Item added.
ID: 1101 | Pen | Qty: 50 | Price: 10
```

**Result:** Pass. The item was added with the first ID, and no low stock alert appeared because 50 is not below 5.

### Test Case 2: Boundary / Minimum Input

**Input:** Option 1 (Add), Name: Eraser, Quantity: 0, Price: 5

**Output:**
```
Item added.
ID: 1102 | Eraser | Qty: 0 | Price: 5
Low stock alert: Eraser (0)
```

**Result:** Pass. A quantity of 0 is accepted as the minimum, and the low stock alert fires.

### Test Case 3: Invalid Input

**Input:**
- (a) Option 1 (Add), Name: Pencil, Quantity: -5
- (b) Option 3 (Update), ID: 1999

**Output:**
```
Invalid quantity. Quantity must be a non-negative whole number. Item not added.
Item ID 1999 not found.
```

**Result:** Pass. The negative quantity is rejected and nothing is saved. An ID that doesn't exist is reported clearly.

### Test Case 4: Different Valid Scenario

**Starting inventory:** ID 1101 Pen (50 x 10) and ID 1102 Notebook (3 x 40)

**Input and output:**

| Step | Input | Output |
|------|-------|--------|
| (a) | Option 5 (Total Stock Value) | `Pen: 500`, `Notebook: 120`, `Total stock value: 620` |
| (b) | Option 6 (Low Stock Report) | `ID: 1102 \| Notebook \| Qty: 3 \| Price: 40` |
| (c) | Option 4 (Delete), ID: 1101 | `Item Pen deleted. Items left: 1` |

**Result:** Pass. The total is correct (500 + 120 = 620), only the Notebook shows as low stock, and deleting the Pen leaves one item.

## Summary of results

| Test Case | Scenario | Status |
|-----------|----------|--------|
| 1 | Normal input | Pass |
| 2 | Boundary / minimum input | Pass |
| 3 | Invalid input | Pass |
| 4 | Different valid scenario | Pass |

## Requirements checklist

- [x] Written in Python 3, one `.py` file, runs from the console
- [x] Each item stored as a dictionary
- [x] One function each for add, view, update, search, and delete
- [x] Total stock value calculated, and items with quantity below 5 listed
- [x] Quantity and price validated, and records shown in a neat format

## What I learned

- How to combine lists and dictionaries to store structured records.
- Why splitting code into small functions makes it easier to read and test.
- How `try/except` and simple `if` checks stop bad input from breaking the program.
- Why you should `return` right after removing an item from a list inside a loop.

## Possible improvements

- Save the inventory to a file (JSON or CSV) so data survives after exit.
- Search by part of a name, not only the full name.
- Make updates all-or-nothing, so an error halfway doesn't leave an item partly changed.
