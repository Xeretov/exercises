# Esercizi
---
## 15/04/2024
<details>
  <summary>Lezione 2</summary>
  
> 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
>
> --- 
> 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
> 
> ---
> 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
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
> 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
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
</details>
17/04/2024
<details>
  <summary>Lezione 3</summary>

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
```python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
```
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

</details>
