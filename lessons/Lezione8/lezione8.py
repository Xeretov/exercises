# Gioele Amendola
# 30/05/2025

from abc import ABC, abstractmethod
from turtle import title

# Exercise 1: Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter.
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    
    def area(self, radius: float) -> float:
        return 3.14 * radius**2
    
    def perimeter(self, radius: float) -> float:
        return 2*3.14 * radius

class Rectangle(Shape):
    
    def area(self, base: float, height: float) -> float:
        return base*height
    
    def perimeter(self, base: float, height: float) -> float:
        return base*2 + height*2

# Exercise 2: Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum,
# and another static method multiply that takes two numbers and returns their product.

class MathOperations:
    
    @staticmethod
    def add(num1: float, num2: float) -> float:
        return num1+num2
    
    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        return num1*num2


# Exercise 3: Library Management System 
# Create a Book class containing the following attributes: title, author, isbn
class Book:
    
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn

# The book class must contains the following methods:
# __str__ method to return a string representation of the book.
    def __str__(self) -> str:
        return f"{self.title} by {self.author} | isbn: {self.isbn}"

# @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn".
# It means that you must use the class reference cls to create a new object of the Book class using a string.
    @classmethod
    def from_string(cls, book_str: str):
        title: str
        author: str
        isbn: str
        title, author, isbn = map(str, book_str.split(', '))
        book: Book = Book(title, author, isbn)
        return book

# Example: 
# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 
# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666
book: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book)
print(str(divina_commedia))

# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:
class Member:
    
    def __init__(self, name: str, member_id: str) -> None:
        self.name: str = name
        self.member_id: str = member_id
        self.borrowed_books: list[Book] = []

# borrow_book(book) to add a book to the borrowed_books list.
    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)
        
# return_book(book) to remove a book from the borrowed_books list.
    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)

# __str__ method to return a string representation of the member.
    def __str__(self) -> str:
        return f"{self.member_id} | {self.name} has borrowed {self.borrowed_books if self.borrowed_books else 'nothing yet'}"
    
# @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".
    @classmethod
    def from_string(cls, member_str: str):
        name: str
        member_id: str
        name, member_id = map(str, member_str.split(", "))
        member: Member = Member(name, member_id)
        return member
    
# Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
# The library class must contain the following methods:
class Library:
    
    total_books: int = 0
    
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []

# add_book(book) to add a book to the library and increment total_books.
    def add_book(self, book: Book) -> None:
        self.books.append(book)
        Library.total_books += 1

# remove_book(book) to remove a book from the library and decrement total_books.
    def remove_book(self, book: Book) -> None:
        self.books.remove(book)
        Library.total_books -= 1

# register_member(member) to add a member to the library.
    def register_member(self, member: Member) -> None:
        self.members.append(member)
        
# lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.
    def lend_book(self, book: Book, member: Member) -> None:
        if book in self.books and member in self.members:
            member.borrow_book(book)
            self.remove_book(book)

# __str__ method to return a string representation of the library with the list of books and members.
    def __str__(self) -> str:
        return f"Books available:\n{self.books}\nMembers registered:\n{self.members}"
    
# @classmethod library_statistics(cls) to print the total number of books.
    @classmethod
    def library_statistics(cls) -> None:
        print(cls.total_books)

# Create a script and play a bit with the classes:
# Create instances of books and members using class methods.
# Register members and add books to the library.
# Lend books to members and display the state of the library before and after lending.
book = "The Communist Manifesto, Karl Marx, 555555555"
communist_manifesto: Book = Book.from_string(book)
book = "The Iliad and The Odyssey, Homer, 713713713"
iliad_and_the_odyssey: Book = Book.from_string(book)

member: str = "Angelo Carini, 666"
angelo: Member = Member.from_string(member)
member = "Francesco Totti, 10"
totti: Member = Member.from_string(member)

library: Library = Library()
library.add_book(divina_commedia)
library.add_book(communist_manifesto)
library.add_book(iliad_and_the_odyssey)

