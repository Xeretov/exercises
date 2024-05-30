'''
Module provides a function that searches for words in a grid
and returns its starting and ending points.

# Gioele Amendola
# 01/05/2024

# Create a function that solves a word search puzzle.
# Provide a 2D grid representing the puzzle and a list of words to find.
# Implement a backtracking algorithm to search for the words in the grid,
# marking visited cells to avoid repetition.
# Output the locations of the found words within the grid.

# The grid is a list of lists filled with chars (every row is the same size)

# The function takes as parameters the grid and a list or set of words to search for in the grid
# Once the words are found returns a dictionary
# The returned dictionary will have a list of starting points and a list of lists of ending points
# The index of the starting points correspond to the list of ending points
# example:  word_index['piccolo']['start'][0] is a tuple of the starting points
#           word_index['piccolo']['end'][0] is a list of tuples of the ending points
# The ending points will always be added in order (right,down,left,up)
'''
# NEEDS REDO
def word_search(grid: list[list[str]], words: list | set) -> dict:
    '''
    Main function to call. It will iter inside the grid to find every possible
    combination of chars that will equal to the list of words.

    Args:
        grid (list): characters grid.
        words (list | set): words that needs to be searched inside the grid.

    Raises:
        ValueError: grid isn't a n*n grid
        ValueError: grid isn't a grid full of str
        ValueError: grid contains str longer than 1 char
        ValueError: words contains more than strings
        ValueError: words contains non alphabetical strings

    Returns:
        dict: dictionary that has the name of the word
        its starting point and its ending points.
    '''

    # Transform words list in set
    if not isinstance(words, set):
        words = set(words)

    # Check if grid has every row with same size
    it = iter(grid)
    default_len = len(next(it))  # takes lenght of first row
    # check if the other rows are same lenght of the first one
    if not all(len(l) == default_len for l in it):
        raise ValueError('grid doesn\'t have rows with same size.')

    # Check if grid has only char and is not a string
    for sublist in grid:
        for char in sublist:
            if not isinstance(char, type(grid[0][0])):
                raise ValueError('grid contains types other than string.')
            if len(char) > 1:
                raise ValueError(
                    'grid contains strings longer than one character.')

    # Check if words has only alphabetic strings
    for word in words:
        if not isinstance(word, str):
            raise ValueError('words list contains types other than string.')
        if not word.isalpha():
            raise ValueError('words list contains non alphabetic strings')

    # Lower case grid list and word list
    grid = [[x.lower() for x in sublist] for sublist in grid]
    words = [word.lower() for word in words]

    # Word_index is to store the index found
    # row is the 'height' of the grid (x)
    # column is the 'length' of the grid (y)
    word_index: dict = {word: [] for word in words}
    row: int = len(grid)
    column: int = len(grid[0])

    # Adds the index starting point for every first character of the words given in word_index
    for word in words:
        if len(word) > row and len(word) > column:
            continue
        char: str = word[:1]
        for x in range(row):
            for y in range(column):
                if char == grid[x][y]:
                    word_index[word].append([(x, y)])

    check(grid, word_index, row, column)

    # Deletion of starting index without ending index in word_index
    for word in word_index:
        j: int = 0
        for _ in range(len(word_index[word])):
            if j >= len(word_index[word]):
                break
            if word_index[word]:
                if len(word_index[word][j]) < 2:
                    del word_index[word][j]
                else:
                    j += 1

    # Creation of a dictionary of a dictionary
    # Adds words that have a starting and ending index to the dictionary
    dictionary: dict = {word: {'start': list, 'end': list}
                        for word in word_index if word_index[word]}
    for word in dictionary:
        # Adds the starting point and the ending point to the dictionary
        dictionary[word]['start'] = [word_index[word][i][0]
                                     for i in range(len(word_index[word]))]
        dictionary[word]['end'] = [word_index[word][i][1:]
                                   for i in range(len(word_index[word]))]
    dictionary = dict(sorted(dictionary.items()))

    # Check if word is palindrome (duplicated coordinates)
    to_delete: list = []
    for word in dictionary:
        if word == word[::-1]:
            start_list: list = dictionary[word]['start']
            end_list: list = dictionary[word]['end']
            print(start_list,end_list)
            for start_coordinates in start_list:
                for i,end_coordinates_list in enumerate(end_list):
                    for end_coordinates in end_coordinates_list:
                        if start_coordinates == end_coordinates:
                            print(i,start_list[i],end_coordinates)
                            if [end_coordinates,start_list[i]] not in to_delete:
                                to_delete.append([start_list[i],end_coordinates])
    # Delete found coordinates
    for word in dictionary:
        for tuples in to_delete:
            if tuples[0] in dictionary[word]['start']:
                for _ in range(len(dictionary[word]['end'])):
                    for i in range(len(dictionary[word]['end'][_])):
                        if tuples[1] == dictionary[word]['end'][_][i]:
                            del dictionary[word]['end'][_][i]
                        if not dictionary[word]['end'][_]:
                            del dictionary[word]['start'][_]
        
    # Ask for printing result
    # Shows the 2D grid and the words that have a starting and ending point
    while True:
        try:
            choose: str = input("Do you want to print the result? (Y/n) ")
            if choose in ['Y', 'n']:
                if choose == 'Y':
                    print_grid_result(grid, dictionary)
                break
        except ValueError:
            continue

    return dictionary


