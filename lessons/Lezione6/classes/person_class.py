'''
Module used for studying the classes in python.

Returns:
    Person: Class describing a person

# Gioele Amendola
# 08/05/2024

# Python classes:

# Create a Class that represents a Person
# first_name, last_name, ssn
# birth_date, birth_place, gender

# Define all getters and setters
# Define a method that calculates ssn (and update for every possible change)
'''
from typing import Literal

class Person:
    '''
    A class offering a general description of a person and
    a method to generate theirs social security number.
    '''

    def __init__(self, first_name: str, last_name: str, **kwargs: str) -> None:

        self.first_name: str = first_name
        self.last_name: str = last_name
        self.birth_date: str = ""
        if kwargs.get('birth_date'):
            self.birth_date: str = kwargs["birth_date"]
        self.birth_place: str = ""
        if kwargs.get('birth_place'):
            self.birth_place: str = kwargs["birth_place"]
        self.gender: str = ""
        if kwargs.get('gender'):
            self.gender: Literal["Maschio","Femmina","M","F"] = kwargs["gender"]
        self._ssn: str = ""
        if kwargs.get('birth_date') and kwargs.get('birth_place') and kwargs.get('gender'):
            self._ssn: str = self.update_ssn()

    def get_first_name(self) -> str:
        '''
        This method is used to get the variable first_name.

        Returns:
            str: self.first_name
        '''
        return self.first_name

    def get_last_name(self) -> str:
        '''
        This method is used to get the variable last_name.

        Returns:
            str: self.last_name
        '''
        return self.last_name

    def get_birth_date(self) -> str:
        '''
        This method is used to get the variable birth_date.
        If the variable is empty it returns None.
google.com
        Returns:
            str: self.birth_date
        '''
        return self.birth_date if self.birth_date else None

    def get_birth_place(self) -> str:
        '''
        This method is used to get the variable birth_place.
        If the variable is empty it returns None.

        Returns:
            str: self.birth_place
        '''
        return self.birth_place if self.birth_place else None

    def get_gender(self) -> str:
        '''
        This method is used to get the variable gender.
        If the variable is empty it returns None.

        Returns:
            str: self.gender
        '''
        return self.gender if self.gender else None

    def get_ssn(self) -> str:
        '''
        This method is used to get the variable _ssn.
        If the varial is empty it returns None.

        Returns:
            str: self._ssn
        '''
        return self._ssn

    def set_first_name(self, first_name: str) -> None:
        '''
        This method is used to change the variable first_name.

        Args:
            first_name (str): will replace self.first_name
        '''
        self.first_name = first_name
        self._ssn: str = self.update_ssn()

    def set_last_name(self, last_name: str) -> None:
        '''
        This method is used to change the variable last_name.

        Args:
            last_name (str): will replace self.last_name
        '''
        self.last_name = last_name
        self._ssn: str = self.update_ssn()

    def set_birth_date(self, birth_date: str) -> None:
        '''
        This method is used to change the variable birth_date.

        Args:
            birth_date (str): will replace self.birth_date
        '''
        self.birth_date = birth_date
        self._ssn: str = self.update_ssn()

    def set_birth_place(self, birth_place: str) -> None:
        '''
        This method is used to change the variable birth_place.

        Args:
            birth_place (str): will replace self.birth_place
        '''
        self.birth_place = birth_place
        self._ssn: str = self.update_ssn()

    def set_gender(self, gender: str) -> None:
        '''
        This method is used to change the variable gender.

        Args:
            gender (str): will replace self.gender
        '''
        self.gender = gender
        self._ssn: str = self.update_ssn()

    def update_ssn(self) -> str:
        '''
        This is used to calculate the ssn based on Codice Fiscale.
        It requires first_name, last_name, birth_date, birth_place and gender.
        '''
        # Check required variables
        if self.birth_date and self.birth_place and self.gender:
            _ssn: str
            # Dictionaries used to facilitate conversions
            mth_conv: dict = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"H",
                                7:"L",8:"M",9:"P",10:"R",11:"S",12:"T"}
            cadastral_codes: dict = {"Ancona":"A271","Aosta":"A326","L'Aquila":"A345","Roma":"H501",
                                     "Bologna":"A944","Cagliari":"B354","Campobasso":"B519",
                                     "Catanzaro":"C352","Firenze":"D612","Genova":"D969",
                                     "Milano":"F205","Napoli":"F839","Palermo":"G273","Bari":"A662",
                                     "Perugia":"G478","Potenza":"G942","Torino":"L219",
                                     "Trento":"L378","Trieste":"L424","Venezia":"L736"}
            odd_alphanumeric: dict = {"0":1,"1":0,"2":5,"3":7,"4":9,"5":13,"6":15,"7":17,"8":19,
                                      "9":21,"A":1,"B":0,"C":5,"D":7,"E":9,"F":13,"G":15,"H":17,
                                      "I":19,"J":21,"K":2,"L":4,"M":18,"N":20,"O":11,"P":3,"Q":6,
                                      "R":8,"S":12,"T":14,"U":16,"V":10,"W":22,"X":25,"Y":24,"Z":23}
            even_alphanumeric: dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,
                                      "9":9,"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,
                                      "J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,
                                      "S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
            alphanum_conv: dict = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",
                                   9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",
                                   18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}
            # Creation of list based on last_name with consonant first
            last_name: list = list(x.upper() for x in self.last_name)
            for x,_ in enumerate(last_name):
                last_name.append(last_name.pop(x)) if _ in ['A','E','I','O','U'] else None
            # Creation of list based on first_name with consonant first
            first_name: list = list(x.upper() for x in self.first_name)
            for x,_ in enumerate(first_name):
                first_name.append(first_name.pop(x)) if _ in ['A','E','I','O','U'] else None
            # Variables that have year, month and day of birth_date
            year: str = self.birth_date[-4:]
            month: int = int(self.birth_date[3:5])
            day: int = int(self.birth_date[:2])
            # If 'Femmina' add 40 to the day
            if self.gender[:1] == "F":
                day += 40
            # Find cadastral code from birth_place
            place: str = self.birth_place
            code: str = cadastral_codes[place.capitalize()]
            # Creation of ssn
            _ssn = ''.join(last_name[:3]) + ''.join(first_name[:3])
            _ssn = _ssn[:] + year[-2:] + mth_conv[month] + str(day) + code
            # Find control character
            addition: int = sum(odd_alphanumeric[y] for x,y in enumerate(list(_ssn)) if x%2 != 0)
            addition += sum(even_alphanumeric[y] for x,y in enumerate(list(_ssn)) if x%2 == 0)
            rem = addition%26
            last_char = alphanum_conv[rem]
            # Add control character to ssn
            _ssn = _ssn[:] + last_char
            return _ssn
        raise KeyError("Doesn't have all the information needed to calculate the ssn")

    def __str__(self) -> str:
        '''
        This method is used to return a full string with information about the Person.

        Returns:
            str: Variable string with information stored in the Person.
        '''
        cmt: str = f"{self.first_name} {self.last_name}"
        if self.gender:
            cmt += f", {self.gender}"
        if self.birth_date:
            cmt += f"\n{self.birth_date}"
        if self.birth_place:
            cmt += f"\n{self.birth_place}"
        if self._ssn:
            cmt += f"\n{self._ssn}"
        cmt += "\n"
        return cmt


person1: Person = Person("Luca", "Committeri",
                         birth_date= "21/04/2000", birth_place= "Roma", gender= "M")
person2: Person = Person("Marco", "Ciccia")
person3: Person = Person("Giacomo", "Palermitano",
                         birth_place= "Venezia") 
person4: Person = Person("Maria","Granula",
                         birth_date="09/07/1969", birth_place= "Palermo", gender= "F")
print(str(person1))
print(str(person2))
print(str(person3))
print(str(person4))
