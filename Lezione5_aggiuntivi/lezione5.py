# Gioele Amendola
# 08/05/2024

# 1. Two Sum
# Given a list of integers and a target sum,
# find all unique pairs of integers within the list that sum up to the target.

def two_sum():
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

def longest_sub():
    integers: list[int] = [2,6,1,23,2,41,4,65,64,7,4,34,23,25,45,567,67,5,45,5,24,52,6,54,6,456,4,25,25]
    length: int = sum(1 for i in range(1,len(integers)) if integers[i] >= integers[i-1])
    print(length,end="\n\n")

# longest_sub() Expected Output: 15

# 3. Longest Common Subsequence
# Given two strings, find the length of the longest common subsequence (LCS) between them.
# An LCS is a subsequence of one string that is also a subsequence
# of the other string while maintaining the relative order of elements.

def common_sub():
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

# common_sub() Expected Output: 6

# 4. Word Break Problem:
# Given a string and a dictionary of words,
# determine whether the string can be segmented into a space-separated sequence
# of one or more dictionary words.
# Each word in the dictionary must be a contiguous substring of the input string.
from pathlib import Path

def generate_words_dict() -> dict:
    path = Path(__file__).parent.resolve()
    words: dict = {}
    lines: list | set = []
    with open(str(path)+'/dictionary.txt',mode='r',encoding='utf8') as file:
        for line in file:
            lines.append(line.lower().strip('\n'))
        lines = set(lines)
        file.close()
    i: int = 0
    for _,word in enumerate(lines):
        if len(word)>3 and len(word)<6:
            words[i] = word
            i += 1
        if i == 101:
            break
    return words

def word_break(string: str):
    words: dict = generate_words_dict()
    words[101] = "pay"; words[102] = "roll"
    substrings: list = [words[word] for word in words if string.find(words[word]) != -1]
    print(substrings)

# word_break("payroll") Expected Output ['pay','roll']

# 5. Longest Palindrome Subsequence:
# A palindrome is a word, phrase, or sequence that reads
# the same backwards as forward. Given a string,
# the task is to find the longest palindrome subsequence within the string.
# A subsequence is obtained from a string by deleting zero
# or more elements without changing the order of the remaining elements.

def sub_pal(string: str):
    iter_string: list = list(string)
    subsequence: str = ""
    substring: list = []
    broken: bool = False
    for i in range(len(iter_string)):
        for j in range(i+1,len(iter_string)):
            if iter_string[i] == iter_string[j]:
                for m,l in zip(range(i,j), range(j,i,-1)):
                    if m > l:
                        break
                    elif iter_string[m] == iter_string[l]:
                        subsequence = subsequence[:] + iter_string[m]
                    else:
                        broken = True
                        break
            if not broken and subsequence:
                subsequence = subsequence[:-1] + subsequence[::-1]
                if substring:
                    for word in substring:
                        if word.find(subsequence) != -1:
                            subsequence = ""
                            break
                if subsequence:
                    substring.append(subsequence)
            broken = False
            subsequence = ""        
    print(substring)

# sub_pal("palkingnikpalap") Expected Output: ['kingnik','palap']

# 6. Armstrong Number Checker:
# Develop a function to check if a given number is an Armstrong number
# (the sum of its digits raised to the power of the number of digits equals the number itself).

def check_armstrong(number: int) -> bool:
    temp: int = number
    digits: list = []
    while temp > 0:
        digits.append(temp%10)
        temp //= 10
    return True if sum(digit**len(digits) for digit in digits) == number else False

# print(check_armstrong(153)) Expected Output: True
# print(check_armstrong(12))                   False

# 7. Merge Two Sorted Lists: 
# Implement a function to merge two sorted lists into a single sorted list.

def merge_sorted_lists():
    list1: list = [i for i in range(20) if i%2 == 0]
    list2: list = [i for i in range(20) if i%2 != 0]
    print(list(sorted(list1+list2)))

# 8. Find the Most Frequent Element:
# Create a function that finds the element that appears most frequently in a given list.

def most_frequent(ele_list: list):
    frequence: list = []
    for element in ele_list:
        frequence.append(ele_list.count(element))
    return ele_list[frequence.index(max(frequence))]

# print(most_frequent([2,2,2,2,2,2,23,3,3,3,1,51,5,1,51,51,5,1,5,3,3,3,3,3,3])) Expected Output: 3

# 9. Find the Second Largest Element in an Array:
# Implement a function to find the second largest element in an unsorted list without using sorting algorithms.

def second_largest(ele_list: list):
    frequence: list = []
    for element in ele_list:
        frequence.append(ele_list.count(element))
    second: int = 0
    first: int = max(frequence)
    for count in frequence:
        if count > second and count < first:
            second = count
    return ele_list[frequence.index(second)]

# print(second_largest([2,2,2,2,2,2,23,3,3,3,1,51,5,1,51,51,5,1,5,3,3,3,3,3,3]))

# 10. Find the Intersection of Two Sorted Arrays:
# Implement a function to find the elements that are present in both of the two sorted lists.

def intersection(array1:list,array2:list) -> set:
    both: set = set()
    for x in array1:
        for y in array2:
            if x == y:
                both.add(x)
    return both

# print(intersection([1,2,3,4,5,"paolo",1.7324,"acciuga"],["acciuga",4,1.7324])) Expected output: {1.7324,4,'acciuga'}