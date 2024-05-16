'''
This module provides a backtracking function to solve the N*Queen problem
'''
# Gioele Amendola
# 15/05/2024

def nqueen(queens: int = 4) -> None:
    '''
    This is the main function for solving nqueen problem

    Args:
        queens(int)(optional): queens needed to find. Defaults to 4.
    '''
    global N
    N = queens
    grid: list[list[int]] = [[0]*N]
    for _ in range(N-1):
        grid.append([0]*N)
    if solve_nqueen(grid, 0):
        print_nqueen(grid)
    else:
        print("Solution not found")
    
def print_nqueen(grid: list) -> None:
    '''
    This function prints the solutions found for the nqueen problem

    Args:
        grids(list): a list containing all the possible solutions
    '''
    print()
    for x in range(N):
        for y in range(N):
            print(f"{'#' if grid[x][y] == 0 else 'Q'}", end= " ")
        print()
    print()

def solve_nqueen(grid: list[list[int]], col: int) -> bool:
    '''
    This function checks all possibilities while finding a solution for the nqueen problem

    Args:
        grid(list[list[int]]): the grid.
        col(int): the current column.
    '''
    # Check if all queens are placed
    if col >= N:
        return True
    # Place a Queen on every column
    # Checks every row(i)
    for i in range(N):
        # Check if queen is safe to place
        if is_safe(grid, i, col):
            grid[i][col] = 1
            # Goes to the next cell
            if solve_nqueen(grid, col + 1):
                return True
            grid[i][col] = 0
    # Doesn't find a solution
    return False
    
def is_safe(grid: list[list[int]], row: int, col: int) -> bool:
    '''
    This function checks if the queen is safe to place on the current row and column
    
    Args:
        grid(list[list[int]]): grid to check.
        row(int): current row
        col(int): current column.
    '''
    # Check if row is safe
    if 1 in grid[row]:
        return False
    # Check diagonal (upper left)
    if 1 in [grid[i][j] for i,j in zip(range(row, -1, -1), range(col, -1, -1))]:
        return False
    # Check diagonal (lower left)
    if 1 in [grid[i][j] for i,j in zip(range(row,N), range(col, -1, -1))]:
        return False
    return True

nqueen(4)
