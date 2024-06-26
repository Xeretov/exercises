# Python Exercises
<br>
<details>
  <summary>exercises</summary>

>###### 15/04/2024 - Tipi di dato, Operatori e Collection
>
><details>
>  <summary>Lezione 2</summary><br>
>  
> 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"
>
> --- 
> 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
> 
> ---
> 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, "A person who never made a mistake never tried anything new."
>
> ---
> 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
>
> --- 
> 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
>
> ---
> 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
>
> ---
> 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
>
> ---
> 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."
>
> ---
> 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
>
> ---
> 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
> 
> • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
> 
> • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
> 
> • Print a second set of invitation messages, one for each person who is still in your list.
>
> ---
> 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
>
> • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
> 
> • Use insert() to add one new guest to the beginning of your list.
> 
> • Use insert() to add one new guest to the middle of your list.
> 
> • Use append() to add one new guest to the end of your list.
> 
> • Print a new set of invitation messages, one for each person in your list.
>
> ---
> 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
> 
> • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
> 
> • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
> 
> • Print a message to each of the two people still on your list, letting them know they’re still invited.
> 
> • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
>
> --- 
> 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
> 
> • Store the locations in a list. Make sure the list is not in alphabetical order.
> 
> • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
> 
> • Use sorted() to print your list in alphabetical order without modifying the actual list.
> 
> • Show that your list is still in its original order by printing it.
> 
> • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
> 
> • Show that your list is still in its original order by printing it again.
> 
> • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
> 
> • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
> 
> • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
> 
> • Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
>
> ---
> 3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.
>
> ---
> 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
>
> ---
> 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
>
> --- 
> 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
>
> ---
> 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
> 
> • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
> 
> • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
>
> ---
> 6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
>
> ---
> 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
>
> ---
> 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
>
> ---
> 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
>
> --- 
> 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
>
> ---
> 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
>
> ---
---
>###### 19/04/2024 - Cicli e Condizionali
>
><details>
>  <summary>Lezione 3</summary><br>
>
> 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
> 
> • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
> 
> • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
>
> ---
> 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
> • Modify your program to print a statement about each animal, such as A dog would make a great pet.
> • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
>
> ---
> 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
>
> ---
> 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
>
> ---
> 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
>
> ---
> 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
>
> ---
> 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
>
> ---
> 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
>
> ---
> 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
>
> ---
> 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
> 
> • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
> 
> • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
> 
> • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
>
> ---
> 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
> 
> • Add a new pizza to the original list.
>
> • Add a different pizza to the list friend_pizzas.
>
> • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
>
> ---
> 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
>
> ---
> 4-14. PEP 8: Look through the original [PEP 8 style guide](https://peps.python.org/pep-0008/) You won’t use much of it now, but it might be interesting to skim through it.
>
> ---
> 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
>
> ---
> 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code should look something like this:
> 
> ```python
> car = 'subaru'
> print("Is car == 'subaru'? I predict True.")
> print(car == 'subaru')
> print("\nIs car == 'audi'? I predict False.")
> print(car == 'audi')
> ```
>
> • Look closely at your results, and make sure you understand why each line evaluates to True or False.
>
> • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
>
> ---
> 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
>
> • Tests for equality and inequality with strings
>
> • Tests using the lower() method
>
> • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
>
> • Tests using the and keyword and the or keyword
>
> • Test whether an item is in a list
>
> • Test whether an item is not in a list
>
> ---
> 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
>
> • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
>
> • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
>
> ---
> 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
>
> • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
>
> • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
>
> • Write one version of this program that runs the if block and another that runs the else block.
>
> ---
> 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
>
> • If the alien is green, print a message that the player earned 5 points.
>
> • If the alien is yellow, print a message that the player earned 10 points.
>
> • If the alien is red, print a message that the player earned 15 points.
>
> • Write three versions of this program, making sure each message is printed for the appropriate color alien.
>
> ---
> 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
>
> • If the person is less than 2 years old, print a message that the person is a baby.
>
> • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
>
> • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
>
> • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
>
> • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
>
> • If the person is age 65 or older, print a message that the person is an elder.
>
> ---
> 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
>
> • Make a list of your three favorite fruits and call it favorite_fruits.
>
>• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!
>
> ---
> 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
>
> • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
>
> • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
>
> ---
> 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
>
> • If the list is empty, print the message We need to find some users!
>
> • Remove all of the usernames from your list, and make sure the correct message is printed.
>
> ---
> 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
>
> • Make a list of five or more usernames called current_users.
>
> • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
>
> • Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
>
> • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
>
> ---
> 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
>
> • Store the numbers 1 through 9 in a list.
>
> • Loop through the list.
>
> • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
>
> ---
---
>###### 22/04/2024 - Problem solving, Errori e Funzioni
>
><details>
>  <summary>Lezione 4</summary><br>
>
> 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
>
> ---
> 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.
>
> ---
> 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
>
> ---
> 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
>
> ---
> 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
>
> ---
> 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
>
> ---
> 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
>
> ---
> 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
>
> ---
> 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
>
> ---
> 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
>
> ---
> 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
>
> ---
> 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
>
> ---
> 8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
>
> ---
> 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 
>
> ---
> 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
>
> ---
> 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
> ```python
> import module_name
> from module_name import function_name
> from module_name import function_name as fn
> import module_name as mn
> from module_name import *
> ```
>
> ---
> 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
>
> ---
---
>###### 23/04/2024 - Problem solving, Errori e Funzioni
>
><details>
>  <summary>Lezione 4 - aggiuntivi</summary><br>
>
> 1. School Grading System:
>
> Create a function that takes a student's name and their scores in different subjects as input. The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.Create a for loop to iterate over a list of students and scores, calling the function for each student.
>
> ---
> 2. Guess the Number Game:
>
> Create a function that generates a random number within a range specified by the user. Prompt the user to guess the number within a specified maximum number of attempts. Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct. Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
>
> ---
> 3. E-commerce Shopping Cart:
>
> Create a function that defines a product with a name, price, and quantity. Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart. The function should calculate the cart total and apply any discounts or taxes.Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
>
> ---
> 4. Text Analysis:
>
> Create a function that reads a text file and counts the number of occurrences of each word. The function should print a report showing the most frequent words and their number of occurrences. You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences. Implement error handling to handle missing files or other input issues.
>
> ---
> 5. Inventory Management System:
>
> Create a function that defines an item with a code, name, quantity, and price. Create a database or dictionary to store the items in inventory. Implement functions to add, remove, search, and update items in the inventory. Use for loops and conditional statements to manage the various inventory operations.
>
> ---
> 6. Password Generator:
>
> Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols). Allow the user to specify the password length and desired character types. Generate and return a random password that meets the user's criteria.
>
> ---
> 7. Roman Numeral Conversion:
>
> Create a function that converts a given integer to its Roman numeral representation. Handle numbers from 1 to 3999. Use a combination of string manipulation and conditional statements to build the Roman numeral.
>
> ---
> 8. ATM Machine Simulator:
>
> Create a function that simulates an ATM machine. Initialize an account with a starting balance. Allow the user to perform transactions such as deposit, withdraw, and check balance. Validate transactions against the account balance and available funds. Provide appropriate feedback to the user for each transaction.
>
> ---
> 9. Caesar Cipher Encryption/Decryption
> 
> Create functions for encrypting and decrypting a message using the Caesar cipher. Allow the user to specify the shift value (number of positions to shift each letter). Handle both encryption and decryption using the same function with appropriate adjustments. Encrypt and decrypt the given message using the specified shift value.
>
> ---
> 10. Anagram Checker:
>
> Create a function that checks whether two given strings are anagrams of each other. Convert both strings to lowercase and remove any non-alphabetic characters. Sort the characters of each string and compare the sorted strings for equality. Indicate whether the strings are anagrams or not.
>
> ---
> 11. Word Search Puzzle Solver:
>
> Create a function that solves a word search puzzle. Provide a 2D grid representing the puzzle and a list of words to find. Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition. Output the locations of the found words within the grid.
>
> ---
> 12. Sieve of Eratosthenes Prime Number Generator:
>
> Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm. Initialize an array of all numbers up to the limit, marking each number as prime initially. Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime. The remaining unmarked numbers are the prime numbers within the limit. Return the list of prime numbers.
>
> ---
> 13. Fractal Tree Generator:
>
> Create a function that generates a fractal tree using recursion. Specify the starting trunk length and branching angle. Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length. Repeat the branching process until a desired level of detail is reached.
>
> ---
> 14. Sudoku Solver:
>
> Create a function that solves a Sudoku puzzle using backtracking. Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank. Implement a backtracking algorithm to check for valid placements in empty cells, ensuring no row, column, or 3x3 subgrid contains duplicates. Solve the puzzle by filling in the remaining empty cells with valid numbers.
>
> ---
> 15. Text Editor with Basic Functionality:
>
> Create a simple text editor that allows the user to open, edit, and save text files. Implement basic functionality such as inserting, deleting, and copying text. Provide undo/redo functionality to allow users to reverse actions. Save the edited text to a file when the user chooses to save.
>
> ---
---
>###### 07/05/2024 - Ripasso Generale
>
><details>
>  <summary>Lezione 5</summary><br>
>
> 1. Create a Playlist:
>
> Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.
>
> Example: 
>```python
> create_playlist("Road Trip", {"Song 1", "Song 2"})
>```
> Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.
>
> Example: 
>```python
> add_like(dictionary, "Road Trip", liked=True)
>```
> ---
> 2. Book Collection:
>
> Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. This function should return a dictionary where the author's name is the key and the value is a list of their books. Demonstrate this function by adding books for different authors.
>
> Example: 
> ```python
> add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
>```
> Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. This function should return an updated dictionary.
>
> Example: 
>```python
> delete_book(dictionary, "Mark Twain")
>```
> ---
> 3. Personal Info:
>
> Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. Make occupation, location, and age optional parameters. Use this function to create profiles for different people, demonstrating how it handles these optional parameters.
>
> Example: 
>```python
> build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
>```
> ---
> 4. Event Organizer:
>
> Write a function called plan_event() that accepts an event name, a list of participants, and an hour. The function should return a dictionary that includes the event name and a list of the participants. Call this function with varying numbers of participants to plan different events.
>
> Example: 
>```python
> plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"4pm")
>```
> Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.
>
> Example: 
>```python
> modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], "4pm")
>```
> ---
> 5. Shopping List:
>
> Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.
>
> Example: 
>```python
>create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
>```
> Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.
>
> Example: 
>```python
> print_shopping_list(dictionary, "Grocery Store")
>```
> ---
---
>###### 07/05/2024 - Ripasso Generale
>
><details>
>  <summary>Lezione 5 - aggiuntivi</summary><br>
>
> 1. Two Sum
>
> Given a list of integers and a target sum, find all unique pairs of integers within the list that sum up to the target.
>
> ---
> 2. Longest Increasing Subsequence
>
> Given a list of integers, find the length of the longest increasing subsequence within the list. An increasing subsequence is a sequence of elements from the array where each element is greater than or equal to the previous element.
>
> ---
> 3. Longest Common Subsequence
>
> Given two strings, find the length of the longest common subsequence (LCS) between them. An LCS is a subsequence of one string that is also a subsequence of the other string while maintaining the relative order of elements.
>
> ---
> 4. Word Break Problem: 
>
> Given a string and a dictionary of words, determine whether the string can be segmented into a space-separated sequence of one or more dictionary words. Each word in the dictionary must be a contiguous substring of the input string.
>
> ---
> 5. Longest Palindrome Subsequence:
>
> A palindrome is a word, phrase, or sequence that reads the same backwards as forward. Given a string, the task is to find the longest palindrome subsequence within the string. A subsequence is obtained from a string by deleting zero or more elements without changing the order of the remaining elements.
>
> ---
> 6. Armstrong Number Checker:
>
> Develop a function to check if a given number is an Armstrong number (the sum of its digits raised to the power of the number of digits equals the number itself).
>
> ---
> 7. Merge Two Sorted Lists: 
>
> Implement a function to merge two sorted lists into a single sorted list.
>
> ---
> 8. Find the Most Frequent Element:
>
> Create a function that finds the element that appears most frequently in a given list.
>
> ---
> 9. Find the Second Largest Element in an Array:
>
> Implement a function to find the second largest element in an unsorted list without using sorting algorithms.
>
> ---
> 10. Find the Intersection of Two Sorted Arrays:
>
> Implement a function to find the elements that are present in both of the two sorted lists.
>
> ---
---
>###### 25/05/2024 - Esercitazioni sulle classi
>
><details>
>  <summary>Lezione 6</summary><br>
>
> 1. Create student class
> - Attributes: <br>
>   name, study_program, age, gender
> 
> - Methods: <br>
>   print_info that prints the attributes
>
> ---
> 2. Create person class
> - Attributes: <br>
>   first_name, last_name, ssn,
>   birth_date, birth_place, gender
>
> - Methods: <br>
>   all getters and setters <br>
>   calculate_ssn (and update for every possible change)
>
> ---
> 3. Create animal class
> - Attributes: <br>
>   name, legs
>
> - Methods: <br>
>   setLegs and getLegs. <br>
>   print_info that prints all attributes of Animal
>
> ---
> 4. Create food and menu classes
> - Attributes: <br>
>   food: name, price, description <br>
>   menu: menu
>
> - Methods: <br>
>   add_food and remove_food <br>
>   print_prices and get_average_price
>
> ---
---
>###### 16/05/2024 - Ripasso funzioni
>
><details>
>  <summary>Lezione 7</summary><br>
>
>
> 1. Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). The numbers should be stored in a list and returned as output.
>
> ---
> 2. Write a function to calculate the factorial of a number given as input. The number should be returned as output. <br>For example:
> ```python
> Input: 8
> Output: 40320
> ```
> ---
> 3. Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. The list is given as input to the function. All factorials should be returned as output. <br>For example:
> ```python
> Input: [2, 5, 8, 10]
> Output: [2, 120, 40320, 3628800]
> ```
> ---
> 4. Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output. <br>For example:
>```python
> Input: 8
> Output: {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64}
>```
> ---
> 5. Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a comma-separated sequence after sorting them alphabetically. <br>For example:
>```python
> Input: "without,hello,bag,world"
> Output: "bag,hello,without,world"
>```
> ---
> 6. Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising all sentence characters. <br>For example:
>```python
> Input: ["Practice", "makes", "perfect"]
> Output: ["PRACTICE", "MAKES", "PERFECT"]
>```
> ---
> 7. Write a function accepting an input string defined with whitespace-separated words and returning it after removing all duplicates and sorting each word alphanumerically. For example:
>```python
> Input: "hello world and practice makes perfect and hello world again"
>
> Output: "again and hello makes perfect practice world"
>```
> ---
> 8. Write a function to check whether a string is a pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once.
>```python
> Input: "The quick brown fox jumps over the lazy dog"
> Output: True
>```
> ---
> 9. Write a function to check whether a number is "Perfect" or not. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). <br>For example:
>```python
> Input: 6
> Output: True
>```
> ---
> 10. Using the code implemented in Exercise 8, write a function that, given a number n as input, computes all "Perfect" numbers between 1 and n. <br>For example:
>```python
> Input: 500
> Output: [6, 28, 496]
>```
> ---
> 11. Write a function to sort the (name, age, height) input list of tuples by ascending order where name is string, age and height are numbers. The function should return a list of tuples of strings. The priority is that name > age > score. Namely, the sort criteria are: <br>
>        Sort based on name;<br>
>        Then, sort based on age;<br>
>        Then, sort by score.
>```python
> Input: [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]
>
> Output:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
>```
> ---
---
>###### 30/05/2024 - Esercizi su classi astratte, class methods e static methods
>
><details>
> <summary>Lezione 8</summary><br>
><b>Exercise 1: Creating an Abstract Class with Abstract Methods</b><br>
> Create an abstract class Shape with an abstract method area and another abstract method perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
>
> ---
> <b>Exercise 2: Implementing Static Methods</b><br>
> Create a class MathOperations with a static method add that takes two numbers and returns their sum, and another static method multiply that takes two numbers and returns their product.
>
> ---
> <b>Exercise 3: Library Management System</b><br> 
>Create a <b>Book</b> class containing the following attributes:<br>
> - title, author, isbn
>
>The <b>book</b> class must contains the following methods:<br>
> - __str__ method to return a string representation of the book.
> - @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn".<br> It means that you must use the class reference cls to create a new object of the Book class using a string.
>
>   - Example:<br>
> ```python
> book = “La Divina Commedia, D. Alighieri, 999000666”
> divina_commedia: Book = Book.from_string(book)
> 
> # Here divina_commedia must contain an instance of the class Book with 
>
> title = La Divina Commedia, author = D. Alighieri, isbn = 999000666
>```
>Create a <b>Member</b> class with the following attributes: <br>
> - name, member_id, borrowed_books<br>
>
> The <b>member</b> class must contain the following methods:
> - borrow_book(book) to add a book to the borrowed_books list.
> - return_book(book) to remove a book from the borrowed_books list.
> - __str__ method to return a string representation of the member.
> - @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".
>
> Create a <b>Library</b> class with the following attributes:<br> 
> - books, members, total_books<br> (class attribute to keep track of the total number of books)<br>
>
> The <b>library</b> class must contain the following methods:
> - add_book(book) to add a book to the library and increment total_books.
> - remove_book(book) to remove a book from the library and decrement total_books.
> - register_member(member) to add a member to the library.
> - lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.
> - __str__ method to return a string representation of the library with the list of books and members.
> - @classmethod library_statistics(cls) to print the total number of books.
>
> Create a script and play a bit with the classes:<br>
> Create instances of books and members using class methods. Register members and add books to the library. Lend books to members and display the state of the library before and after lending.
> 
> ---
> <b>Exercise 4: University Management System</b>
>
> Create a system to manage a university with departments, courses, professors, and students. <br>
> Create an abstract class <b>Person</b>:<br>
> Attributes:
> - name (str)
> - age (int)
> 
> Methods:
>
> - __init__ method to initialize the attributes.<br>
> - Abstract method get_role to be implemented by subclasses.<br>
> __str__ method to return a string representation of the person.<br>
>
> Create subclasses Student and Professor that inherit from Person and implement the abstract methods:<br>
>
> - Student:<br>
> Additional attributes: 
>   - student_id (string), 
>   - courses (list of Course instances)
>   - Method enroll(course) to enroll the student in a course.
>
> - Professor:<br>
> Additional attributes: 
>   - professor_id (string), 
>   - department (string), courses (list of Course instances)
>   - Method assign_to_course(course) to assign the professor to a course.
>
> Create a class Course:
><br>Attributes:
>
> - course_name (string)
> - course_code (string)
> - students (list of Student instances)
> - professor (Professor instance)
>
> <br>Methods:
> - __init__ method to initialize the attributes.
> - add_student(student) to add a student to the course.
> - set_professor(professor) to set the professor for the course.
> - __str__ method to return a string representation of the course.<br>
>
> Create a class Department:<br>
> Attributes:
> - department_name (string)
> - courses (list of Course instances)
> - professors (list of Professor instances)<br>
>
> Methods:
> 
> - __init__ method to initialize the attributes.
> - add_course(course) to add a course to the department.
> - add_professor(professor) to add a professor to the department.
> - __str__ method to return a string representation of the department.<br>
>
> Create a class University:
> <br>Attributes:
>
> - name (string)
> - departments (list of Department instances)
> - students (list of Student instances)<br>
>
> Methods:
> - __init__ method to initialize the attributes.
> - add_department(department) to add a department to the university.
> - add_student(student) to add a student to the university.
> - __str__ method to return a string representation of the university.
>
> Create a script:<br>
> Create instances of departments, courses, professors, and students. Add them to the university. Enroll students in courses and assign professors to courses. Display the state of the university.
>
>---
---
>###### 28/06/2024 - Ereditarietà e Polimorfismo
>
><details>
>   <summary>Lezione 8 - aggiuntivi </summary>
>
> 1. The Number of Beautiful Subsets:<br> write a function with an array nums of positive integers and a positive integer k given as inputs.<br> A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.<br> Return the number of non-empty beautiful subsets of the array nums.<br> A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.<br> Two subsets are different if and only if the chosen indices to delete are different.
>     ```
>     Example 1:
>     Input: nums = [2,4,6], k = 2
>     Output: 4
>     
>     Example 2:
>     Input: nums = [1], k = 1
>     Output: 1
>     ```
> 2. Combinations:<br> given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].<br> You may return the answer in any order.
>     ```
>     Example 1:
>     Input: n = 4, k = 2
>     Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
>     
>     Example 2:
>     Input: n = 1, k = 1
>     Output: [[1]]
>     ```
>
> 3. Generate Parentheses:<br> Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
>     ```
>     Example 1:
>     Input: n = 3
>     Output: ["((()))","(()())","(())()","()(())","()()()"]
>     
>     Example 2:
>     Input: n = 1
>     Output: ["()"]
>     ```
>---
---
>###### 25/05/2024 - Esercitazione sulle Classi
>
><details>
>  <summary>Lezione 11</summary><br>
> 1. <b>Sistema di Prenotazione Cinema</b><br>
> Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
> 
> <br><b>Classi</b>:<br>
> - Film: Rappresenta un film con titolo e durata.
> 
> - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
>
>   - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
>   - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
> 
>- Cinema: Gestisce le operazioni legate alla gestione delle sale.
>
>    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
>    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
>
> <br><b>Test case</b>:<br>
> - Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
> - Un cliente sceglie un film e prenota un certo numero di posti.
> - Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione. 
>
> ---
> <br>
> 2. <b>Gestione di un magazzino</b><br>
> Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.
>
> <b>Classi</b>:<br>
> - Prodotto:
>   - nome (stringa)
>   - quantità (intero)
>
> - Magazzino:
>   - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
>   - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
>   - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
>
> <br><b>Test case</b>:<br>
> - Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
> - Il sistema cerca un prodotto per verificare se esiste nell'inventario.
> - Il sistema verifica la disponibilità dei prodotti in inventario.<br>
>
> ---
---
>###### 29/05/2024 - Esercitazione sulle Classi
>
><details>
>  <summary>Lezione 12</summary><br>
> <br>
> 1. <b>Sistema di Gestione Biblioteca</b><br>
> Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
> 
><br><b>Classi</b>:<br>
> - Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).
>
> - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.
>    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
>
>    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.
>
>    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.
>
>    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.
>
> <br><b>Test Cases</b>:<br>
> - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
> - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
> - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
> - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
>
> <br>
> 2. <b>Catalogo Film</b><br> 
>Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.
>
><br><b>Classe</b>:<br>
> - MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.
>
>   - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.
>
>   - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
>
>   - list_directors(): Elenca tutti i registi presenti nel catalogo.
>
>   - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.
>
>   - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
>
> ---
---
>###### 26/06/2024 - Context Managers
><details>
>   <summary>lezione 15</summary>
>
><b>Esercizio 1</b><br>
>Crea un context manager usando una classe
>
>Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.
>
>Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__
>
>Esempio di funzionamento:
>
>Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.
> ```python
> with FileManager('example.txt', 'w') as f:
>
>    f.write('Hello, world!')
> ```
> <br>
> <b>Esercizio 2</b><br>
>Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with:
>
> ```python
> with Timer():
>
>    time.sleep(1)
>
> time elapsed: 1.00000
> ```
>
> in questo esempio il tempo passato non sarà mai uguale a 1
>
> ---
---
>######  12/06/2024 - Esercizio Classi, Ereditarietà, UnitTest
>
><details>
> <summary>lezione 17</summary>
>
>> <details>
>>   <summary>Hospital System</summary>
>>
>>   ### CLASSE: Persona
>> Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
>>
>> <b>La classe Persona deve avere i seguenti metodi:</b>
>> - init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name non sono due stringhe, allora assegnare None all'età.
>> - setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
>> - setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
>> - setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
>> - getName(): consente di ritornare il nome di una persona.
>> - getLastname(): consente di ritornare il cognome di una persona.
>> - getAge(): consente di ritornare l'età di una persona.
>> - greet(): stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"
>>
>>  ### CLASSE: Dottore
>> Creare un file chiamato "dottore.py".
>> In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.
>>
>> Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcella per le visite in studio (si usi il tipo float). Gli attributi della classe dottore devono essere anch'essi privati.
>>
>> <b>Definire i seguenti metodi:</b>
>> - costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel). Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".
>> - setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".
>> - setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".
>> - getSpecialization(): consente di ritornare la specializzazione del dottore.
>> - getParcel(): consente di ritornare la parcella del dottore.
>> - isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. In caso contrario, stampare "Doctor nome e cognome is not valid!".
>> - doctorGreet():tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specializzazione}"
>>
>> ### CLASSE: Paziente
>> Creare un file chiamato "paziente.py".
>> In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.
>> 
>> Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).<br>
>> <b> Definire i seguenti metodi:</b>
>> - costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
>> - setIdCode(idCode): consente di impostare il codice identificativo del paziente.
>> - getidCode(): consente di ritornare il codice identificativo del paziente.
>> - patientInfo(): stampa in output le informazioni del paziente in questo modo: 
>> ```python
>>        f"Paziente: {nome} {cognome}
>>         ID: {codice identificativo}"
>> ```
>> 
>>### CLASSE: Fattura
>> Creare un file chiamato "fatture.py".
>> In tale file, creare una classe chiamata Fattura.
>>
>> <b> Definire i seguenti metodi:</b>
>> - init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
>> - getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
>> - getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
>> - addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
>> - removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
>>
>> ### Creazione di Test Case con UnitTest
>> Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
>>
>> <b>Istruzioni</b><br>
>> Creare un nuovo file Python denominato "test_persona.py".
>> Importare il modulo unittest e tutte le classi definite.
>>
>><b>Test della Classe Persona</b>
>>- Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
>>- Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
>>- Scrivere test per verificare:
>>    - L'inizializzazione corretta degli attributi first_name, last_name e age.
>>    - Il funzionamento dei metodi setName, setLastName e setAge.
>>
>><b>Test della Classe Dottore</b>
>>- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
>>- Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
>>- Scrivere test per verificare:
>>    - L'inizializzazione corretta degli attributi specifici di Dottore.
>>    - Il funzionamento del metodo isValidDoctor con diverse età.
>>
>><b>Test della Classe Paziente</b>
>>- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
>>- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
>>- Scrivere test per verificare:
>>    - L'inizializzazione corretta degli attributi specifici di Paziente.
>>
>><b>Test della Classe Fattura</b>
>>- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
>>- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
>>- Scrivere test per verificare:
>>    - L'inizializzazione corretta della classe Fattura.
>>    - Il calcolo corretto del salario e del numero di fatture.
>>    - L'aggiunta e la rimozione di pazienti dalla lista.
>>
> ---
>> <details>
>>   <summary>Blockbuster System</summary>
>>
>> ### CLASSE: Film
>> In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
>> 
>> <b> Definire i seguenti metodi:</b>
>> - init(id, title): metodo costruttore.
>> - setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
>> - setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
>> - getID(): che consente di ritornare il valore del codice identificativo di un film.
>> - getTitle(): che consente di ritornare il valore del titolo di un film.
>> - isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
>> 
>>### CLASSI GENERE
>>Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.
>>
>> <b> Per ognuna di queste classi si implementi un metodo chiamato:</b>
>> - getGenere(), che ritorna il genere di film
>> - getPenale(), che ritorna il valore della penale
calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
>>
>>Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".
>> 
>>### CLASSE: Noleggio
>>In un file "noleggio.py", creare una classe Noleggio.
>>Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), un dizionario (rented_film) che ha come chiave un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente i film affittati dal cliente.
>> 
>><b> Definire i seguenti metodi:</b>
>> - init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
>> - isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
>> - rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:<br>
>>    - la chiave sarà l'id del cliente che noleggia (id_client)<br>
>> il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.<br>
>> Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: "Il cliente {clientId} ha noleggiato {titolo_film}!". Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: Non è possibile nolegiare il film {titolo_film}!".<br>
>> - giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
>> - printMovies(): stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"
>> - printRentMovies(clientID): questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
>> ### Creazione di Test Case con UnitTest
>>Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Film, Azione, Commedia, Dramma, e Noleggio. 
>>
>><b>Istruzioni</b><br>
>>Creare un nuovo file Python denominato "test_blockbuster.py".
>>Importare il modulo unittest e tutte le classi definite.
Creare una sola classe di test chiamata TestFilm che eredita da unittest.TestCase.
>> 
>><b>Configurazione Iniziale:</b><br>
>>  Utilizzare il metodo setUp per creare l'ambiente di test:
>>   - In setUp, istanziare 10 film (5 di azione, 4 commedie e 1 drammatico) e aggiungerli a una lista di film.
>>   - Creare un oggetto Noleggio utilizzando la lista di film creata.
>>
>>Testare la Disponibilità di un Film (isAvaible):
>>- Scrivere un test per verificare che un film disponibile ritorni True.
>>- Scrivere un test per verificare che un film non disponibile ritorni False.
>>
>>Testare il Noleggio di un Film (rentAMovie):
>>- Scrivere un test per verificare che un film disponibile possa essere noleggiato correttamente.
>>- Dopo il noleggio, verificare che il film non sia più disponibile.
>>- Verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.
>>
>>Testare il Noleggio di un Film Non Disponibile:
>>- Noleggiare un film con un cliente.
>>- Provare a noleggiare lo stesso film con un altro cliente e verificare che non sia possibile.
>>
>>Testare la Restituzione di un Film (giveBack):
>>- Noleggiare un film e poi restituirlo.
>>- Verificare che il film restituito sia nuovamente disponibile.
>>- Verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.
>>
>>Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo):
>>- Scrivere test per verificare il calcolo della penale di ritardo per film di diversi generi (azione, commedia, dramma).
>>
>>Testare la Stampa dei Film Disponibili (printMovies):
>>- Verificare che la lista dei film disponibili contenga i titoli corretti.
>>
>>Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies):
>>- Noleggiare uno o più film per un cliente.
>>- Verificare che la stampa dei film noleggiati contenga i titoli corretti.
>>
> ---
---
> ###### 13/06/2024 - Le eccezioni in Python
>
> <details>
>   <summary>Lezione 18</summary>
>
> 1. <b>Safe Square Root</b>: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.
>
> 2. <b>Password Validation</b>: Write a function validate_password(password) that checks if a password meets certain criteria (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
>
> 3. <b>Context Managers for File Handling</b>: Use the with statement and context managers to open and close a file. Handle potential IOError within the with block for clean resource management.
>
> 4. <b>Database of dates</b>:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string.
>
> 5. <b>An interactive calculator</b>: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
>     - If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
>     - Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
>     <br> If the second input is not '+' or '-', again raise a FormulaError.
>     <br> If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.
>
> 6. <b>Personalized math library</b>: Create a Python library that provides functions for handling fractions, with built-in error handling. The library must include functions for the following operations:
>     - Create a fraction from the numerator and denominator.
>     - Collect the numerator and denominator of a fraction.
>     - Simplify a fraction.
>     - Add, subtract, multiply and divide fractions.
>     - Check whether one fraction is equivalent to another. 
>     - All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero.<br> The library must raise custom exceptions to indicate specific errors to the user.
>
> <b>Custom Exception for Data Structure Integrity</b>: Define a custom exception class DataStructureIntegrityError.  Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error).
>
> ---
---
> ###### 12/06/2024 - Classi Astratte, Ereditarietà, Polimorfismo
>
> <details>
>   <summary> Lezione 20 </summary>
>
> 1. <b>GESTIONALE PAGAMENTO</b><br>
> Si definisca una nuova classe <b>Pagamento</b> che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set().<br> L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno.<br> Si crei inoltre un metodo <b>dettagliPagamento()</b> che visualizza una frase che descrive l'importo del pagamento, ad esempio:
>    ```python
>     "Importo del pagamento: €20.00" 
>    ```
>    Quando viene stampato, l'importo è sempre con 2 cifre   decimali.<br><br>
> Successivamente, si definisca una classe <b>PagamentoContanti</b> che sia derivata da Pagamento e definisca l'importo.<br> Questa classe dovrebbe ridefinire il metodo <b>dettagliPagamento()</b> per indicare che il pagamento è in contanti.<br> Si definisca inoltre il metodo <b>inPezziDa()</b> che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.<br><br>
> Si definisca una classe <b>PagamentoCartaDiCredito</b> derivata anch'essa da Pagamento e che definisce l'importo.<br> Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito.<br> Infine, si ridefinisca il metodo <b>dettagliPagamento()</b> per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.<br>
> Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.<br>
> <b>Esempio di output</b>:
>     ```
>     Pagamento in contanti di: €150.00
>     150.00 euro da pagare in contanti con:
>     1 banconota da 100 euro
>     1 banconota da 50 euro
>   
>     Pagamento in contanti di: €95.25
>     95.25 euro da pagare in contanti con:
>     1 banconota da 50 euro
>     2 banconote da 20 euro
>     1 banconota da 5 euro
>     1 moneta da 0.2 euro
>     1 moneta da 0.05 euro
>   
>     Pagamento di: €200.00 effettuato con la carta di credito
>     Nome sulla carta: Mario Rossi
>     Data di scadenza: 12/24
>     Numero della carta: 1234567890123456
>   
>     Pagamento di: €500.00 effettuato con la carta di credito
>     Nome sulla carta: Luigi Bianchi
>     Data di scadenza: 01/25
>     Numero della carta: 6543210987654321
>     ``` 
> 2. <b>RENDERING GRAFICO</b><br>
>Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.<br>
>Definire la classe astratta <b>Forma</b> che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le funzionalità base di ogni forma, come i metodi astratti <b>getArea()</b> per calcolare l'area e <b>render()</b> per disegnare su schermo la forma.<br><br>
>Definire la classe <b>Quadrato</b> che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.<br>
>Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".<br>
>Il metodo getArea() deve calcolare l'area del quadrato.<br>
>Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore.<br> Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("\*") lungo il suo perimetro. (Vedi Esempio di output)<br><br>
>Definire la classe <b>Rettangolo</b> che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.<br>
>Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome della forma su "Rettangolo".<br>
>Il metodo getArea() deve calcolare l'area del rettangolo.<br>
>Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore.<br> Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("\*") lungo il suo perimetro. (Vedi Esempio di output)<br><br>
>Definire la classe <b>Triangolo</b> che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).<br>
>Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".<br>
>Il metodo getArea() deve calcolare l'area del triangolo.<br>
>Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel costruttore.<br> Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("\*") lungo il suo perimetro. (Vedi Esempio di output)<br><br>
> *Hint: per il disegno utilizzare print("\*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.*
>
><b>Esempi di output</b>:<br>
>```
>Ecco un Quadrato di lato 4!
>
>* * * *
>*      *
>*      *
>* * * *
>L'area di questo quadrato vale: 16
>
>Ecco un Rettangolo avente base 8 ed altezza 4!
>* * * * * * * *
>*                *
>*                *
>* * * * * * * *
>L'area di questo rettangolo vale: 32
>
>Ecco un Triangolo avente base 4 ed altezza 4!
>*      
>* *    
>*   *  
>* * * *
>L'area di questo triangolo vale: 8.0
> ```
> ---
---
</details>
<br>
<details>
  <summary>projects</summary>

> ###### 13/05/2024 - progetto zoo
> <details>
>   <summary>project zoo</summary><br>
>
> Sistema di gestione dello zoo virtuale
>
> Classi:
>
> 1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
>
> 2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
>
> 3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
>
> 4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.
>
> Funzionalità:
>
> 1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.
>
> 2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.
>
> 3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
>
> 4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.
>
> 5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 
>
> E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:
>```
> Guardians:
>
> ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)
>
> Fences:
>
> Fence(area=100, temperature=25, habitat=Continent)
>
> with animals:
>
> Animal(name=Scoiattolo, species=Blabla, age=25)
>
> Animal(name=Lupo, species=Lupus, age=14)
> #########################
>```
> Fra un recinto e l'altro mettete 30 volte il carattere #.
> </details>
---
> ###### 14/05/2024 - progetto lepre e tartaruga
> <details>
>   <summary>project hare and turtle</summary><br>
> In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:
>
> - Tartaruga:
>     - Passo veloce (50% di probabilità): avanza di 3 quadrati.
>     - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
>     - Passo lento (30% di probabilità): avanza di 1 quadrato.
>
> - Lepre:
>     - Riposo (20% di probabilità): non si muove.
>     - Grande balzo (20% di probabilità): avanza di 9 quadrati.
>     - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
>     -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
>     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.
>
> Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.
>
> Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.
>
> Iniziate la gara stampando:
> ```python
> "BANG !!!!! AND THEY'RE OFF !!!!!"
> ```
> Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.
>
> Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.
>
> Requisiti del Codice:
> - Utilizzare il modulo random per la generazione dei numeri casuali.
> - Definire e utilizzare:
>     - una funzione per visualizzare le posizioni sulla corsia di gara,
>     - una funzione per calcolare la mossa della tartaruga,
>     - una funzione per calcolare la mossa della lepre.
> - Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
> 
> <b>SFIDE AGGIUNTIVE:</b>
> 1. Variabilità Ambientale:
> Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
> Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
>
> Modificatori mossa:
> - La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
> - La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
> 
> 2. Energia o Stamina:
> Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. L'energia inziale per entrambi gli animali è 100.
>
> <b>Nuove regole di movimento:</b>
> - Tartaruga:
>     - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia. Non può superare l'energia iniziale.
>     - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
>     - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
>     - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.
>
> - Lepre:
>     - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
>     - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
>     - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
>     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
>     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
> 
> 3. Ostacoli e Bonus
> Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il movimento degli animali quando vengono calpestati. Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.
>
> <b>Dettagli Implementativi:</b>
> - Ostacoli:
> Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7). Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso (chiave) ed i relaviti effetti (valore). Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.
>
> - Bonus:
> Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale di un numero determinato di quadrati (es: 5, 3, 10). I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso (chiave) ed i relaviti effetti (valore). Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.
>
> </details>
---
> ###### 15/05/2024 - progetto N*Queen
> <details>
>   <summary>project NQueen</summary><br>
>
> Create a backtracking function that can solve the NQueen problem
> </details>
</details>
<br>

> [!WARNING]
>
> Imported modules may not work, add parent directory "exercises" to sys.path
> ```python
> import sys
> sys.path.append("repo_directory")
> ```
> or add to
> home\user\\.bashrc
> this line:
> ```bash
> export PYTHONPATH="${PYTHONPATH}:/home/user/repo_directory"
> ```
