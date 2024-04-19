# Gioele Amendola
# 17/04/2024

# 2-3.  Personal Message: Use a variable to represent a person’s name, and print a message to that person.
#       Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
print('# Exercise 2-3:\n')

name: str = 'Marco'
message1: str = f"Hello {name}, would you like to learn some Python today?\n"
print(message1)


# 2-4.  Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase,
#       uppercase, and title case.
print('# Exercise 2-4:\n')

print(name.lower()+'\n'+name.upper()+'\n'+name.title()+'\n')


# 2-5.  Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author.
#       Your output should look something like the following, including the quotation marks: Albert Einstein once said,
#       “A person who never made a mistake never tried anything new.”
print('# Exercise 2-5:\n')

print("Oscar Wilde once said, \"No good deed goes unpunished.\"\n")


# 2-6.  Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called 
#       famous_person. Then compose your message and represent it with a new variable called message. Print your message.
print('# Exercise 2-6:\n')

famous_person: str = "Oscar Wilde"
message2: str = f"{famous_person} once said, \"No good deed goes unpunished.\"\n"

print(message2)


# 2-8.  File Extensions: Python has a removesuffix() method that works exactly like removeprefix().
#       Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix()
#       method to display the filename without the file extension, like some file browsers do.
print('# Exercise 2-8:\n')

filename: str = 'python_notes.txt'
print(filename.removesuffix('.txt')+"\n")


# 3-1.  Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing
#       each element in the list, one at a time.
print('# Exercise 3-1:\n')

names: list = ["Gianfranco","Totti","Ludovico","Marie Curie"]

for i in names:
    print(i)

print("")


# 3-2.  Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
#       print a message to them. The text of each message should be the same, but each message should be personalized with
#       the person’s name.
print('# Exercise 3-2:\n')

for i in names:
    print(f"Hey {i}, hope you are well!")

print("")


# 3-3.  Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list
#       that stores several examples. Use your list to print a series of statements about these items, 
#       such as “I would like to own a Honda motorcycle.”
print('# Exercise 3-3:\n')

veichle_list: list = ['train','airplane','motorcycle']

for i in veichle_list:
    print(f'I would like to own a {i}')

print("")


# 3-4.  Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
#       Make a list that includes at least three people you’d like to invite to dinner.
#       Then use your list to print a message to each person, inviting them to dinner.
print('# Exercise 3-4:\n')

guest_list: list = ['Charlie Chaplin','Leonardo da Vinci','Freddie Mercury']

for i in guest_list:
    print(f"{i} you are hereby invited to the dinner of the dead")

print("")


# 3-5.  Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set
#       of invitations. You’ll have to think of someone else to invite.
#
#       • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of  
#         the guest who can’t make it.
#       • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#       • Print a second set of invitation messages, one for each person who is still in your list.
print('# Exercise 3-5:\n')

print(f"It appears that {guest_list[0]} cannot make it.")

guest_list[0] = 'Cleopatra'

for i in guest_list:
    print(f"Since one of our guest isn't able to come anymore, you {i} are hereby invited to the dinner of the dead")

print("")


# 3-6.  More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite
#       to dinner.
#
#       • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that
#         you found a bigger table.
#       • Use insert() to add one new guest to the beginning of your list.
#       • Use insert() to add one new guest to the middle of your list.
#       • Use append() to add one new guest to the end of your list.
#       • Print a new set of invitation messages, one for each person in your list.
print('# Exercise 3-6:\n')

print(f"Good news everyone! I found a bigger table so that more guests can come!")

