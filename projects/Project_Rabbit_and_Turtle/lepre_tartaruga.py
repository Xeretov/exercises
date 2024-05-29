'''
This module provides several functions to simulate a race between the turtle and the hare
'''

# Gioele Amendola
# 14/05/2024 - 24/05/2024

from random import choices
from random import randint
from random import choice
from modules import color_terminal as color

def turtle_movement(t_token, t_energy, weather: bool = False) -> int:
    '''
    This function returns the walking speed of the turtle based on probability.

    Returns:
        int: [3, 1, -6]
    '''
    # Values of movement
    movement: list[int] = [3, 1, -6]
    # Weight for picking a certain movement
    weight: list[float] = [0.5, 0.3, 0.2]
    # Chosen movement
    chosen: int = choices(movement, weight)[0]
    # Index of chosen value
    index: int = movement.index(chosen)
    # Energy change, if energy is above 0 then move token else refill energy
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
    # Return new position and energy
    return t_token, t_energy


def hare_movement(h_token, h_energy, weather: bool = False) -> int:
    '''
    This function returns the walking speed of the hare based on probability

    Returns:
        int: [0, 9, -12, 1, -2]
    '''
    # Values of movement
    movement: list[int] = [0, 9, -12, 1, -2]
    # Weight for picking a certain movement
    weight: float = [0.2, 0.2, 0.1, 0.3, 0.2]
    # Chosen movement
    chosen: int = choices(movement, weight)[0]
    # Index of chosen value
    index: int = movement.index(chosen)
    # Temporary variable (energy) to check if hare can do a movement
    # If not returns current token and energy otherwise return new position and energy
    energy: int = h_energy
    if index == 0:
        h_energy += 10
        h_energy = min(h_energy, 100)
    elif index == 1:
        energy -= 15
    elif index == 2:
        energy -= 20
    elif index == 3:
        energy -= 5
    elif index == 4:
        energy -= 8
    if energy >= 0:
        h_token += chosen - 2 if weather and chosen != 0 else chosen
        h_energy = energy

    return h_token, h_energy


def bonuses_obstacles(token: int, t_name: str, obstacles: dict, bonuses: dict, max_len: int) -> int:
    '''
    This function checks for bonuses and obstacles

    Args:
        token (int): position of token
        t_name (str): name of token's possesor
        obstacles (dict): dictionary of obstacles
        bonuses (dict): dictionary of bonuses
        max_len (int): length of track

    Returns:
        int: token new position
    '''
    # Variables used for loops and debugging
    checking: list = []
    values: list = []
    checking_len: int = 0
    start_token: int = token
    print(color.grey,end="")
    while True:
        # Checks if token has already been to same position before
        if token in checking:
            print(f"The {color.c}{t_name}{color.grey} got out of the loop")
            break
        # Checks if token is in the same position as an obstacle
        if token in obstacles:
            print(f"The {color.c}{t_name}{color.grey} hit an obstacle of {color.bred}{obstacles[token]}{color.cgrey} on position {color.cb}{token}{color.cgrey}")
            checking.append(token)
            values.append(obstacles[token])
            token += obstacles[token]
        # Checks if token has already been to same position before
        if token in checking:
            print(f"The {color.c}{t_name}{color.grey} got out of the loop")
            break
        # Checks if token is in the same position as a bonus
        if token in bonuses:
            print(f"The {color.c}{t_name}{color.grey} got a bonus of {color.bgreen}{bonuses[token]}{color.cgrey} on position {color.cb}{token}{color.cgrey}")
            checking.append(token)
            values.append(bonuses[token])
            token += bonuses[token]
        # Check if token has not been in any new obstacle or bonus position
        if checking_len == len(checking):
            break
        checking_len = len(checking)
    # Debug print if token has been in obstacle or bonus position
    if checking:
        # Debug print to see the total movement if more than one obstacle or bonus position has been hit
        if len(checking) > 1:
            print("\nThe total amount of movement was "+(color.red if sum(values)<0 else color.green)+f"{sum(values)}{color.cgrey} for the {color.c}{t_name}{color.grey}:")
        print(f"started from {color.cb}{start_token}{color.cgrey} ended to {color.cb}{min(token,max_len) if token > max_len else max(token,0)}")
    print(color.c)
    # Return new token position
    return token


