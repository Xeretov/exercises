'''
Module provides a function that checks
if a given student and its votes has
an average of more than 60.

# Gioele Amendola
# 23/04/2024

# Create a function that takes a student's name and their scores in different subjects as input.
# The function calculates the average score and prints
# the student's name, average, and a message indicating whether the student
# passed the exam (average >= 60) or failed.
# Create a for loop to iterate over a list of students and scores,
# calling the function for each student.
'''

def average_score(scores: list) -> float:
    '''
    Calculates the average of a list

    Args:
        scores (list): list of votes

    Returns:
        float: average of the votes
    '''
    # Calculates the average given a list of numbers
    scores_sum: int = sum(scores)
    scores_average: float = scores_sum/len(scores)

    return scores_average


def check_student(student: str, scores: list):
    '''
    Prints the student, their average and if they passed the exam or not.

    Args:
        student (str): student
        scores (list): list of votes
    '''

    # Checks if average is above 60 and prints result
    average: float = average_score(scores)
    if average >= 60:
        print(f"{student}, {average}.\nThe student passed the exam.")
    else:
        print(f"{student}, {average}.\nThe student didn't pass the exam.")


# Example Test:
students_list: list = ['Gabriel',
                       'Gabriele',
                       'Giuseppe',
                       'Angelo']
grades_list: list = [[60, 55, 80, 60],
                     [100, 100, 70, 40],
                     [20, 50, 90, 55],
                     [60, 55, 45, 75]]

for i in enumerate(students_list):
    check_student(students_list[i], grades_list[i])