guest_list.insert(0,'Alan Turing')
guest_list.insert(len(guest_list)//2, 'Marilyn Monroe')
guest_list.append('Giovanna D\'Arco')

for i in guest_list:
    print(f"Sorry for the spam but, {i}, you are hereby invited to the dinner of the dead")

print("")


# 3-7.  Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
#       and now you have space for only two guests.
#
#       • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only
#         two people for dinner.
#       • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a 
#         name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#       • Print a message to each of the two people still on your list, letting them know they’re still invited.
#       • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure 
#         you actually have an empty list at the end of your program.
print('# Exercise 3-7:\n')

print(f"Aww! The new table won't come in time! Only two of you can be invited!")

for i in range(len(guest_list)-2):
    print(f"I'm sorry {guest_list.pop(0)}, your invitation is, as of now, revoked.")

print("")

for i in guest_list:
    print(f"Hello {i}, just so you know, you are still invited!")

del guest_list[:]

print(f"\nThe remaining list is: {guest_list}\n")


# 3-8.  Seeing the World: Think of at least five places in the world you’d like to visit.
#
#       • Store the locations in a list. Make sure the list is not in alphabetical order.
#       • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#       • Use sorted() to print your list in alphabetical order without modifying the actual list.
#       • Show that your list is still in its original order by printing it.
#       • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#       • Show that your list is still in its original order by printing it again.
#       • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#       • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#       • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order
#         has been changed.
#       • Use sort() to change your list so it’s stored in reverse-alphabetical order.
#         Print the list to show that its order has changed.
print('# Exercise 3-8:\n')

locations_list: list = ['Japan','Iceland','New Zealand','Maldives','Qatar']

print(f"Here is the unmodified list: {locations_list}")
print(f"Here is the unmodified but sorted list: {sorted(locations_list)}")
print(f"Here is the same unmodified list: {locations_list}")
print(f"Here is the unmodified but reversed list: {sorted(locations_list,reverse=True)}")
print(f"Here is the same unmodified list: {locations_list}")

locations_list.reverse()

print(f"Here is the modified list in reverse order: {locations_list}")

locations_list.reverse()

print(f"Here is the modified list in the original order: {locations_list}")

locations_list.sort()

print(f"Here is the modified list in ascending order: {locations_list}")

locations_list.sort(reverse=True)

print(f"Here is the modified list in descending order: {locations_list}\n")


# 3-9.  Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating 
#       the number of people you’re inviting to dinner.
print('# Exercise 3-9:\n')

print(f"The number of people invited to the dinner is {len(locations_list)}\n")


# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, 
#       rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing 
#       these items and then uses each function introduced in this chapter at least once.
print('# Exercise 3-10:\n')

countries_list: list = ['Algeria','Saint Lucia','El Salvador','Cambodia','Bahrain','Namibia']

print(f'Here is the original list: {countries_list}')

countries_list.insert(len(countries_list)//2,'Zimbabwe')
countries_list.append('Singapore')

print(f'Here is the same list updated with two more countries: {countries_list}')
print(f'Here is one of the countries that has been popped from the list: {countries_list.pop(2)}')

del countries_list[2:4]

print(f'Here is the list updated with fewer countries: {countries_list}')
print(f'Here is the unmodified but sorted list: {sorted(countries_list)}')

countries_list.reverse()

print(f'Here is the modified list but sorted in reverse: {countries_list}')

countries_list.sort()

print(f'Here is the modified list with ascending order: {countries_list}\n')


# 6-1.  Person: Use a dictionary to store information about a person you know. Store their first name, last name, age,
#       and the city in which they live. You should have keys such as first_name, last_name, age, and city.
#       Print each piece of information stored in your dictionary.
print('# Exercise 6-1:\n')

personal_information1: dict = {'first_name':'Valerio','last_name':'Serra','age': 25,'city':'Rome'}

print(f"These are the personal informations that you required: ",end="")

for i in personal_information1.values():
    print(f"{i} ",end="")

print("\n")


# 6-2.  Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys
#       in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary.
#       Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual 
#       data for your program.
print('# Exercise 6-2:\n')

favorite_numbers: dict = {'Valerio':17,'Federico':3,'Riccardo':8,'Lorenzo':7,'Chiara':5}

print(f"Here are the names of your friends and their favorite number: ")

for i in favorite_numbers.items():
    print(f"{i[0]} : {i[1]}")

print("")


# 6-3.  Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion,
#       let’s call it a glossary.
#       • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys 
#         in your glossary, and store their meanings as values.
#       • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and
#         then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#         Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
print('# Exercise 6-3:\n')

glossary: dict = {
        'print':'prints a specified message to the screen',
        'del':'a keyword used to delete objects',
        'append':'adds a single item to certain collection types',
        'insert':'adds a single item in a speciefied position to certain collection types',
        '\\n':'a special character used for printing a new line'
    }

for i in glossary.items():
    print(f"{i[0]}: {i[1]}\n")

print("")


# 6-7.  People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, 
#       and store all three dictionaries in a list called people. Loop through your list of people. 
#       As you loop through the list, print everything you know about each person.
print('# Exercise 6-7:\n')

personal_information2: dict = {'first_name':'Federico','last_name':'Lattanzio','age':24,'city':'Rome'}
personal_information3: dict = {'first_name':'Damiano','last_name':'Mindrila','age':24,'city':'Rome'}
people: list = [personal_information1,personal_information2,personal_information3]

for i in people:
    for j in i.items():
        print(f"{j[0]}: {j[1]}")
    print("")

print("")


# 6-8.  Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include 
#       the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your 
#       list and as you do, print everything you know about each pet. 
print('# Exercise 6-8:\n')

pets_information1: dict = {'pet_name':'Luna','pet_kind':'cat','pet_owner':'Elisa Somari'}
pets_information2: dict = {'pet_name':'Rex','pet_kind':'dog','pet_owner':'Mirko Lattanzio'}
pets_information3: dict = {'pet_name':'Kira','pet_kind':'platypus','pet_owner':'Aiko Suzuki'}
pets_information4: dict = {'pet_name':'Pluto','pet_kind':'dog','pet_owner':'John Doe'}
pets_information5: dict = {'pet_name':'ScoobyDoo','pet_kind':'horse','pet_owner':'Marcus Rothschild'}
pets: list = [pets_information1,pets_information2,pets_information3,pets_information4,pets_information5]

for i in pets:
    for j in i.items():
        print(f"{j[0]}: {j[1]}")
    print("")

print("")


# 6-9.  Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
#       and store one to three favorite places for each person. To make this exercise a bit more interesting, 
#       ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name 
#       and their favorite places.
print('# Exercise 6-9:\n')

favorite_places: dict = {'Marco':['Spain','Greece','Italy'],'Jessica':['India','South Africa'],'Lorenzo':'Japan'}

for i in favorite_places.items():
    print(f"{i[0]}'s favorite places are: {i[1]}")

print("")


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#       Then print each person’s name along with their favorite numbers.
print('# Exercise 6-10:\n')

for i in favorite_numbers.items():
    j = i[0]
    favorite_numbers[j] = [i[1],i[1]**2,(i[1]**2)//2]

print(f"Here are the names of your friends and their favorite numbers: ")

for i in favorite_numbers.items():
    print(f"{i[0]}: {i[1]}")
    
print("")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#       Create a dictionary of information about each city and include the country that the city is in, 
#       its approximate population, and one fact about that city. 
#       The keys for each city’s dictionary should be something like country, population, and fact. 
#       Print the name of each city and all of the information you have stored about it.
print('# Exercise 6-11:\n')

cities: dict = {
        'Rome':{'country':'Italy','population':'2.8 million','fact':'Home of the Colosseum'},
        'Los Angeles':{'country':'California, U.S.A','population':'3.8 million','fact':'Hollywood\'s HQ'},
        'Singapore':{'country':'Singapore','population':'5.6 million','fact':'One of the world\'s greenest cities'}
    }

for i in cities.items():
    print(f"{i[0]} is a city located in {i[1]['country']}",
          f"with a population of {i[1]['population']} people",
          f"and it is {i[1]['fact']}")
    
print("")


# 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
#       Use one of the example programs from this chapter, and extend it by adding new keys and values, 
#       changing the context of the program, or improving the formatting of the output.
print('# Exercise 6-12:\n')

for i in favorite_numbers.items():
    i[1].append(8086)

print(f"Your friends added a new favorite number: ")

for i in favorite_numbers.items():
    print(f"{i[0]}: {i[1]}")
    
print("")