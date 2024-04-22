# Gioele Amendola
# 19/04/2024

# 4-1.  Pizzas: 
#       Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
#       and then use a for loop to print the name of each pizza.
#
#       • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
#         For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#       • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#         The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#         such as I really love pizza!
print("# Exercise 4-1:\n")

pizzas_list: list = ['Diavola','Boscaiola','Capricciosa']

for pizza in pizzas_list:
    print(pizza)

print("")

for pizza in pizzas_list:
    print(f"I like {pizza} pizza.")

print("")

print(f"I really like {pizzas_list[0]} for its spicyness.\n",
      f"\r{pizzas_list[1]} is great and fullfilling.\n",
      f"\rEverything is on {pizzas_list[2]}!\n\n",
      "\rI really love pizza!\n")


# 4-2.  Animals: 
#       Think of at least three different animals that have a common characteristic. 
#       Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#
#       • Modify your program to print a statement about each animal, such as A dog would make a great pet.
#       • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
#         such as Any of these animals would make a great pet!
print("# Exercise 4-2:\n")

animals_list: list = ['dog','dolphin','crow']

for animal in animals_list:
    print(animal)

print("")

for animal in animals_list:
    print(f"A {animal} would make a great pet!")

print("")

print("All these pets are really smart!\n")


# 4-3.  Counting to Twenty: 
#       Use a for loop to print the numbers from 1 to 20, inclusive.
print("# Exercise 4-3:\n")

for number in range(1,21):
    print(number)

print("")

# 4-4.  One Million: 
#       Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#       (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
print("# Exercise 4-4:\n")

numbers_list1: list = [number for number in range(1,11)] # One million and one has been replaced by eleven

for number in numbers_list1:
    print(number)

print("")


# 4-5.  Summing a Million: 
#       Make a list of the numbers from one to one million, and then use min() and max() to make sure
#       your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly 
#       Python can add a million numbers.
print("# Exercise 4-5:\n")

numbers_list2: list = [number for number in range(1,10**6+1)]

print(f"somma di una lista da {min(numbers_list2)} a {max(numbers_list2)}: {sum(numbers_list2)}")       

print("")


# 4-6.  Odd Numbers: 
#       Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#       Use a for loop to print each number.
print("# Exercise 4-6:\n")

numbers_list3: list = [number for number in range(1,20,2)]

for number in numbers_list3:
    print(number)

print("")


# 4-7.  Threes: 
#       Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
print("# Exercise 4-7:\n")

numbers_list4: list = [number for number in range(3,31,3)]

for number in numbers_list4:
    print(number)

print("")


# 4-8.  Cubes: 
#       A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#       Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
#       and use a for loop to print out the value of each cube.
print("# Exercise 4-8:\n")

numbers_list5: list = [number**3 for number in range(1,11)]

for number in numbers_list5:
    print(number)

print("")


# 4-9.  Cube Comprehension: 
#       Use a list comprehension to generate a list of the first 10 cubes.

# Already done above ^^ but i'll swap them
print("# Exercise 4-9:\n")

numbers_list6: list = []

for number in range(1,11):
    numbers_list6.append(number**3)

print(f"{numbers_list6}\n")


# 4-10. Slices: 
#       Using one of the programs you wrote in this chapter, add several lines to the end of the program that
#       do the following:
#
#       • Print the message The first three items in the list are:. Then use a slice to print the first three items 
#         from that program’s list.
#       • Print the message Three items from the middle of the list are:. Then use a slice to print three items 
#         from the middle of the list.
#       • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
print("# Exercise 4-10:\n")

print(f"The first three items in the list are: {numbers_list5[:3]}\n",
      f"\rThree items from the middle of the list are: {numbers_list5[len(numbers_list5)//2-1:len(numbers_list5)//2+2]}\n",
      f"\rThe last three items in the list are: {numbers_list5[-3:]}\n")


# 4-11. My Pizzas, Your Pizzas: 
#       Start with your program from Exercise 4-1. Make a copy of the list of pizzas, 
#       and call it friend_pizzas. Then, do the following:
#
#       • Add a new pizza to the original list.
#       • Add a different pizza to the list friend_pizzas.
#       • Prove that you have two separate lists. Print the message My favorite pizzas are:, 
#         and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
#         and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print("# Exercise 4-11:",end="")

friend_pizzas: list = pizzas_list[:]

pizzas_list.append("Quattro formaggi")
friend_pizzas.append("Margherita")

for count in range(2):
    print("\n")
    if count == 0:
        print("My favorite pizzas are:")
        for pizza in pizzas_list:
            print(f"{pizza}",end=" ")
    else:
        print("My friend's favorite pizzas are:")
        for pizza in friend_pizzas:
            print(f"{pizza}",end=" ")
print("\n")


