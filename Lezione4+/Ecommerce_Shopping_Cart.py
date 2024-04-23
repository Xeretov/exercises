# Gioele Amendola
# 23/04/2024

# Create a function that defines a product with a name, price, and quantity.
# Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
# The function should calculate the cart total and apply any discounts or taxes.
# Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

def shopping_cart(products_dictionary: dict):
    choose: int = 0
    while True:
        print("\nPlease type one of these:\n1. Add item\n2. Remove item\n3. View item\n4. Check price\n5. Check Out")
        choose = int(input("\n\tInsert number to go on: "))
        if choose == 1:
            add_to_cart()


def product_information(products_dictionary: dict, selected: int):
    return 

def add_to_cart(products_dictionary: dict, cart_list: list) -> list:
    return cart_list

def remove_from_cart(cart_list: list) -> list:
    return cart_list

def check_price(cart_list: list):
    return

def checkOut(cart_list: list):
    return