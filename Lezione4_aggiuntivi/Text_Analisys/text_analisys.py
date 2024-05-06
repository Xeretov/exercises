'''Module providing a function printing
the occurances of every word given
a text file.
'''
# Gioele Amendola
# 27/04/2024

# Create a function that reads a text file and counts the number of occurrences of each word.
# The function should print a report showing the most frequent words and
# their number of occurrences.
# You can use a for loop to iterate over the words in the text and
# a dictionary to store the occurrences.
# Implement error handling to handle missing files or other input issues.

# Import string for exclude variable (special characters)
import string
# Import Path to open file in same directory
from pathlib import Path


def count_words(file_name: str):
    '''
    Given a file, count the occurances of every word
    and print the result

    Args:
        file_name (str): the name of the file
    '''

    # If name or path of the file given to the function is not correct, catches the except and exits
    try:
        # Finds current path of file
        p = Path(__file__).with_name(file_name)
        # Opens file in read
        with open(p, "r", encoding="utf8") as file:
            text_file = file.read()
    except FileNotFoundError:
        # If name or path of the file given is incorrect:
        print("\nAn error occured while opening text file\n")
        input("Press ENTER to continue...\n\n")
    else:
        # If name or path of the file given is correct:
        print("\nFile opened Succesfully\n")
        input("Press ENTER to continue...\n\n")

        # Dictionary for words occurrances
        words_occurrance: dict = {}
        # Contains a set of special characters
        exclude: set = set(string.punctuation)

        # Iterate in opened file line by line
        for text_word in text_file.split():
            # Check if word is in dictionary or not.
            # If it is, adds 1 to occurance
            # Otherwise adds the word to the dictionary
            text_word = text_word.lower()
            # Removes special characters from the string
            if text_word[-1] in exclude:
                text_word = text_word[:-1]
            if text_word in words_occurrance:
                words_occurrance[text_word] += 1
            else:
                words_occurrance[text_word] = 1

        # Closing of file
        file.close()

        # Sort by alphabetical order
        words_occurrance = dict(sorted(words_occurrance.items()))
        # Sort by occurances (sort iterable 'words_occurance.items()'
        # by the value of the dictionary x[1])
        words_occurrance = dict(
            sorted(words_occurrance.items(), key=lambda x: x[1]))

        # Print of how many words and which one are the most used
        print(f"\nTotal Words: {sum(words_occurrance.values())}\n")
        for word, i in zip(words_occurrance.keys(), range(1, len(words_occurrance.keys())+1)):
            print(f"{word}: {words_occurrance[word]} ", end="")
            if i % 5 == 0:
                print("")
        print("\n\n")


count_words("Lorem_Ipsum.txt")
