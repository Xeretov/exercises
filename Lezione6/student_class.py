'''
This module contains the student class

Returns:
    Snimal: Class describing a student

# Gioele Amendola
# 13/05/2024

# Create a Class that represents a Student
# name, study_program, age, gender

# Define methods print_info that prints the attributes
'''

class Student:

    def __init__(self, name:str, study_program:str, age:int, gender:str) -> None:
        self.name: str = name
        self.study_program: str =  study_program
        self.age: int = age
        self.gender: str = gender
    
    def print_info(self) -> None:
        print(f"\nStudent: {self.name:<15}\tage: {self.age:<4}\tgender: {self.gender}\n",
              f"Program: {self.study_program}", sep="")

student1: Student = Student("Gioele Amendola", "Python", 24, "Male")
student2: Student = Student("Ricky Gervais", "Stand-up Comedy", 52, "Male")
student3: Student = Student("Giorgia", "Giorgia", 0, "Female")

lista: list = [student1,student2,student3]

for student in lista:
    student.print_info()