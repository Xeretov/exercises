'''
Module providing a function returning
a boolean when the istances of two strings
is the same
'''
# Gioele Amendola
# 29/04/2024

# Create a function that checks whether two given strings are anagrams of each other.
# Convert both strings to lowercase and remove any non-alphabetic characters.
# Sort the characters of each string and compare the sorted strings for equality.
# Indicate whether the strings are anagrams or not.


def isanagram(string1: str, string2: str) -> bool:
    '''
    Check if two strings are an anagram of eachother

    Args:
        string1 (str): first string
        string2 (str): second string

    Returns:
        bool: True if string1 is equal to string2
    '''

    string1 = ''.join(char.lower() for char in string1 if char.isalpha())
    string2 = ''.join(char.lower() for char in string2 if char.isalpha())
    string1 = sorted(string1)
    string2 = sorted(string2)

    return string1 == string2


# Example Test:
print(isanagram("coolbeaa.21!", "ciao"))
print(isanagram('Pi1ll03!ola', 'lliP!.,lao'))
