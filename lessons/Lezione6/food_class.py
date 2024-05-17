'''
This module contains the food class and menu class

Returns:
    Food: Class describing a food item
    Menu: Class describing a menu

# Gioele Amendola
# 13/05/2024

# Create a Class that represents a Food
# name, price, description

# Create a Class that represents a Menu
# menu

# Define methods add_food() and remove_food() for menu
# Define methods print_prices() and get_average_price() for menu
'''

class Food:

    def __init__(self, name: str, price: float, description: str) -> None:
        self.name: str = name
        self.price: float = price
        self.description: str = description

class Menu:

    def __init__(self, food_list: list[Food] = []) -> None:
        self.food_list: list[Food] = food_list

    def add_food(self, food: Food) -> None:
        self.food_list.append(food)

    def remove_food(self, food: Food) -> None:
        if food in self.food_list:
            del self.food_list[self.food_list.index(food)]
        else:
            raise Exception("There is no such food in the menu")

    def print_prices(self) -> None:
        print(f"\n{'Food':^20}{'Price':^10}\n")
        for food in self.food_list:
            price = str(f"{food.price:.2f}")+"€"
            print(f"{food.name:^20}{price:^10}")

    def get_average_price(self) -> float:
        return sum(food.price for food in self.food_list) / len(self.food_list)


food1: Food = Food("Carbonara", 10, "Bona")
food2: Food = Food("Matriciana", 10, "Bona")
food3: Food = Food("Tiramisù", 12.5, "Gnam")
food4: Food = Food("Lasagna", 15.99, "Pesante")
food5: Food = Food("Frittata", 5, "Meh")

food_list: list[Food] = [food1,food2,food3]

menu1: Menu = Menu(food_list)

menu1.add_food(food4)
menu1.add_food(food5)

menu1.remove_food(food2)

menu1.print_prices()

print(f"\nAverage Price: {menu1.get_average_price():.2f}€")