# 4-12. More Loops: 
#       All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#       Choose a version of foods.py, and write two for loops to print each list of foods.

# Cannot be done


# 4-14. PEP 8: 
#       Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. 
#       You won’t use much of it now, but it might be interesting to skim through it.

# Done, Thank you


# 4-15. Code Review: 
#       Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

# Already done


# 5-1.  Conditional Tests: 
#       Write a series of conditional tests. Print a statement
#       describing each test and your prediction for the results of each test. Your code
#       should look something like this:
#
#       car = 'subaru'
#       print("Is car == 'subaru'? I predict True.")
#       print(car == 'subaru')
#       print("\nIs car == 'audi'? I predict False.")
#       print(car == 'audi')
#
#       • Look closely at your results, and make sure you understand why each line
#         evaluates to True or False.
#       • Create at least 10 tests. Have at least 5 tests evaluate to True and another
#         5 tests evaluate to False.
print("# Exercise 5-1:\n")

print("\nTest 1:")

car: str = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nTest 2:")

motorcycle: str = 'suzuki'
print("Is motorcycle == 'suzuki'? I predict True.")
print(motorcycle == 'suzuki')
print("\nIs motorcycle == 'ducati'? I predict False.")
print(motorcycle == 'ducati')

print("\nTest 3:")

tank: str = 'leopard 1'
print("Is tank == 'leopard 1'? I predict True.")
print(tank == 'leopard 1')
print("\nIs tank == 'M60'? I predict False.")
print(tank == 'M60')

print("\nTest 4:")

city: str = 'sydney'
print("Is city == 'sydney'? I predict True.")
print(city == 'sydney')
print("\nIs city == 'rome'? I predict False.")
print(city == 'rome')

print("\nTest 5:")

mountain: str = 'mont blanc'
print("Is mountain == 'mont blanc'? I predict True.")
print(mountain == 'mont blanc')
print("\nIs mountain == 'everest'? I predict False.")
print(mountain == 'everest')

print("")


# 5-2.  More Conditional Tests: 
#       You don’t have to limit the number of tests you create to 10.
#       If you want to try more comparisons, write more tests and add them to conditional_tests.py.
#       Have at least one True and one False result for each of the following:
#
#       • Tests for equality and inequality with strings
#       • Tests using the lower() method
#       • Numerical tests involving equality and inequality, greater than and less
#         than, greater than or equal to, and less than or equal to
#       • Tests using the and keyword and the or keyword
#       • Test whether an item is in a list
#       • Test whether an item is not in a list
print("# Exercise 5-2:\n")

conditional_string1: str = 'Puma'
conditional_string2: str = 'Cheeta'
conditional_string3: str = 'puMA'
conditional_number1: int = 5
conditional_number2: int = 12
conditional_list1: list = [3,6,'Puma',37,'cheeta']

print("Test for equality with 'Puma' and 'puMA':\n",
      f"\r'Puma' == 'puMA': {conditional_string1 == conditional_string3}")

print("\nTest for inequality with 'Puma' and 'Cheeta':\n",
      f"\r'Puma' == 'Cheeta': {conditional_string1 != conditional_string2}")

print("\nTest for equality with 'Puma' and 'puMA' both using lower() method:\n",
      f"\r'Puma.lower()' == 'puMA.lower()': {conditional_string1.lower() == conditional_string3.lower()}")

print("\nTests for equality, inequality, greater than, less than, greater or equal than, less or equal than with '12' and '5':\n",
      f"\r'5' == '12': {conditional_number1 == conditional_number2}\n",
      f"\r'5' != '12': {conditional_number1 != conditional_number2}\n",
      f"\r'5'  > '12': {conditional_number1 > conditional_number2}\n",
      f"\r'5'  < '12': {conditional_number1 < conditional_number2}\n",
      f"\r'5' >= '12': {conditional_number1 >= conditional_number2}\n",
      f"\r'5' <= '12': {conditional_number1 <= conditional_number2}\n")

print("Test using the AND and OR keywords:\n",
      f"\r('5' >= 0 or '12' < 15) and '12' > '5': {((conditional_number1 >= 0) or (conditional_number2 < 15)) and (conditional_number2 > conditional_number1)}\n")

print("Test wheter an item is in a list or not:\n",
      f"\r'Puma' is in '[3,6,Puma,37,cheeta]': {conditional_string1 in conditional_list1}\n",
      f"\r'12' is not in '[3,6,Puma,37,cheeta]': {conditional_number2 not in conditional_list1}\n")

# 5-3.  Alien Colors #1: 
#       Imagine an alien was just shot down in a game. 
#       Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#
#       • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player 
#         just earned 5 points.
#       • Write one version of this program that passes the if test and another that fails. 
#         (The version that fails will have no output.)
print("# Exercise 5-3:\n")

