from random import randint
import settings

def run(games):
    # Iterate over games
    for game in range(0, games):
        # Position players in the starting point
        positions = [1, 1]
        # Append data to analyse this games
        settings.ROLLS.append(0)
        settings.SNAKES_LANDED.append(0)
        while settings.BOARD[-1] not in positions:
            for player in range(0, len(positions)):
                # Roll the dice
                positions[player] += settings.roll_dice()
                settings.ROLLS[game] += 1
                # Check if its a ladder
                if positions[player] in settings.LADDERS:
                    # 50% chance to take it
                    if randint(0,1):
                        positions[player] = settings.LADDERS[positions[player]]
                # Check if its a snake
                elif positions[player] in settings.SNAKES:
                    settings.SNAKES_LANDED[game] += 1
                    positions[player] = settings.SNAKES[positions[player]]
                # Check if player won
                if positions[player] >= settings.BOARD[-1]:
                    settings.WINS[player] += 1
                    settings.GAMES_PLAYED += 1
                    positions[player] = settings.BOARD[-1]
                    break
