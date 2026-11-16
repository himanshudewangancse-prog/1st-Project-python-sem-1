# Inventory Management System


inventory = []          # list to store all items
next_id = 1101          # first item ID will be 1101

def format_money(value):
    if float(value).is_integer():
        return str(int(value))
    return str(value)

def show_item(item):
    # Print one item in neat format
    print(f"ID: {item['id']} | {item['name']} | Qty: {item['quantity']} | Price: {format_money(item['price'])}")

def add_item():
    global next_id

    name = input("Name: ")

    # Quantity must be whole number and 0 or more
    try:
        quantity = int(input("Quantity: "))
    except:
        print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
        return

    if quantity < 0:
        print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
        return

    # Price must be 0 or more
    try:
        price = float(input("Price: "))
    except:
        print("Invalid price. Price must be 0 or more. Item not added.")
        return

    if price < 0:
        print("Invalid price. Price must be 0 or more. Item not added.")
        return

    # Create item as dictionary and add to list
    item = {
        "id": next_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(item)
    print("Item added.")
    show_item(item)

    # Low stock alert if quantity is 0
    if quantity < 5:
        print(f"Low stock alert: {name} ({quantity})")

    next_id = next_id + 1

def view_items():
    if len(inventory) == 0:
        print ("No items in inventory.")
        return

    print("---- All Items ----")
    for item in inventory:
        show_item(item)

def update_item():
    try:
        item_id = int(input("Enter ID to update: "))
    except:
        print("Invalid ID.")
        return

    for item in inventory:
        if item["id"] == item_id:
            new_name = input("New Name (press Enter to keep same): ")
            if new_name != "":
                item["name"] = new_name

            new_qty = input("New Quantity (press Enter to keep same): ")
            if new_qty != "":
                try:
                    quantity = int(new_qty)
                except ValueError:
                    print("Invalid quantity. Quantity must be a non-negative whole number. Item not updated.")
                    return
                if quantity < 0:
                    print("Invalid quantity. Quantity must be a non-negative whole number. Item not updated.")
                    return
                item["quantity"] = quantity

            new_price = input("New Price (press Enter to keep same): ")
            if new_price != "":
                try:
                    price = float(new_price)
                except ValueError:
                    print("Invalid price. Price must be 0 or more. Item not updated.")
                    return
                if price < 0:
                    print("Invalid price. Price must be 0 or more. Item not updated.")
                    return
                item["price"] = price

            print("Item updated.")
            show_item(item)
            return

    print(f"Item ID {item_id} not found.")

def search_item():
    name = input("Enter name to search: ")
    found = False

    for item in inventory:
        if item["name"].lower() == name.lower():
            show_item(item)
            found = True

    if found == False:
        print("Item not found.")

def delete_item():
    try:
        item_id = int(input("Enter ID to delete: "))
    except:
        print("Invalid ID.")
        return

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            print(f"Item {item['name']} deleted. Items left: {len(inventory)}")
            return

    print(f"Item ID {item_id} not found.")

def total_stock_value():
    total = 0
    for item in inventory:
        value = item["quantity"] * item["price"]
        print(f"{item['name']}: {format_money(value)}")
        total = total + value

    print(f"Total stock value: {format_money(total)}")

def low_stock_report():
    print("---- Low Stock Items (Qty < 5) ----")
    found = False
    for item in inventory:
        if item["quantity"] < 5:
            show_item(item)
            found = True

    if found == False:
        print("No low stock items.")

# Main Menu - runs again and again
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. View All Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Total Stock Value")
    print("6. Low Stock Report")
    print("7. Search Item")
    print("8. Exit")

    choice = input("Enter option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        total_stock_value()
    elif choice == "6":
        low_stock_report()
    elif choice == "7":
        search_item()
    elif choice == "8":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid option. Try again.")