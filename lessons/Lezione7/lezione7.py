# Gioele Amendola
# 16/05/2024


# Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers should be stored in a list and returned as output.
def seven_notFive() -> list:
    numbers: list = [number for number in range(2000,3201) if number % 7 == 0 and number % 5 != 0]
    return numbers


# Write a function to calculate the factorial of a number given as input. The number should be returned as output. For example:
#     Input: 8
#     Output: 40320
def factorial(num: int = None) -> int:
    if not num:
        num = int(input("> "))
    if num <= 0:
        raise Exception("Number less than 1")
    result: int = 1
    for x in range(1, num+1):
        result *= x
    return result

# Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers.
# The list is given as input to the function. All factorials should be returned as output. For example:
#     Input: [2, 5, 8, 10]
#     Output: [2, 120, 40320, 3628800]
def list_factiorial(numbers: list) -> list:
    for i,number in enumerate(numbers):
        numbers[i] = factorial(number)
    return numbers

# Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) pairs
# such that i is an integer between 1 and n (both included). The function should return the dictionary as output. For example:
#     Input: 8
#     Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def power_two(num: int = None) -> dict:
    result: dict = {}
    if not num:
        num = int(input("> "))
    if num <= 0:
        raise Exception("Number less than 1")
    for number in range(1, num+1):
        result[number] = number*number
    return result


# Write a function that accepts a string with a comma-separated sequence of words as input
# and prints the words as a comma-separated sequence after sorting them alphabetically. For example:
#     Input: without,hello,bag,world
#     Output: bag,hello,without,world
def organize_comma(string: str) -> str:
    strings: list = string.split(",")
    strings = sorted(strings)
    result: str = ",".join(word for word in strings)
    return result
# Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising
# all sentence characters. For example:
#     Input: Practice makes perfect
#     Output: PRACTICE MAKES PERFECT
def capitalize(strings: list[str]) -> str:
    for i,string in enumerate(strings):
        strings[i] = string.upper()
    return strings

# Write a function accepting an input string defined with whitespace-separated words
# and returning it after removing all duplicates and sorting each word alphanumerically. For example:
#     Input: hello world and practice makes perfect and hello world again
#     Output: again and hello makes perfect practice world
def organize_string(string: str) -> str:
    strings: set = set(string.split(" "))
    strings = sorted(strings)
    result = " ".join(word for word in strings)
    return result

# Write a function to check whether a string is a pangram or not.
# Pangrams are words or sentences containing every letter of the alphabet at least once.
#     Input: The quick brown fox jumps over the lazy dog
#     Output: True
from string import ascii_lowercase
def is_pangram(string: str) -> bool:
    alphabet: list = list(ascii_lowercase)
    for char in string:
        if char.lower() in alphabet:
            alphabet.remove(char.lower())
    return True if not alphabet else False

# Write a function to check whether a number is "Perfect" or not.
# In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). For example:
#     Input: 6
#     Output: True
def is_perfect_number(num: int) -> bool:
    check: int = sum(number for number in range(1,num//2 + 1) if num % number == 0)
    return True if check == num else False

# Using the code implemented in Exercise 8, write a function that, given a number n as input, computes all "Perfect" numbers between 1 and n. For example:
#     Input: 500
#     Output: [6, 28, 496]
def list_perfect(num: int = None) -> list:
    result: list = []
    if not num:
        num = int(input("> "))
    if num <= 0:
        raise Exception("number less than 1")
    for x in range(1, num+1):
        result.append(x) if is_perfect_number(x) else None
    return result

# Write a function to sort the (name, age, height) input list of tuples by ascending order where name is string,
# age and height are numbers. The function should return a list of tuples of strings.
# The priority is that name > age > score. Namely, the sort criteria are:
#     Sort based on name;
#     Then, sort based on age;
#     Then, sort by score.

#     Input: [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]
#     Output:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
def sort_people(people: list[tuple]) -> list[tuple]:
    name: list = [list(x) for x in people]
    name = sorted(tuple(name[i]) for i in range(len(name)))
    return name
