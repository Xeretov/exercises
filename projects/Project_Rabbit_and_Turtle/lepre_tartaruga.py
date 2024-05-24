'''
This module provides several functions to simulate a race between the turtle and the hare
'''

# Gioele Amendola
# 14/05/2024

from random import choices
from random import randint


def turtle_walk_speed(t_token, t_energy, weather: bool = False) -> int:
    '''
    This function returns the walking speed of the turtle based on probability.

    Returns:
        int: [3, 1, -6]
    '''
    # values of walking speed
    walking_speed: list[int] = [3, 1, -6]
    # weight for picking a certain walking speed
    weight: list[float] = [0.5, 0.3, 0.2]
    # chosen speed
    chosen: int = choices(walking_speed, weight)[0]
    # found index of chosen speed
    index: int = walking_speed.index(chosen)

    if index == 0:
        t_energy -= 5
    elif index == 1:
        t_energy -= 3
    else:
        t_energy -= 10
    if t_energy < 0:
        t_energy = 10
    else:
        t_token += chosen - 1 if weather else chosen

    return t_token, t_energy

def hare_walk_speed(h_token, h_energy, weather: bool = False) -> int:
    '''
    This function returns the walking speed of the hare based on probability

    Returns:
        int: [0, 9, -12, 1, -2]
    '''
    walking_speed: list[int] = [0, 9, -12, 1, -2]
    weight: float = [0.2, 0.2, 0.1, 0.3, 0.2]
    chosen: int = choices(walking_speed, weight)[0]
    index: int = walking_speed.index(chosen)
    temp: int = h_energy
    if index == 0:
        h_energy += 10
        h_energy = min(h_energy,100)
    elif index == 1:
        temp -= 15
    elif index == 2:
        temp -= 20
    elif index == 3:
        temp -= 5
    elif index == 4:
        temp -=8
    if temp >= 0:
        h_token += chosen -2 if weather and chosen != 0 else chosen
        h_energy = temp

    return h_token, h_energy

def bonuses_obstacles(token: int, t_name: str, obstacles: dict, bonuses: dict) -> int:
    '''
    This function checks for bonuses and obstacles

    Args:
        token (int): position of token
        t_name (str): name of token's possesor
        obstacles (dict): dictionary of obstacles
        bonuses (dict): dictionary of bonuses

    Returns:
        int: token new position
    '''
    check: list = []
    check_len: int = 0
    while True:
        if token in check:
            print(f"The {t_name} got out of the loop")
            break
        if token in obstacles.keys():
            print(f"The {t_name} hit an obstacle of {obstacles[token]} on position {token}")
            check.append(token)
            token += obstacles[token]
        if token in check:
            print(f"The {t_name} got out of the loop")
            break
        if token in bonuses.keys():
            print(f"The {t_name} got a bonus {bonuses[token]} on position {token}")
            check.append(token)
            token += bonuses[token]
        if check_len == len(check):
            break
        check_len = len(check)
    print()
    return token

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
    max_len: int = len(route) -1
    # interval for obstacles (fixed to 10% of route length)
    interval: int = round(max_len * 0.1)
    # obstacles:
    # keys = range(1, route length) when on interval
    # value = -(randint(1, route length//10))
    obstacles: dict = {k:-v for k,v in zip(
                        range(1,max_len+1),
                        [randint(1,max_len//10) for _ in range(1,max_len+1)])
                       if k%interval == 0}
    # bonuses:
    # keys = randint(1, route length-2) if not already an obstacle
    # values = randint(1, route length//10)+3
    bonuses: dict = {k:v for k,v in zip(
                    [randint(1,max_len-1) for _ in range(len(obstacles.values()))],
                    [randint(1,max_len//10)+3 for _ in range(1,max_len+1)])
                     if k not in list(obstacles.keys())}
    i: int = 1
    weather: bool = False
    t_token: int = 0
    t_energy: int = 100
    h_token: int = 0
    h_energy: int = 100
    prev_t: int = 0
    prev_h: int = 0
    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")
    while True:
        route[t_token], route[h_token] = "_", "_"
        if (i-1)% 10 == 0:
            weather = choices([True,False],[0.5,0.5])[0]
        prev_t, prev_h = t_token, h_token
        t_token, t_energy = turtle_walk_speed(t_token, t_energy, weather)
        h_token, h_energy = hare_walk_speed(h_token, h_energy, weather)
        print()
        t_token = bonuses_obstacles(t_token, "turtle", obstacles, bonuses)
        h_token = bonuses_obstacles(h_token, "hare", obstacles, bonuses)
        if t_token >= max_len and h_token >= max_len:
            route[-1] = "X"
            print(f"Last Round: {i}")
            print("It's raining ☂" if weather else "It's sunny ☀︎")
            show_route(route)
            print("\nIT'S A TIE.")
            print(f"\nroute length: {max_len}")
            break
        if t_token >= max_len:
            route[h_token if h_token >= 0 else 0] = "H"
            route[-1] = "T"
            print(f"Last Round: {i}")
            show_route(route)
            print("\nTURTLE WINS! || VAY!!!")
            print(f"\nroute length: {max_len}")
            break
        if h_token >= max_len:
            route[t_token if t_token >= 0 else 0] = "T"
            route[-1] = "H"
            print(f"Last Round: {i}")
            show_route(route)
            print("\nHARE WINS || YUCH!!!")
            print(f"\nroute length: {max_len}")
            break
        t_token = max(t_token,0)
        h_token = max(h_token,0)
        if t_token == h_token:
            route[t_token] = 'X'
        else:
            route[t_token] = 'T'
            route[h_token] = 'H'
        print(f"Round: {i}",end=" ")
        if i%3 == 0 or i == 1:
            print("- It's raining ☂" if weather else "- It's sunny ☀︎")
        else:
            print()
        i += 1
        show_route(route)
        print(f"Turtle moved: {t_token-prev_t}, Turtle position: {t_token}, Turtle energy: {t_energy}")
        print(f"Hare moved: {h_token-prev_h}, Hare position: {h_token}, Hare energy: {h_energy}")
        print("\n")
        if i > 5000:
            print("The race was too long. Neither won and everyone left.\n")
            break

if __name__ == "__main__":
    start_simulation()
