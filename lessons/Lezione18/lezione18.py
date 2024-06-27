import math
import string
#from modules import terminal_codes as tc

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
try:
    validate_password("A!menoUnC@cc@$lmjklm")
    validate_password("Ahaheah")
except InvalidPasswordError as e:
    print(e)

try:
    with open("terminal_codes.py", 'r') as f:
        pass
except IOError:
    print("Something went wrong when handling the file")

class Date:
    
    def __init__(self, day: str, month: str, year: str) -> None:
        self.day: str = day
        self.month: str = month
        self.year: str = year
    
    @classmethod
    def from_int(cls, day: int, month: int, year: int) -> 'Date':
        if 1>month>12:
            raise ValueError("Month not valid")
        if 1>day>31 or (day>28 and month == 2) or (day>29 and month == 2 and year%4 == 0) or (day>30 and month in [4, 6, 9, 11]):
            raise ValueError("Day not valid")
        date: Date = Date(str(day), str(month), str(year))
        return date
    
    @classmethod
    def from_str(cls, string: str) -> 'Date':
        '''
        string format must be "gg.mm.yyyy"
        '''
        day: int; month: int; year: int
        day, moth, year = map(int, string.split('.'))
        if 1>month>12:
            raise ValueError("Month not valid")
        if 1>day>31 or (day>28 and month == 2) or (day>29 and month == 2 and year%4 == 0) or (day>30 and month in [4, 6, 9, 11]):
            raise ValueError("Day not valid")
        date: Date = Date(str(day), str(month), str(year))
        return date
    
    def __eq__(self, otherDate: 'Date') -> bool:
        return self.day == otherDate.day and self.month == otherDate.month and self.year == otherDate.years

    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

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
    
    def query_date(self, day: int = None, month: int = None, year: int = None) -> list['Date']:
        if not self.date_list:
            raise ValueError("There is nothing stored in this database")
        if all(v is None for v in [day, month, year]):
            raise ValueError("At least one paramter must be specified")
        if month:
            if 1>month>12:
                raise ValueError("Month not valid")
        if day:
            if 1>day>31 or (day>28 and month == 2) or (day>29 and month == 2 and year%4 == 0) or (day>30 and month in [4, 6, 9, 11]):
                raise ValueError("Day not valid")
        result: list[Date] = []
        for date in self.date_list:
            add: bool = True
            if date.year != str(year) and year:
                add = False
            if date.month != str(month) and month:
                add = False
            if date.day != str(day) and day:
                add = False
            if add:
                result.append(date)
        return result


class FormulaError(Exception):
    pass

def calculator():
    while True:
        string: str = input("Insert Formula (or 'exit' to exit) > ")
#        tc.delete_lines()
        if string == 'exit':
            return
        num1, op, num2 = string.split()
        try:
            num1, num2 = float(num1), float(num2)
        except:
            raise FormulaError("Inserted input not Valid")
        if op not in ['+','-','/',':','*','x','%','**','^','root']:
            raise FormulaError("Inserted input not Valid")
        result: float
        if op in ['*','x']:
            result = num1*num2
        elif op == '+':
            result = num1+num2
        elif op == '-':
            result = num1-num2
        elif op == ['/',':']:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1/num2
        elif op == '%':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1%num2
        elif op in ['^','**']:
            result = num1**num2
        elif op == 'root':
            if num2 < 0:
                raise FormulaError("No negative number for x")
            if num1 == 0:
                raise FormulaError("No zero for nth root")
            result = num2**(1/num1)
        print(f"{num1} {op} {num2} = {result}")
        
class denominatorError(Exception):
    pass
        
class fractionStructureError(Exception):
    pass