alien_color1: str = 'green'

if alien_color1 == 'green':
    print("+5 points\n")


# 5-4.  Alien Colors #2: 
#       Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#
#       • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#       • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#       • Write one version of this program that runs the if block and another that runs the else block.
print("# Exercise 5-4:\n")

alien_color2: str = 'yellow'

if alien_color2 == 'green':
    print("+5 points\n")
else:
    print("+10 points\n")

# 5-5.  Alien Colors #3: 
#       Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#
#       • If the alien is green, print a message that the player earned 5 points.
#       • If the alien is yellow, print a message that the player earned 10 points.
#       • If the alien is red, print a message that the player earned 15 points.
#       • Write three versions of this program, making sure each message is printed for the appropriate color alien.
print("# Exercise 5-5:\n")

alien_color3: str = 'red'

if alien_color3 == 'green':
    print("+5 points\n")
elif alien_color3 == 'yellow':
    print("+10 points\n")
else:
    print("+15 points\n")

# 5-6.  Stages of Life: 
#       Write an if-elif-else chain that determines a person’s stage of life.
#       Set a value for the variable age, and then:
#
#       • If the person is less than 2 years old, print a message that the person is a baby.
#       • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#       • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#       • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#       • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#       • If the person is age 65 or older, print a message that the person is an elder.
print("# Exercise 5-6:\n")

age: int = 23

if age < 2:
    print("baby\n")
elif age < 4:
    print("toddler\n")
elif age < 13:
    print("kid\n")
elif age < 20:
    print("teenager\n")
elif age < 65:
    print("adult\n")
else:
    print("elder\n")


# 5-7.  Favorite Fruit: 
#       Make a list of your favorite fruits, and then write a series of independent if statements 
#       that check for certain fruits in your list.
#
#       • Make a list of your three favorite fruits and call it favorite_fruits.
#       • Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#         If the fruit is in your list, the if block should print a statement, such as You really like Apples!
print("# Exercise 5-7:\n")

favorite_fruits: list = ['strawberry','mango','pineapple']

if 'apple' in favorite_fruits:
    print("You really like Apples!\n")
if 'kiwi' in favorite_fruits:
    print("You really like Kiwis!\n")
if 'strawberry' in favorite_fruits:
    print("You really like Strawberries!\n")
if 'pineapple' in favorite_fruits:
    print("You really like Pineapples!\n")
if 'blueberry' in favorite_fruits:
    print("You really like Blueberries!\n")

# 5-8.  Hello Admin: 
#       Make a list of five or more usernames, including the name 'admin'. 
#       Imagine you are writing code that will print a greeting to each user after they log in to a website. 
#       Loop through the list, and print a greeting to each user.
#
#       • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#       • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
print("# Exercise 5-8:\n")

users_list1: list = ['admin','Asterix','Obelix','lily82','totti10']

for user in users_list1:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?\n")
    else:
        print(f"Hello {user}, thank you for loggin in again.\n")

# 5-9.  No Users: 
#       Add an if test to hello_admin.py to make sure the list of users is not empty.
#
#       • If the list is empty, print the message We need to find some users!
#       • Remove all of the usernames from your list, and make sure the correct message is printed.
print("# Exercise 5-9:\n")

users_list2: list = []

if not users_list2:
    print("We need to find some users!\n")

# 5-10. Checking Usernames: 
#       Do the following to create a program that simulates how websites ensure that everyone 
#       has a unique username.
#
#       • Make a list of five or more usernames called current_users.
#       • Make another list of five usernames called new_users. Make sure one or two of the new usernames are 
#         also in the current_users list.
#       • Loop through the new_users list to see if each new username has already been used. If it has, 
#         print a message that the person will need to enter a new username. If a username has not been used, 
#         print a message saying that the username is available.
#       • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
#         (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
print("# Exercise 5-10:\n")

current_users: list = users_list1[1:]
current_users.append('pringlez')
new_users: list = ['Asterix','prince82','john','Pringlez','Cleopatra']
check_users: list = [current_user.lower() for current_user in current_users]


for new_user in new_users:
    if new_user.lower() in check_users:
        print(f"{new_user} is already in use.\n")
    else:
        print(f"{new_user} is available.\n")


# 5-11. Ordinal Numbers: 
#       Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, 
#       except 1, 2, and 3.
#
#       • Store the numbers 1 through 9 in a list.
#       • Loop through the list.
#       • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#         Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
print("# Exercise 5-11:\n")

numbers_list7: list = [x for x in range(1,10)]

for number in numbers_list7:
    if number == 1:
        print(f"{number}st",end=" ")
    elif number == 2:
        print(f"{number}nd",end=" ")
    elif number == 3:
        print(f"{number}rd",end=" ")
    else:
        print(f"{number}th",end=" ")

print("\n")