library.register_member(angelo)
library.register_member(totti)

library.library_statistics()
library.lend_book(communist_manifesto, angelo)
library.lend_book(divina_commedia, angelo)
library.library_statistics()

# Exercise 4: University Management System
# Create a system to manage a university with departments, courses, professors, and students. 
# Create an abstract class Person:
# Attributes:
# name (string)
# age (int)
class Person(ABC):
    
# __init__ method to initialize the attributes.
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        
# Abstract method get_role to be implemented by subclasses.
    @abstractmethod
    def get_role():
        pass
    
# __str__ method to return a string representation of the person.
    def __str__(self) -> str:
        return f"{self.name} is {self.age} old"

# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:
# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
class Student(Person):
    
    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id: str = student_id
        self.courses: list[Course] = []
    
    def enroll(self, course) -> None:
        self.courses.append(course)
        course.add_student(self)
    
    def get_role(self) -> None:
        return "student"
    
    def __str__(self) -> str:
        message: str = super().__str__()
        message += " and takes "
        message += ', '.join(course.course_name for course in self.courses)
        return message
    
# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.
class Professor(Person):
    
    def __init__(self, name: str, age: int, professor_id: str) -> None:
        super().__init__(name, age)
        self.professor_id: str = professor_id
        self.department: Department = None
        self.courses: list[Course] = []
    
    def assign_to_course(self, course) -> None:
        self.courses.append(course)
        course.set_professor(self)
    
    def get_role(self) -> str:
        return f"professor at {self.department.department_name}"

# Create a class Course:
# Attributes:
# course_name (string)
# course_code (string)
# students (list of Student instances)
# professor (Professor instance)
class Course:
    
    # __init__ method to initialize the attributes.
    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name: str = course_name
        self.course_code: str = course_code
        self.students: list[Student] = []
        self.professor: Professor = None
    
    # add_student(student) to add a student to the course.
    def add_student(self, student: Student) -> None:
        self.students.append(student)
    
    # set_professor(professor) to set the professor for the course.
    def set_professor(self, professor: Professor) -> None:
        self.professor = professor
    
    # __str__ method to return a string representation of the course.
    def __str__(self) -> str:
        message: str = f"{self.course_code} | {self.course_name} taught by {self.professor.name}"
        message += "\nStudents:\n"
        message += ', '.join(student.name for student in self.students)
        message += "\n"
        return message

# Create a class Department:
class Department:
    
# Attributes:
# department_name (string)
# courses (list of Course instances)
# professors (list of Professor instances)
# __init__ method to initialize the attributes.
    def __init__(self, department_name: str) -> None:
        self.department_name: str = department_name
        self.courses: list[Course] = []
        self.professors: list[Professor] = []
        
# add_course(course) to add a course to the department.
    def add_course(self, course: Course) -> None:
        self.courses.append(course)

# add_professor(professor) to add a professor to the department.
    def add_professor(self, professor: Professor) -> None:
        self.professors.append(professor)
        professor.department = self

# __str__ method to return a string representation of the department.
    def __str__(self) -> str:
        message: str = f"\n{self.department_name.capitalize()} courses:\n\n"
        message += '\n'.join(str(course) for course in self.courses)
        message += "\nprofessors:\n"
        message += '\n'.join(str(professor) for professor in self.professors)
        return message

# Create a class University:
class University:
    
# Attributes:
# name (string)
# departments (list of Department instances)
# students (list of Student instances)
# __init__ method to initialize the attributes.
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.departments: list[Department] = []
        self.students: list[Student] = []
        
# add_department(department) to add a department to the university.
    def add_department(self, department: Department) -> None:
        self.departments.append(department)
        
# add_student(student) to add a student to the university.
    def add_student(self, student: Student) -> None:
        self.students.append(student)
        