class fractions:
        
    @staticmethod
    def simplify(num: int, den: int) -> int:
        '''
        simplify numerator and denominator of a fraction
        '''
        if any(x < 2 for x in [num,den]):
            return num, den
        minim: int = min(num, den)
        for i in range(minim, 1, -1):
            if num % i == 0 and den % i == 0:
                num //= i
                den //= i
        return num, den

    @staticmethod
    def find_nums(string: str) -> int:
        try:
            num, den = map(int, string.split('/'))
        except:
            raise fractionStructureError(f"String inserted '{string}' isn't a fraction")
        return num, den
        
    @staticmethod
    def greatest_common_fact(a: int, b: int) -> int:
        if a == 0:
            return b
        return fractions.greatest_common_fact(b % a, b)
        
    @staticmethod
    def least_common_den(a: int, b: int) -> int:
        return (a * b) / fractions.greatest_common_fact(a, b)
    
    @staticmethod
    def add(string1: str, string2: str, formula: bool = False) -> str:
        '''
        Addition between fractions (example: add('3/4', '6/3'))

        formula (optional): if True gives back entire operation instead of the result
        '''
        num1, den1 = fractions.find_nums(string1)
        num2, den2 = fractions.find_nums(string2)
        if den1 == 0 or den2 == 0:
            raise denominatorError("denominator is 0")
        num1, den2 = fractions.simplify(num1, den2)
        num2, den1 = fractions.simplify(num2, den1)
        num1, den1 = fractions.simplify(num1, den1)
        num2, den2 = fractions.simplify(num2, den2)
        den: int = fractions.least_common_den(den1, den2)
        op1: int = (den//den1) * num1
        op2: int = (den//den2) * num2
        if formula:
            return f"{string1} + {string2} = {op1+op2}/{den}"
        return f"{op1+op2}/{den}"

    @staticmethod
    def sub(string1: str, string2: str, formula: bool = False) -> str:
        '''
        Subtraction between fractions (example: sub('3/4', '6/3'))

        formula (optional): if True gives back entire operation instead of the result
        '''
        num1, den1 = fractions.find_nums(string1)
        num2, den2 = fractions.find_nums(string2)
        if den1 == 0 or den2 == 0:
            raise denominatorError("denominator is 0")
        num1, den2 = fractions.simplify(num1, den2)
        num2, den1 = fractions.simplify(num2, den1)
        num1, den1 = fractions.simplify(num1, den1)
        num2, den2 = fractions.simplify(num2, den2)
        den: int = fractions.least_common_den(den1, den2)
        op1: int = (den//den1) * num1
        op2: int = (den//den2) * num2
        if formula:
            return f"{string1} - {string2} = {op1-op2}/{den}"
        return f"{op1-op2}/{den}"

    @staticmethod
    def mul(string1: str, string2: str, formula: bool = False) -> str:
        '''
        Multiplication between fractions (example: mul('3/4', '6/3'))
        
        formula (optional): if True gives back entire operation instead of the result
        '''
        num1, den1 = fractions.find_nums(string1)
        num2, den2 = fractions.find_nums(string2)
        if den1 == 0 or den2 == 0:
            raise denominatorError("denominator is 0")
        num1, den2 = fractions.simplify(num1, den2)
        num2, den1 = fractions.simplify(num2, den1)
        num1, den1 = fractions.simplify(num1, den1)
        num2, den2 = fractions.simplify(num2, den2)
        num = num1 * num2
        den = den1 * den2
        num, den = fractions.simplify(num, den)
        if formula:
            return f"{string1} * {string2} = {num}/{den}"
        return f"{num}/{den}"

    @staticmethod
    def div(string1: str, string2: str, formula: bool = False) -> str:
        '''
        Division between fractions (example: div('3/4', '6/3'))
        
        formula (optional): if True gives back entire operation instead of the result
        '''
        num1, den1 = fractions.find_nums(string1)
        num2, den2 = fractions.find_nums(string2)
        if num2 == 0:
            if formula:
                return f"{string1} / {string2} = 1"
            return "1"
        if den1 == 0 or den2 == 0:
            raise denominatorError("denominator is 0")
        num2, den2 = den2, num2
        num1, den2 = fractions.simplify(num1, den2)
        num2, den1 = fractions.simplify(num2, den1)
        num1, den1 = fractions.simplify(num1, den1)
        num2, den2 = fractions.simplify(num2, den2)
        num = num1 * num2
        den = den1 * den2
        num, den = fractions.simplify(num, den)
        if formula:
            return f"{string1} / {string2} = {num}/{den}"
        return f"{num}/{den}"
        
    @staticmethod
    def eq(string1: str, string2: str) -> bool:
        '''
        Check if two fractions are equal to eachother
        '''
        num1, den1 = fractions.find_nums(string1)
        num2, den2 = fractions.find_nums(string2)
        num1, den1 = fractions.simplify(num1, den1)
        num2, den2 = fractions.simplify(num2, den2)

        if num1 == num2 and den1 == den2:
            return True
        return False


print("\n\n")
class DataStructureIntegrityError(Exception):
    """Raised when the data structure's integrity is compromised"""
    pass

# Define the custom linked list data structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def remove(self, value):
        if not self.head:
            raise DataStructureIntegrityError("Cannot remove from an empty list")
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        raise DataStructureIntegrityError("Value not found in the list")

    def access(self, index):
        if not self.head:
            raise DataStructureIntegrityError("Cannot access an empty list")
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        raise DataStructureIntegrityError("Index out of range")

# Functions that operate on the linked list
def print_list(linked_list):
    current = linked_list.head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

def reverse_list(linked_list):
    previous = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    linked_list.head = previous

def is_ordered(linked_list):
    current = linked_list.head
    previous_value = None
    while current:
        if previous_value and current.value < previous_value:
            return False
        previous_value = current.value
        current = current.next
    return True

# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print_list(linked_list)  # Output: 1 2 3 4 5

reverse_list(linked_list)
print_list(linked_list)  # Output: 5 4 3 2 1

print(is_ordered(linked_list))  # Output: False

reverse_list(linked_list)
print(is_ordered(linked_list)) # Output: True

try:
    linked_list.access(5)
except DataStructureIntegrityError as e:
    print(e)  # Output: Index out of range

try:
    linked_list.remove(6)
except DataStructureIntegrityError as e:
    print(e)  # Output: Value not found in the list

print()