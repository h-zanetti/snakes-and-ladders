from random import randint

# Functions
def roll_dice():
    return randint(1,6)

# Game setup
BOARD = list(range(1,37))
LADDERS = {
    3: 16,
    5: 7,
    15: 25,
    18: 20,
    21: 32
}
SNAKES = {
    12: 2,
    14: 11,
    17: 4,
    31: 19,
    35: 22
}

# Statistics
GAMES_PLAYED = 0
SNAKES_LANDED = []
ROLLS = []
WINS = [0, 0]