def check(t: int, h: int, length: int, **kwargs) -> bool:
    '''
    This function checks if the tokens have won the race

    Args:
        t (int): turtle token
        h (int): hare token
        length (int): track length

    Returns:
        bool: return True if a token won else False
    '''

    track = kwargs["track"]
    weather = kwargs["weather"]
    i = kwargs["i"]

    if t >= length and h >= length:
        track[-1] = "X"
        print(f"Last Round: {color.b}{i}{color.c}",end=" - ")
        print(f"{color.bblue}It's raining ''☂''" if weather else f"{color.byellow} It's sunny ☀︎"+color.c)
        show_route(track)
        print(f"\n{color.b}IT'S A TIE.{color.c}")
        print(f"\nroute length: {color.b}{length}{color.c}\n")
        return True
    if t >= length:
        track[h if h >= 0 else 0] = "H"
        track[-1] = "T"
        print(f"Last Round: {color.b}{i}{color.c}",end=" - ")
        print((f"{color.bblue}It's raining ''☂''" if weather else f"{color.byellow} It's sunny ☀︎")+color.c)
        show_route(track)
        print(f"\n{color.b}TURTLE WINS! || VAY!!!{color.c}")
        print(f"\nroute length: {color.b}{length}{color.c}\n")
        return True
    if h >= length:
        track[t if t >= 0 else 0] = "T"
        track[-1] = "H"
        print(f"Last Round: {color.b}{i}{color.c}",end=" - ")
        print((f"{color.bblue}It's raining ''☂''" if weather else f"{color.byellow} It's sunny ☀︎")+color.c)
        show_route(track)
        print(f"\n{color.b}HARE WINS || YUCH!!!{color.c}")
        print(f"\nroute length: {color.b}{length}{color.c}\n")
        return True
    return False


def show_route(track: list[str]) -> None:
    '''
    This function shows the current progression of the tokens 
    '''
    for char in track:
        print(f"{char}", end="")
    print(end="\n\n")


def start_simulation() -> None:
    '''
    This function starts the simulation
    '''
    # Initialization of track and all variables
    track: list[str] = ["_"]*randint(26, 101)
    max_len: int = len(track) - 1
    # Interval for obstacles (fixed to 10% of track length)
    interval: int = round(max_len * 0.1)
    # Obstacles:
    # keys = range(1, track length) every interval
    # values = -(randint(1, track length//10))
    obstacles: dict = {k: -v for k, v in zip(
        range(1, max_len+1),
        [randint(1, max_len//10) for _ in range(1, max_len+1)])
        if k % interval == 0}
    # Bonuses:
    # keys = randint(1, track length-2) if not already an obstacle
    # values = randint(1, track length//10)+3
    bonuses: dict = {k: v for k, v in zip(
        [randint(1, max_len-1) for _ in range(len(obstacles.values()))],
        [randint(1, max_len//10)+3 for _ in range(1, max_len+1)])
        if k not in obstacles}
    # Ticks or Rounds
    i: int = 1
    # Sunny or Rainy
    weather: bool = False
    # Token and energy of Turtle
    t_token: int = 0
    t_energy: int = 100
    # Token and energy of Hare
    h_token: int = 0
    h_energy: int = 100
    # Variables used to know previous position of the tokens
    prev_t: int = 0
    prev_h: int = 0

    # Start racing
    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")
    while True:
        track[t_token], track[h_token] = "_", "_"
        # Weather change every ten ticks
        if (i-1) % 10 == 0:
            weather = choice([True, False])
        # Previous position has been established
        prev_t, prev_h = t_token, h_token
        # Move token based on turtle or hare movement
        t_token, t_energy = turtle_movement(t_token, t_energy, weather)
        h_token, h_energy = hare_movement(h_token, h_energy, weather)
        # Check if token has hit a special position
        t_token = bonuses_obstacles(t_token, "turtle", obstacles, bonuses, max_len)
        h_token = bonuses_obstacles(h_token, "hare", obstacles, bonuses, max_len)
        # Check if race has finished
        if check(t_token, h_token, max_len, track=track, weather=weather, i=i):
            break
        # Takes max from t_token (it can go less than 0) and 0
        t_token = max(t_token, 0)
        h_token = max(h_token, 0)
        # Changes track positioning the tokens on the track
        if t_token == h_token:
            track[t_token] = 'X'
        else:
            track[t_token] = 'T'
            track[h_token] = 'H'
        # Shows changes and round for debug
        print(f"Round: {color.b}{i}{color.c}", end=" ")
        if i % 3 == 0 or i == 1:
            print("- "+(f"{color.bblue}It's raining ''☂''" if weather else f"{color.byellow} It's sunny ☀︎")+color.c)
        else:
            print()
        # Next tick/round
        i += 1
        # Prints track
        show_route(track)
        # Debug
        print(f"{color.bgrey}Turtle moved: {color.cbgreen if t_token-prev_t>0 else color.cbred if t_token-prev_t<0 else color.cb}{t_token-prev_t}{color.bgrey},",
              f" Turtle position: {color.cb}{t_token}{color.grey},",
              f" Turtle energy: {color.clight_cyan if t_energy!=0 else color.cred}{t_energy}{color.bgrey}")

        print(f"Hare moved: {color.cbgreen if h_token-prev_h>0 else color.cbred if h_token-prev_h<0 else color.cb}{h_token-prev_h}{color.bgrey},",
              f" Hare position: {color.cb}{h_token}{color.grey},",
              f" Hare energy: {color.clight_cyan if h_energy!=0 else color.cred}{h_energy}{color.c}")

        print("\n")
        # if reached 5000th round exit program
        if i > 5000:
            print("The race was too long. Neither won and everyone left.\n")
            break


if __name__ == "__main__":
    start_simulation()
