'''
This module contains the animal class

# Gioele Amendola
# 09/05/2024

# Create a Class that represents an Animal
# name, legs

# Define methods setLegs and getLegs
# Add method print Info that prints all attributes of Animal
'''
class Animal:

    def __init__(self, name: str, legs: int) -> None:
        self.name = name
        self.legs = legs

    def get_legs(self) -> str:
        '''
        This method is used to get the variable legs.

        Returns:
            str: self.legs
        '''
        return self.legs
    
    def set_legs(self, legs: str) -> None:
        '''
        This method is used to set the variable legs.

        Args:
            legs (str): variable that will replace self.legs
        '''
        self.legs = legs
    
    def print_info(self) -> None:
        '''
        This method is used to print all attributes of the Animal
        '''
        print(f"The animal {self.name} has {self.legs}")

animal1: Animal = Animal("Cat",3)
animal2: Animal = Animal("Dog",5)
print(animal1.name)
print(animal2.name)
animal1.legs = 4
animal2.set_legs(4)
print(animal2.get_legs())
animal1.print_info()
animal2.print_info()
