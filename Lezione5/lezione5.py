# Gioele Amendola
# 07/05/2024

# 1. Create a Playlist:
# Write a function called create_playlist() that accepts a playlist name
# and a variable number of song titles.
# The function should return a dictionary with the playlist name and a set of songs.
# Call the function with different numbers of songs to demonstrate flexibility.

# Example:
# create_playlist("Road Trip", {"Song 1", "Song 2"})

# Write a function called add_like() that accepts a dictionary,
# the name of a playlist, and a boolean value indicating whether it is liked (True or False).
# This function should return an updated dictionary.

# Example:
# add_like(dictionary, “Road Trip”, liked=True)

def create_playlist(p_name: str, *s_name: str) -> dict:
    songs: set = set(s_name)
    playlist: dict = {p_name:songs}
    return playlist

def add_like(playlist: dict, p_name: str, liked: bool) -> dict:
    playlist = {p_name:(playlist[p_name],liked)}
    return playlist

print(add_like(create_playlist("White Album","Jurassic Park","Cure","Balboa"),"White Album",True))

# 2. Book Collection:
# Write a function called add_book() that accepts 
# an author's name and a variable number of book titles authored by them.
# This function should return a dictionary where the author's name is the key
# and the value is a list of their books.
# Demonstrate this function by adding books for different authors.

# Example:
# add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

# Write a function called delete_book() that accepts a dictionary
# and the name of the author from whom to remove all details.
# This function should return an updated dictionary.

# Example:
# delete_book(dictionary, “Mark Twain”)

def add_book(author: str, *b_titles: str) -> dict:
    titles = list(b_titles)
    books: dict = {author: titles}
    return books

def delete_book(books: dict, author: str) -> dict:
    del books[author]
    return

test: dict = add_book("Mark Twain","The Adventures of Tom Sawyer","Life on the Mississippi")
print(test)
delete_book(test,"Mark Twain")
print(test,end="\n\n")

# 3. Personal Info:
# Write a build_profile() function that accepts the name,
# surname, occupation, location, and age of a person.
# Make occupation, location, and age optional parameters.
# Use this function to create profiles for different people,
# demonstrating how it handles these optional parameters.

# Example:
# build_profile("John", "Doe", occupation="Developer", location="USA", age=30)

def build_profile(first_name: str, last_name: str, occupation: str = None, location: str = None, age: int = None):
    print(f"{first_name+' '+last_name}",end="")
    if age:
        print(f", {age}")
    else:
        print()
    if location:
        print(f"{location}",end=" - " if occupation else "\n")
    if occupation:
        print(f"{occupation}")
    print()
    return

build_profile("John","Doe",occupation="Developer",location="USA",age=30)
build_profile("Mia","Dawson",age=25)
build_profile("Larry","Mark",occupation="Janitor")
build_profile("Patrick","Fentanyl",location="Italy")
build_profile("Giorgio","Carro",location="Peru",age=28,occupation="Policeman")


# 4. Event Organizer:
# Write a function called plan_event() that accepts an event name,
# a list of participants, and an hour.
# The function should return a dictionary that includes
# the event name and a list of the participants.
# Call this function with varying numbers of participants to plan different events.

# Example:
# plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

# Write a function called modify_event() that accepts a dictionary,
# an event name, and new details to modify an already planned event.

# Example:
# modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)

def plan_event(name: str, people: list, hour: str) -> dict:
    event: dict = {name: people}
    return event

def modify_event(event: dict, name: str, people: list = None, hour: str = None) -> dict:
    if people:
        event = {name: people}
    if hour:
        event = {name: (event[name], hour)}
    return event

print(modify_event(plan_event("cooking",["Mary","Leonidas","Mark"],"4pm"),"cooking",["Perry","Marty","Leonidas"],"4pm"))

# 5. Shopping List:
# Write a function called create_shopping_list() that accepts
# a store name and any number of items as arguments.
# It should return a dictionary with the store name and a set of items to buy there.
# Test the function with different stores and item lists.

# Example:
# create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

# Write a function called print_shopping_list() that
# accepts a dictionary and a store name,
# then prints each item from that store's shopping list.

# Example:
# print_shopping_list(dictionary, "Grocery Store")

def create_shopping_list(store_name: str, *items) -> dict:
    item_set: set = set(items)
    stores: dict = {store_name: item_set}
    return stores

def print_shopping_list(stores: dict, store_name: str):
    print(f"{store_name}:")
    for x in stores[store_name]:
        print(f"{x}")
    return

test = create_shopping_list("Grocery Store", "Milk", "Eggs", "Bread")
print(test)
print_shopping_list(test, "Grocery Store")
