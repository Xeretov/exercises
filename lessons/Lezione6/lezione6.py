# Gioele Amendola
# 23/05/2025

# 9-1. Restaurant:
# Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:

    def __init__(self, name: str, type: str) -> None:
        self.restaurant_name: str = name
        self.cuisine_type: str = type
    
    def describe_restaurant(self) -> None:
        print(f"The restaurant {self.restaurant_name} cooks only {self.cuisine_type.lower()} cuisine.",end="\n\n")
    
    def open_restaurant(self) -> None:
        print(f"{self.restaurant_name} is now Open!",end="\n\n")

restaurant1: Restaurant = Restaurant("Pizzeria Romana", "italian")
print(restaurant1.restaurant_name,restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# 9-2. Three Restaurants:
# Start with your class from Exercise 9-1.
# Create three different instances from the class, and call describe_restaurant() for each instance.

restaurant2: Restaurant = Restaurant("Karma","indian")
restaurant3: Restaurant = Restaurant("Mizu","japanese")
restaurant4: Restaurant = Restaurant("Oro","french")
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

# 9-3. Users:
# Make a class called User.
# Create two attributes called first_name and last_name, and then create several other attributes
# that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:

    def __init__(self, fname: str, lname: str, email:str = None, nick:str = None) -> None:
        self.first_name: str = fname
        self.last_name: str = lname
        self.email: str = email
        self.nickname: str = nick
    
    def describe_user(self) -> None:
        print(f"The user {self.nickname if self.nickname else self.first_name} data:",
              f"First Name: {self.first_name}",
              f"Last Name: {self.last_name}",
              f"Email: {self.email}" if self.email else "",sep="\n",end="\n\n")

    def greet_user(self) -> None:
        print(f"Welcome {self.nickname if self.nickname else self.first_name}!",end="\n\n")

user1: User = User("Giacomo","Giacomo","giacomo@giacomo.com","GiacomoGiacomo")
user2: User = User("Seth","Evergreen","seth_evergreen1978@gmail.com")
user3: User = User("Molly","Smith",nick="cute_drug")

user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.describe_user()
user2.describe_user()
user3.describe_user()

# 9-4. Number Served:
# Start with your program from Exercise 9-1.
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served,
# and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant:
    
    def __init__(self, name: str, type: str, served: int = 0) -> None:
        self.restaurant_name: str = name
        self.cuisine_type: str = type
        self.number_served: int = served if served > 0 else 0
    
    def set_number_served(self, served: int) -> None:
        self.number_served = served if served > 0 else 0
    
    def increment_number_served(self, served: int = 1) -> None:
        self.number_served += served

restaurant5: Restaurant = Restaurant("La Manica","italian")
print(restaurant5.number_served)
restaurant5.number_served = 10
print(restaurant5.number_served)
restaurant5.set_number_served(3)
print(restaurant5.number_served)
for _ in range(5):
    restaurant5.increment_number_served(3)
print(restaurant5.number_served,end="\n\n")


# 9-5. Login Attempts:
# Add an attribute called login_attempts to your User class from Exercise 9-3.
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.

class User:

    def __init__(self, fname: str, lname: str, email:str = None, nick:str = None) -> None:
        self.first_name: str = fname
        self.last_name: str = lname
        self.email: str = email
        self.nickname: str = nick
        self.login_attempts: int = 0
    
    def increment_login_attempts(self) -> None:
        self.login_attempts += 1
    
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

user4: User = User("Mario","Rossi")
for _ in range(4):
    user4.increment_login_attempts()
print(user4.login_attempts)
user4.reset_login_attempts()
print(user4.login_attempts,end="\n\n")
        

# 9-6. Ice Cream Stand:
# An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4.
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

class IceCreamStand(Restaurant):
    def __init__(self, name: str, type: str, flavors: list, served: int = 0) -> None:
        super().__init__(name, type, served)
        self.flavors: list = flavors
    
    def get_flavors(self) -> None:
        print(*self.flavors,sep=" | ", end="\n\n")

icecream1: IceCreamStand = IceCreamStand("Brividi","gelato",["strawberry","mango","passion fruit"])
icecream1.get_flavors()

# 9-7. Admin:
# An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5.
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.

class Admin(User):
    
    def __init__(self, fname: str, lname: str, privileges = None, email: str = None, nick: str = None) -> None:
        super().__init__(fname, lname, email, nick)
        if isinstance(privileges, Privileges):
            self.privileges: Privileges = privileges

# 9-8. Privileges:
# Write a separate Privileges class.
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    
    def __init__(self, privileges: list[str]) -> None:
        self.privileges: list[str] = privileges

    def show_privileges(self) -> None:
        print(*self.privileges,sep=" | ", end="\n\n")

administrator: Admin = Admin("Angelo","Carini",Privileges(["can ban user","can delete post"]))
administrator.privileges.show_privileges()

# 9-9. Battery Upgrade:
# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 65 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once,
# and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

# Cannot do

# 9-10. Imported Restaurant:
# Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant.
# Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

# It works, trust me!

# 9-11. Imported Admin:
# Start with your work from Exercise 9-8.
# Store the classes User, Privileges, and Admin in one module.
# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

# It works, trust me!

# 9-12. Multiple Modules:
# Store the User class in one module, and store the Privileges and Admin classes in a separate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

# It works, trust me!

# 9-13. Dice:
# Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    
    def __init__(self, sides: int = 6) -> None:
        self.sides: int = sides if sides > 0 else 1
    
    def roll_die(self) -> None:
        print(randint(1,self.sides),end=" ")
    
dice1: Die = Die()
dice2: Die = Die(10)
dice3: Die = Die(20)

print("6 sided die:")
for _ in range(10):
    dice1.roll_die()
print("\n10 sided die:")
for _ in range(10):
    dice2.roll_die()
print("\n20 sided die:")
for _ in range(10):
    dice3.roll_die()
print(end="\n\n")


# 9-14. Lottery:
# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and
# print a message saying that any ticket matching these 4 numbers or letters wins a prize.

possible_winning: list = [10,4,6,28,49,14,66,48,2,81,'f','h','l','p','s']
winning_numbers: list = [possible_winning[randint(0,len(possible_winning)-1)] for _ in range(4)]
print(f"Winning numbers:\n",*winning_numbers)

# 9-15. Lottery Analysis:
# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.

my_ticket: set = set("-inf")
i: int = 0
while not my_ticket.issubset(set(winning_numbers)):
    my_ticket = set([possible_winning[randint(0,len(possible_winning)-1)] for _ in range(4)])
    i += 1
print(f"\nnumber of tries: {i}",end="\n\n")
