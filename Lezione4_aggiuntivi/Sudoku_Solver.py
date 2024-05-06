# Gioele Amendola
# 06/05/2024

# Create a function that is_safes a solve_sudoku puzzle using backtracking.
# Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
# Implement a backtracking algorithm to check for valid placements in empty cells,
# ensuring no row, column, or 3x3 subgrid contains duplicates.
# is_safe the puzzle by filling in the remaining empty cells with valid numbers.

# Size of grid
M: int = 9

# Function to print grid
def print_sudoku(grid: list[list[int]]):
    for x in range(M):
        for y in range(M):
            print(grid[x][y], end=" ")
        print()
    print()

# Function to check if a cell is safe
def is_safe(grid: list[list[int]], num: int, row: int, col: int) -> bool:
    # Check same column
    for x in range(M):
        if grid[x][col] == num:
            return False
    # Check same row
    for x in range(M):
        if grid[row][x] == num:
            return False
    # Check in cell 3x3
    start_row = row - row % 3
    start_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[x + start_row][y + start_col] == num:
                return False
    # Checked everything
    return True

# Function to backtracking
def solve_sudoku(grid: list[list[int]], row: int, col: int) -> bool:
    # Check if reached max grid
    if row == M - 1 and col == M:
        return True
    # Check if reached max col
    if col == M:
        row += 1
        col = 0
    # Check if cell has value
    if grid[row][col] > 0:
        # Skip current cell
        return solve_sudoku(grid, row, col + 1)

    # Check for number in grid
    for num in range(1, M + 1):
        # Check for saftey of number
        if is_safe(grid,num,row,col):
            # Assign number as value in grid
            grid[row][col] = num
            # Go to next cell
            if solve_sudoku(grid, row, col+1):
                return True
            # If didn't reach max grid
            # Remove number from grid
            grid[row][col] = 0

    # If number is not found
    return False

# Main function that you call upon
def sudoku(grid):
    # Check if solvable
    if (solve_sudoku(grid, 0, 0)):
        # Print grid if found solution
        print_sudoku(grid)
    else:
        print("Solution not found")

# Test Example:
grid1: list[list[int]] = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
                          [0, 1, 0, 0, 0, 4, 0, 0, 0],
                          [4, 0, 7, 0, 0, 0, 2, 0, 8],
                          [0, 0, 5, 2, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 9, 8, 1, 0, 0],
                          [0, 4, 0, 0, 0, 3, 0, 0, 0],
                          [0, 0, 0, 3, 6, 0, 0, 7, 2],
                          [0, 7, 0, 0, 0, 0, 0, 0, 3],
                          [9, 0, 3, 0, 0, 0, 6, 0, 4]]

grid2: list[list[int]] = [[3, 1, 0, 6, 0, 5, 4, 0, 0],
                          [6, 0, 4, 2, 1, 0, 0, 8, 3],
                          [9, 0, 0, 0, 3, 0, 0, 2, 0],
                          [2, 4, 7, 5, 6, 0, 0, 3, 0],
                          [8, 6, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 5, 3, 0, 2, 6, 7, 0],
                          [0, 8, 0, 0, 0, 0, 0, 0, 4],
                          [0, 3, 0, 0, 0, 0, 7, 6, 2],
                          [5, 0, 0, 0, 7, 0, 8, 0, 9]]
sudoku(grid1)
sudoku(grid2)