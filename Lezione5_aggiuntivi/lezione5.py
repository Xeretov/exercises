# Gioele Amendola
# 08/05/2024

# 1. Two Sum
# Given a list of integers and a target sum,
# find all unique pairs of integers within the list that sum up to the target.

integers: list[int] = [x for x in range(100)]
target = 48
pairs: list[tuple] = []
for i in range(len(integers)-1):
    for j in range(i,len(integers)):
        pairs.append((integers[i],integers[j])) if integers[i]+integers[j] == target else None
print(pairs,end="\n\n")

# 2. Longest Increasing Subsequence
# Given a list of integers, find the length
# of the longest increasing subsequence within the list.
# An increasing subsequence is a sequence of elements
# from the array where each element is greater than or equal to the previous element.

integers2: list[int] = [2,6,1,23,2,41,4,65,64,7,4,34,23,25,45,567,67,5,45,5,24,52,6,54,6,456,4,25,25]
length: int = sum(1 for i in range(1,len(integers2)) if integers2[i] >= integers2[i-1])
print(length,end="\n\n")

# 3. Longest Common Subsequence
# Given two strings, find the length of the longest common subsequence (LCS) between them.
# An LCS is a subsequence of one string that is also a subsequence
# of the other string while maintaining the relative order of elements.

string1: str = "Romanieraman"
string2: str = "arormmaniero"
lcs: set = set()
sub: str = ""
list1: list = list(string1.lower())
list2: list = list(string2.lower())
j: int = 0
for j in range(len(list2)):
    found: bool = False
    start: int = j
    i: int = 0
    while True:
        if i >= len(list1) or j >= len(list2):
            break
        if list2[j] == list1[i]:
            sub += list2[j]
            j += 1
            found = True
        elif found:
            j = start
            found = False
            lcs.add(sub)
            sub = ""
            continue
        i += 1
    if sub:
        lcs.add(sub)
    sub = ""

lengths: list = [len(string) for string in lcs]
print(max(lengths),end="\n\n")

# 4. Word Break Problem:
# Given a string and a dictionary of words,
# determine whether the string can be segmented into a space-separated sequence
# of one or more dictionary words.
# Each word in the dictionary must be a contiguous substring of the input string.


# 5. Longest Palindrome Subsequence:
# A palindrome is a word, phrase, or sequence that reads
# the same backwards as forward. Given a string,
# the task is to find the longest palindrome subsequence within the string.
# A subsequence is obtained from a string by deleting zero
# or more elements without changing the order of the remaining elements.

# 6. Armstrong Number Checker:
# Develop a function to check if a given number is an Armstrong number
# (the sum of its digits raised to the power of the number of digits equals the number itself).

# 7. Merge Two Sorted Lists: 
# Implement a function to merge two sorted lists into a single sorted list.

# 8. Find the Most Frequent Element:
# Create a function that finds the element that appears most frequently in a given list.

# 9. Find the Second Largest Element in an Array:
# Implement a function to find the second largest element in an unsorted list without using sorting algorithms.

# 10. Find the Intersection of Two Sorted Arrays:
# Implement a function to find the elements that are present in both of the two sorted lists.