def check(grid: list[list[str]], words: dict, row: int, col: int) -> dict:
    '''
    Checks in every direction for the word in grid

    Args:
        grid (list[list[str]]): characters grid.
        words (dict): word starting and ending points.
        row (int): grid row
        col (int): grid column

    Returns:
        dict: words indexes
    '''
    right: int = 0
    down: int = 0
    left: int = 0
    up: int = 0
    for word in words.keys():
        # If word has starting point
        if words[word]:
            # Takes index starting point (pos)
            for pos in words[word]:
                # x = row, y = column
                x = pos[0][0]
                y = pos[0][1]
                right, down, left, up = y, x, y, x
                # Matches every character of a word in every direction
                # Right,down,left,up are counters to see if there are matches in those directions
                # If there isn't space for the word to be in the grid they take '-inf' as value
                # If there isn't a match they take '-inf' as value
                # If the word is found in the grid, the ending point is added to the word_index
                for char in word[1:]:
                    if right != '-inf':
                        if right+1 < col and col-len(word) >= 0:
                            if char == grid[x][right+1]:
                                right += 1
                                if right-y == len(word)-1:
                                    pos.append((x, right))
                                    right = '-inf'
                            else:
                                right = '-inf'
                        else:
                            right = '-inf'
                    if down != '-inf':
                        if down+1 < row and row-len(word) >= 0:
                            if char == grid[down+1][y]:
                                down += 1
                                if down-x == len(word)-1:
                                    pos.append((down, y))
                                    down = '-inf'
                            else:
                                down = '-inf'
                        else:
                            down = '-inf'
                    if left != '-inf':
                        if left-1 >= 0 and col-len(word) >= 0:
                            if char == grid[x][left-1]:
                                left -= 1
                                if y-left == len(word)-1:
                                    pos.append((x, left))
                                    left = '-inf'
                            else:
                                left = '-inf'
                        else:
                            left = '-inf'
                    if up != '-inf':
                        if up-1 >= 0 and row-len(word) >= 0:
                            if char == grid[up-1][y]:
                                up -= 1
                                if x-up == len(word)-1:
                                    pos.append((up, y))
                                    up = '-inf'
                            else:
                                up = '-inf'
                        else:
                            up = '-inf'
                    if not [x for x in (right, down, left, up) if x == '-inf']:
                        break

def print_grid_result(grid: list[list[str]], dictionary: dict):
    '''
    This function prints the result of the word search

    Args:
        grid (list[list[str]]): characters grid
        dictionary (dict): dictionary of words found in the grid and their coordinates
    '''
    print("\n\\ y\nx",end=" ")
    for x in grid:
        print(*x,end="\n  ")
    keys: list = dictionary.keys()
    print(f"\n{'WORDS':^15}{'START':^10}{'END':^20}")
    for key in keys:
        j: int = 0
        for x in dictionary[key]['start']:
            for y in range(len(x)-1):
                print(f"{key:<15}{str(dictionary[key]['start'][j]):<10}",
                        f"{str(dictionary[key]['end'][j]):<20}")
                j += 1

# Example test:
word_grid: list = [
    ['a', 'l', 'i', 't', 'o', 's', 'i'],
    ['l', 'i', 'l', 'u', 'r', 'p', 'i'],
    ['p', 'e', 'z', 'o', 'a', 'f', 'l'],
    ['f', 'a', 'e', 'n', 'p', 'a', 'l'],
    ['g', 'e', 'e', 'o', 'r', 't', 'o'],
    ['o', 'r', 'o', 'r', 't', 'o', 'n']]

word_search(word_grid, ['alitosi', 'ululato', 'illuminato',
            'zebra', 'il', 'TUOno', 'orto', 'ora', 'apnea',
            'oro'])
