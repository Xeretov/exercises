'''
This module provides several functions to simulate a race between the turtle and the hare
'''

# Gioele Amendola
# 14/05/2024

from random import choices
from random import randint

def turtle_walk_speed(weather: bool = False) -> int:
    '''
    This function returns the walking speed of the turtle based on probability.

    Returns:
        int: [3, 1, -6]
    '''
    walking_speed: list[int] = [3, 1, -6]
    weight: list[float] = [0.5, 0.3, 0.2]
    return choices(walking_speed, weight)[0] - 1 if weather else choices(walking_speed, weight)[0] 

def hare_walk_speed(weather: bool = False) -> int:
    '''
    This function returns the walking speed of the hare based on probability

    Returns:
        int: [0, 9, -12, 1, -2]
    '''
    walking_speed: list[int] = [0, 9, -12, 1, -2]
    weight: float = [0.2, 0.2, 0.1, 0.3, 0.2]
    return choices(walking_speed, weight)[0] -2 if weather else choices(walking_speed, weight)[0] 

def show_route(route: list[str]) -> None:
    '''
    This function shows the current progression of the turtle and the hare 
    '''
    for char in route:
        print(f"{char}",end="")
    print(end="\n\n")

def start_simulation() -> None:
    '''
    This function starts the simulation
    '''
    route: list[str] = ["_"]*randint(25,100)
    max_len: int = len(route)
    i: int = 1
    weather: bool = False
    t_token: int = 0
    h_token: int = 0
    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")
    while True:
        route[t_token] = "_"
        route[h_token] = "_"
        if (i-1)% 10 == 0:
            weather = choices([True,False],[0.5,0.5])[0]
            print("It's raining ☂" if weather else "It's sunny ☀︎",end="\n\n")
        t_token += turtle_walk_speed(weather)
        h_token += hare_walk_speed(weather)
        if t_token >= max_len and h_token >= max_len:
            route[-1] = "X"
            print("Last Lap:")
            show_route(route)
            print("\nIT'S A TIE.")
            break
        elif t_token >= max_len:
            route[h_token if h_token >= 0 else 0] = "H"
            route[-1] = "T"
            print("Last Lap:")
            show_route(route)
            print("\nTORTOISE WINS! || VAY!!!")
            break
        elif h_token >= max_len:
            route[t_token if t_token >= 0 else 0] = "T"
            route[-1] = "H"
            print("Last Lap:")
            show_route(route)
            print("\nHARE WINS || YUCH!!!")
            break
        if t_token < 0:
            t_token = 0
        if h_token < 0:
            h_token = 0
        if t_token == h_token:
            route[t_token] = 'X'
        else:
            route[t_token] = 'T'
            route[h_token] = 'H'
        print(f"Round: {i}")
        i += 1
        show_route(route)

start_simulation()