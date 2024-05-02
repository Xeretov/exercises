# Gioele Amendola
# 27/04/2024

# Create a function that defines an item with a code, name, quantity, and price.
# Create a database or dictionary to store the items in inventory.
# Implement functions to add, remove, search, and update items in the inventory.
# Use for loops and conditional statements to manage the various inventory operations.

# Main menu for the management system
def inventory(inventory_database: dict = {}):

    print("\nWelcome to the Inventory Management System!\n")

    choose: int = -1

    while True:
        print("\nPlease type one of these:\n1. Add item\n2. Remove item\n3. Search Item\n4. Update Item\n0. Exit")
        # Select the function to go to based on input number
        try:
            choose = int(input("\n> "))
        except:
            print("Input Not Valid. Retry.")

        if choose == 1:
            add_item(inventory_database)
            inventory_database = dict(sorted(inventory_database.items()))
        elif choose == 2:
            remove_item(inventory_database)
            inventory_database = dict(sorted(inventory_database.items()))
        elif choose == 3:
            view_item(inventory_database)
        elif choose == 4:
            update_item(inventory_database)
            inventory_database = dict(sorted(inventory_database.items()))
        elif choose == 0:
            return

# Add item
# Paramaters: inventory_database
# Returns: inventory_database        
def add_item(inventory_database: dict) -> dict:

    while True:

        item_name: str = ""
        item_code: int = 0
        item_quantity: int = 0
        item_price: float = 0
        check: str = True

        # Check for item in database
        while check:
            print("\nAdd item to the database:\n")

            item_name = input("Insert Name > ").capitalize()
            if item_name in inventory_database.keys():
                print("Item alreay in database\n")
            elif item_name == '0':
                print("Item cannot be called 0")
            else:
                print(f"\nItem name: {item_name}")

                while check:
                    check = input(f"Is this correct? (Y/n) ")
                    if check == 'Y':
                        check = False
                    elif check == 'n':
                        break

        # Creation of code, quanity and price
        item_code = hash(item_name)
        check_retry: str = True
        check: str = True
        print()
        while check_retry:

            check = True
            while check:
                try:
                    item_price = float(input("Insert Price > "))
                except:
                    print("Invalid price Input. Retry")
                else:
                    check = False

            check = True
            while check:
                try:
                    item_quantity = int(input("Insert Quantity > "))
                except:
                    print("Invalid quantity Input. Retry")
                else:
                    check = False

            print(f"\n\nName: {item_name}\nPrice: {item_price:.2f}€\nQuantity: {item_quantity}\n")

            while check_retry:
                check_retry = input(f"Is this correct? (Y/n) ")
                if check_retry == 'Y':
                    check_retry = False
                elif check_retry == 'n':
                    break

        # Adds item to database
        inventory_database[item_name] = {'price':item_price,'quantity':item_quantity,'code':item_code}

        check = True
        while check:
            check = input("\nDo you want to add another item? (Y/n) ")
            if check == 'Y':
                break
            elif check == 'n':
                return inventory_database

# Remove item
# Parameters: inventory_database
# Returns: inventory_database        
def remove_item(inventory_database: dict) -> dict:

    while True:

        # Check if in database
        check: str = True
        while check:
            print("\nRemove item from database:\n")
            item_name = input("Insert Name > ").capitalize()

            if item_name in inventory_database.keys():
                print(f"\nItem name: {item_name}")

                while check:
                    check = input("\nAre you sure you want to remove it? (Y/n) ")
                    if check == 'Y':
                        check = False
                    elif check == 'n':
                        break
            else:
                print("Item not in database\n")
        
        # Remove item from database
        del inventory_database[item_name]

        check = True
        while check:
            check = input("\nDo you want to remove another item? (Y/n) ")
            if check == 'Y':
                break
            elif check == 'n':
                return inventory_database
            
# View item
# Parameters: inventory_database        
def view_item(inventory_database: dict):

    while True:

        # Menu for the two options
        print("\nOptions:\n1. View All Inventory\n2. Search for Item\n0. Return")
        try:
            choose: int = int(input("\n> "))
        except:
            print("Input Not Valid. Retry.")
        else:
            # Print every item in the database
            if choose == 1:
                print(f"{'Name':<15}\t\t {'Price':<10} {'Quantity':<10}\t {'...':<5}\t {'code':<30}")
                for item in inventory_database.items():
                    print(f"{item[0]:<15}\t\t {item[1]['price']:<10.2f} {item[1]['quantity']:<10}\t {'...':<5}\t {item[1]['code']:<30}")
                input("\n\nPress Enter to continue...\n")

            # Searches for singular item in the database    
            elif choose == 2:
                check: bool = True
                while check:
                    print("\nView item from database:\n")
                    item_name: str = input("Insert Name > ").capitalize()
                    if item_name in inventory_database.keys():
                        print(f"{item_name}: {inventory_database[item_name]['price']:.2f}€ {inventory_database[item_name]['quantity']}# {'...':<5}\t {inventory_database[item_name]['code']:<30}")
                    else:
                        print("No item found by that name.")
                        
                    while check:
                        check = input("\nDo you want to search another item? (Y/n) ")
                        if check == 'Y':
                            break
                        elif check == 'n':
                            check = False
                        
            elif choose == 0:
                return

# Update item
# Parameters: inventory_database
# Returns: inventory_database            
def update_item(inventory_database: dict) -> dict:

    while True:
        # Search for item in database
        print("Update Database:  **Insert 0 to exit**\n")
        item_name: str = input("Insert Name > ").capitalize()
        if item_name in inventory_database.keys():
            # Choose what to modify of the item
            try:
                choose: int = int(input("\nWhat do you want to modify?\n1. Name\n2. Quantity\n3. Price\n0. Exit\n\n> "))
            except:
                print("Invalid input. Retry")
            else:

                if choose == 0:
                    return inventory_database
                
                elif choose == 1:
                    item_new_name: str = input("Insert new Name > ").capitalize()
                    item_code: int = hash(item_new_name)
                    inventory_database[item_new_name] = inventory_database.pop(item_name)
                    inventory_database[item_new_name]['code'] = item_code

                elif choose == 2:
                    try:
                        item_quantity: int = int(input("Insert quantity > "))
                    except:
                        print("Invalid quantity Input.")
                    else:
                        inventory_database[item_name]['quantity'] = item_quantity

                elif choose == 3:
                    try:
                        item_price: float = float(input("Insert price > "))
                    except:
                        print("Invalid price Input.")
                    else:
                        inventory_database[item_name]['price'] = item_price
                        
        elif item_name == '0':
            return inventory_database
        else:
            print("\nItem not found in database")


# Parameter must adhere to this template:
# {name:{"price":price,"quantity":quantity,"code":code}}
# code is hash(name)

# Example Test:
inventory()