# __str__ method to return a string representation of the university.
    def __str__(self) -> str:
        message: str = f"\n{self.name.capitalize()} University\n\nDepartments:\n"
        message += '\n'.join(str(department) for department in self.departments)
        message += "\n\nStudents:\n"
        message += '\n'.join(str(student) for student in self.students)
        message += "\n"
        return message

# Create a script:
# Create instances of departments, courses, professors, and students.
physics: Department = Department("physics")
engineering: Department = Department("engineering")
science: Department = Department("science and technology")

quantum: Course = Course("quantum physics", "p001")
relativity: Course = Course("relativity", "p002")
astro: Course = Course("astrophysics", "p003")
aerospace: Course = Course("aerospace engineering", "e001")
computer: Course = Course("computer engineering", "e002")
bio: Course = Course("bioengineering", "e003")
chem: Course = Course("chemistry", "s001")
math: Course = Course("mathematics", "s002")
geology: Course = Course("geology", "s003")

lupin: Professor = Professor("Remus Lupin", 38, "hgw001")
hagrid: Professor = Professor("Rubeus Hagrid", 54, "hgw002")
snape: Professor = Professor("Severus Snape", 38, "hgw003")
dyer: Professor = Professor("William Dyer", 33, "hpl0v3")
kirke: Professor = Professor("Digory Kirke", 61, "csl3w1s")
otto: Professor = Professor("Otto Liedenbrock", 42, "v3rn3")
moriarty: Professor = Professor("James Moriarty", 70, "c0n4nd0yl3")
langdon: Professor = Professor("Robert Langdon", 47, "t0mh4nk5")
keating: Professor = Professor("John Keating", 32, "d34dp03t5")

alfred: Student = Student("Alfred Hutheesing", 20, "std001")
freedon: Student = Student("Freedon Annunziato", 21, "std002")
alan: Student = Student("Alan Tucker", 19, "std003")
jenny: Student = Student("Jenny Coleman", 20, "std004")
yvonne: Student = Student("Yvonne William", 20, "std005")
eric: Student = Student("Eric Da Silva", 22, "std006")

# Add them to the university.
hailsmith: University = University("hailsmith")

# Enroll students in courses and assign professors to courses.
alfred.enroll(quantum)
alfred.enroll(computer)
alfred.enroll(math)
freedon.enroll(bio)
freedon.enroll(chem)
freedon.enroll(math)
alan.enroll(quantum)
alan.enroll(relativity)
jenny.enroll(bio)
jenny.enroll(geology)
jenny.enroll(astro)
yvonne.enroll(aerospace)
yvonne.enroll(astro)
yvonne.enroll(relativity)
eric.enroll(computer)
eric.enroll(quantum)
eric.enroll(math)

snape.assign_to_course(math)
lupin.assign_to_course(astro)
hagrid.assign_to_course(bio)
dyer.assign_to_course(relativity)
kirke.assign_to_course(chem)
moriarty.assign_to_course(quantum)
otto.assign_to_course(geology)
langdon.assign_to_course(computer)
keating.assign_to_course(aerospace)

physics.add_course(quantum)
physics.add_course(relativity)
physics.add_course(astro)
engineering.add_course(bio)
engineering.add_course(aerospace)
engineering.add_course(computer)
science.add_course(chem)
science.add_course(math)
science.add_course(geology)

physics.add_professor(dyer)
physics.add_professor(moriarty)
physics.add_professor(lupin)
engineering.add_professor(hagrid)
engineering.add_professor(keating)
engineering.add_professor(langdon)
science.add_professor(snape)
science.add_professor(kirke)
science.add_professor(otto)

hailsmith.add_department(physics)
hailsmith.add_department(engineering)
hailsmith.add_department(science)
hailsmith.add_student(alfred)
hailsmith.add_student(yvonne)
hailsmith.add_student(eric)
hailsmith.add_student(freedon)
hailsmith.add_student(alan)
hailsmith.add_student(jenny)

# Display the state of the university.
print(str(hailsmith))
