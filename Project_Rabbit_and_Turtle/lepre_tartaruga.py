'''
This module provides several functions to simulate a race between the turtle and the hare
'''

# Gioele Amendola
# 14/05/2024
from random import choices

def turtle_walk_speed() -> int:
    '''
    This function returns the walking speed of the turtle based on probability.

    Returns:
        int: [3, 1, -6]
    '''
    walking_speed: list[int] = [3, 1, -6]
    weight: list[float] = [0.5, 0.3, 0.2]
    return choices(walking_speed, weight)[0]

def hare_walk_speed() -> int:
    '''
    This function returns the walking speed of the hare based on probability

    Returns:
        int: [0, 9, -12, 1, -2]
    '''
    walking_speed: list[int] = [0, 9, -12, 1, -2]
    weight: float = [0.2, 0.2, 0.1, 0.3, 0.2]
    return choices(walking_speed, weight)[0]

def show_route(route: list[str]) -> None:
    '''
    This function shows the current progression of the turtle and the hare 
    '''
    for char in route:
        print(f"{char:<1}",end="")
    print(end="\n\n")

def start_simulation() -> None:
    '''
    This function starts the simulation
    '''
    route: list[str] = ["-"]*70
    i: int = 1
    racing: bool = True
    t_token: int = 0
    h_token: int = 0
    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")
    while racing:
        copy_route: list = route[:]
        t_token += turtle_walk_speed()
        h_token += hare_walk_speed()
        if t_token >= 70 and h_token >= 70:
            print("\nIT'S A TIE.")
            break
        elif t_token >= 70:
            print("\nTORTOISE WINS! || VAY!!!")
            break
        elif h_token >= 70:
            print("\nHARE WINS || YUCH!!!")
            break
        if t_token < 0:
            t_token = 0
        if h_token < 0:
            h_token = 0
        if t_token == h_token:
            copy_route[t_token] = 'X'
        else:
            copy_route[t_token] = 'T'
            copy_route[h_token] = 'H'
        print(f"Round: {i}")
        i += 1
        show_route(copy_route)

start_simulation()