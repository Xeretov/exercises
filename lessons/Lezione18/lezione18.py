import math
import string

def safe_sqrt(number: float) -> float:
    try:
        math.sqrt(number)
    except ValueError:
        print("Cannot return the square root of a negative number")

safe_sqrt(4)
safe_sqrt(-6)

class InvalidPasswordError(Exception):
    pass

def validate_password(password: str) -> bool:
    if len(password) < 20:
        raise InvalidPasswordError
    uppercase: str = string.ascii_uppercase
    specialchar: str = "[@_!#$%^&*()<>?/\|}{~:]"
    countup: int = 0
    countsp: int = 0
    for char in password:
        if char in uppercase:
            countup += 1
        elif char in specialchar:
            countsp += 1
    if countup < 3 or countsp < 4:
        raise InvalidPasswordError
    return True

validate_password("A!menoUnC@cc@$lmjklm")
validate_password("Ahaheah")

try:
    with open("terminal_codes.py", 'r') as f:
        pass
except IOError:
    print("Something went wrong when handling the file")

class Date:
    
    def __init__(self, day: str, month: str, year: str) -> None:
        self.day = None
        self.month = None
        self.year = None
    
    @classmethod
    def from_int(cls, day: int, month: int, year: int) -> 'Date':
        date: Date = Date(str(day), str(month), str(year))
        return date
    
    @classmethod
    def from_str(cls, string: str) -> 'Date':
        '''
        string format must be "gg.mm.yyyy"
        '''
        day: str; month: str; year: str
        day, moth, year = map(str, string.split('.'))
        date: Date = Date(day, month, year)
        return date
    
    def __eq__(self, otherDate: 'Date') -> bool:
        return self.day == otherDate.day and self.month == otherDate.month and self.year == otherDate.year:
    

class DataBase:
    
    def __init__(self) -> None:
        self.date_list: list[Date] = []
    
    def add_date(self, new_date: Date) -> None:
        if new_date not in self.date_list:
            self.date_list.append(new_date)
        else:
            print("Date already added")
    
    def remove_date(self, date: Date) -> None:
        if date in self.date_list:
            self.date_list.remove(date)
        else:
            print("There is no date that corresponds")
    
    def query_date(self, day: str = None, month: str = None, year: str) -> list['Date']:
        result: list[Date] = []
        for date in self.date_list:
            add: bool = True
            if date.year != year:
                add = False
            if date.month != month and month:
                add = False
            if date.day != day and day:
                add = False
            if add:
                result.append(date)
        return result


        
'''
An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
 If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
If the second input is not '+' or '-', again raise a FormulaError.
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. The library must include functions for the following operations:
Create a fraction from the numerator and denominator.
Collect the numerator and denominator of a fraction.
Simplify a fraction.
Add, subtract, multiply and divide fractions.
Check whether one fraction is equivalent to another. 
All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user.

 Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error).
 '''