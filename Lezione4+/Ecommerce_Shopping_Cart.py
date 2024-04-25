# Gioele Amendola
# 23/04/2024

# Create a function that defines a product with a name, price, and quantity.
# Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
# The function should calculate the cart total and apply any discounts or taxes.
# Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.


# Main Menu for interactive ecommerce shopping
def shopping_cart(products_dictionary: dict,discount: int = None, taxes: int = None):
    print("\nWelcome to the CYB3R.SH0P!\n")
    cart_list: dict = {}
    choose: int = 0
    check: bool = False
    while True:
        print("\nPlease type one of these:\n1. Add item\n2. View item\n3. Remove Item\n5. Check Out")

        # Select the function to go to based on input number
        choose = int(input("\n> "))
        if choose == 1:
            products_dictionary,cart_list = add_to_cart(products_dictionary,cart_list)
        elif choose == 2:
            product_information(products_dictionary)
        elif choose == 3:
            products_dictionary,cart_list = remove_from_cart(products_dictionary,cart_list)
        elif choose == 5:
            check = check_out(products_dictionary,cart_list,discount,taxes)
            if check:
                return


# Looks through the products given, the names, prices and quantities
def product_information(products_dictionary: dict):
    print("\nHere are all the informations about available products: (Press Enter to continue)\n")
    for product_key,product_value in products_dictionary.items():
        print(f"> {product_key} costs {product_value[0]:.2f}€ and has {product_value[1]} remaining in stock.")
    input("\n")
    return 

# Menu to add a product to cart given a name and its quantity
def add_to_cart(products_dictionary: dict, cart_list: dict) -> dict:
    while True:
        print("***REMEMBER: Insert -1 to go back***")
        print("Insert name to add to the list:\n")
        choose_name: str = ""
        choose_quantity: int = 0

        # Shows what products are there
        for i, product_name in zip(range(1,len(products_dictionary.keys())+1), products_dictionary.keys()):
            print(f"{i}. {product_name}")

        # Control for name inserted if exist and is available (-1 goes back to Main Menu) in products given
        while choose_name not in products_dictionary.keys():
            print("\nChoose the product by inserting its name:\n")
            choose_name = input("> ").capitalize()
            if choose_name == '-1':
                return products_dictionary,cart_list
            elif choose_name in products_dictionary.keys():
                if products_dictionary[choose_name][1] == 0:
                    print("\nThis item is unavailable.")
                    choose_name = ""

        print(f"\n\nYou chose: {choose_name}, there are {products_dictionary[choose_name][1]} left in stock.")
        
        # Control for quantity chosen (-1 goes to Main Menu)
        while 0 >= choose_quantity or choose_quantity > products_dictionary[choose_name][1]:
            print("\nChoose how many do you want to put in the cart:\n")
            choose_quantity = int(input("> "))
            if choose_quantity == -1:
                return products_dictionary,cart_list
            
        # Adds to cart and decrease of quantity in the products given
        if choose_name in cart_list:
            cart_list[choose_name] += choose_quantity
        else:
            cart_list[choose_name] = choose_quantity
        products_dictionary[choose_name][1] -= choose_quantity

# Menu for removing products from the cart given name and its quantity
def remove_from_cart(products_dictionary:dict,cart_list: dict) -> dict:
    while True:
        print("***REMEMBER: Insert -1 to go back***")
        print("Insert name to remove from the cart:\n")
        choose_name: str = ""
        choose_quantity: int = 0

        # Shows products
        for i, product_name in zip(range(1,len(cart_list.keys())+1), cart_list.keys()):
            print(f"{i}. {product_name}")

        # Control for name in cart
        while choose_name not in cart_list.keys():
            print("\nChoose the product by inserting its name:\n")
            choose_name = input("> ").capitalize()
            if choose_name == '-1':
                return products_dictionary,cart_list
        print(f"\n\nYou chose: {choose_name}, there are {cart_list[choose_name]} in the cart.")

        # Control for quantity in cart
        while choose_quantity <= 0 or choose_quantity > cart_list[choose_name]:
            print("\nChoose how many do you want to take out of the cart:\n")
            choose_quantity = int(input("> "))
            if choose_quantity == -1:
                return products_dictionary,cart_list
            
        # Decrease quantity from cart, if 0 delete record, and add to products given
        if choose_quantity == cart_list[choose_name]:
            del cart_list[choose_name]
        else:
            cart_list[choose_name] -= choose_quantity
        products_dictionary[choose_name][1] += choose_quantity    

# Check for price of cart and check out
def check_out(products_dictionary:dict, cart_list: dict, discount: int = 0, taxes: int = 0) -> bool:
    sum: float = 0
    check: str = ''
    print("\nHere is the content of the cart and its cost:\n")
    
    # Shows price for every product in cart
    for i,product in zip(range(1,len(cart_list.keys())+1),cart_list.keys()):
        sum += cart_list[product] * products_dictionary[product][0]
        print(f"{i}. {cart_list[product]} {product} price:\t {cart_list[product]*products_dictionary[product][0]:.2f}€")
    
    # Shows total price
    print(f"\nBase price:\t\t {sum:.2f}€")

    # Calculation of discount and taxes
    print(f"With {taxes}% Taxes:\t\t {(sum+((sum*taxes)/100)):.2f} ")
    print(f"With {discount}% Discount:\t {((sum+((sum*taxes)/100))-((sum*discount)/100)):.2f}")

    # Control for checkout
    while check != 'Y' or check != 'n':
        print("\nDo you want to pay? (Y/n)")
        check = input("\n> ")
        if check == 'Y':
            return True
        elif check == 'n':
            return False



products_dictionary: dict = {"Pizza":[5.25,10],"Pasta":[3.00,25],"Vegetable":[2.00,7],"Sweet":[10.60,3],"Wine":[25.99,1]}
shopping_cart(products_dictionary,25,10)