# Gioele Amendola
# 01/05/2024

# Create a function that solves a word search puzzle. 
# Provide a 2D grid representing the puzzle and a list of words to find.
# Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
# Output the locations of the found words within the grid.

# The grid is a list of lists filled with chars (every row is the same size)

# The function takes as parameters the grid and a list or set of words to search for in the grid
# Once the words are found returns a dictionary
# The returned dictionary will have a list of starting points and a list of lists of ending points
# The index of the starting points correspond to the list of ending points
# example:  word_index['piccolo']['start'][0] is a tuple of the starting points
#           word_index['piccolo']['end'][0] is a list of tuples of the ending points
# The ending points will always be added in order (right,down,left,up)
def word_search(grid: list, words: list | set = {str}) -> dict:

    # Transform words list in set
    if not type(words) == set:
        words = set(words)
    # Check if grid has every row with same size
    it = iter(grid)
    default_len = len(next(it)) # takes lenght of first row
    if not all(len(l) == default_len for l in it): # check if the other rows are same lenght of the first one
        raise ValueError('grid doesn\'t have rows with same size.')

    # Check if grid has only char and is not a string
    for sublist in grid:
        for char in sublist:
            if not type(char) == type(grid[0][0]):
                raise ValueError('grid contains types other than string.')
            if len(char) > 1:
                raise ValueError('grid contains strings longer than one character.')
            
    # Check if words has only alphabetic strings
    for word in words:
        if not type(word) == str:
            raise ValueError('words list contains types other than string.')
        elif not word.isalpha():
            raise ValueError('words list contains non alphabetic strings')
        
    # Lower case grid list and word list
    grid = [[x.lower() for x in sublist] for sublist in grid]
    words = [word.lower() for word in words]

    # Word_index is to store the index found
    # row is the 'height' of the grid (x)
    # column is the 'length' of the grid (y)
    word_index : dict = {word:[] for word in words}
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
                    word_index[word].append([(x,y)])

    # Searches every direction for the word in the grid starting from the index just added in word_index
    # and adds the index ending point if found
    right: int = 0; down: int = 0; left: int = 0; up: int = 0
    for word in word_index.keys():
        # If word has starting point
        if word_index[word]:
            # Takes index starting point (pos)
            for pos in word_index[word]:
                # x = row, y = column
                x = pos[0][0]
                y = pos[0][1]
                right,down,left,up = y,x,y,x
                # Matches every character of a word in every direction
                # Right,down,left,up are counters to see if there are matches in those directions
                # If there isn't space for the word to be in the grid they take '-inf' as value
                # If there isn't a match they take '-inf' as value
                # If the word is found in the grid, the ending point is added to the word_index
                for char in word[1:]:
                    if right != '-inf':
                        if right+1 < column and column-len(word) >= 0:
                            if char == grid[x][right+1]:
                                right += 1
                                if right-y == len(word)-1:
                                    pos.append((x,right))
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
                                    pos.append((down,y))
                                    down = '-inf'
                            else:
                                down = '-inf'
                        else:
                            down = '-inf'
                    if left != '-inf':
                        if left-1 >= 0 and column-len(word) >= 0:
                            if char == grid[x][left-1]:
                                left -= 1
                                if y-left == len(word)-1:
                                    pos.append((x,left))
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
                                    pos.append((up,y))
                                    up = '-inf'
                            else:
                                up = '-inf'
                        else:
                            up = '-inf'
                    if not [x for x in (right,down,left,up) if x == '-inf']:
                        break     

    # Deletion of starting index without ending index in word_index
    for word in word_index.keys():
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
    dictionary : dict = {word:{'start':list,'end':list} for word in word_index.keys() if word_index[word]}
    for word in dictionary.keys():
        # Adds the starting point and the ending point to the dictionary
        dictionary[word]['start'] = [word_index[word][i][0] for i in range(len(word_index[word]))]
        dictionary[word]['end'] = [word_index[word][i][1:] for i in range(len(word_index[word]))]
    dictionary = dict(sorted(dictionary.items()))

    # Ask for printing result
    # Shows the 2D grid and the words that have a starting and ending point
    while True:
        try:
            choose: str = input("Do you want to print the result? (Y/n) ")
            if choose in ['Y','n']:
                if choose == 'Y':
                    print()
                    for x in grid:
                        print(*x)
                    keys: list = dictionary.keys()
                    print(f"\n{'WORDS':<15}{'START':<10}{'END':<20}")
                    for key in keys:
                        j: int = 0
                        for x in dictionary[key]['start']:
                            for y in range(len(x)-1):
                                print(f"{key:<15}{str(dictionary[key]['start'][j]):<10}{str(dictionary[key]['end'][j]):<20}")
                                j += 1
                break
        except:
            continue

    return dictionary
    
grid: list = [
    ['a','l','i','t','o','s','i'],
    ['l','i','l','u','r','p','i'],
    ['p','e','z','o','a','f','l'],
    ['f','a','e','n','p','a','l'],
    ['g','e','e','o','r','t','o']]

word_search(grid,['alitosi','ululato','illuminato','zebra','il','TUOno','orto','ora','apnea'])

