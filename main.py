import sys
import settings
from improved_games import tricky_ladders
from improved_games import fair_game1
from improved_games import fair_game2

def main():
    try:
        games = int(sys.argv[1])
        if len(sys.argv) == 2:
            print(f"Analysing {games} games of Snakes and Ladders\n")
            # Iterate over games
            for game in range(games):
                # Position players in the starting point
                positions = [1, 1]
                # Append game data for statistical analysis
                settings.ROLLS.append(0)
                settings.SNAKES_LANDED.append(0)
                # Sart game
                while settings.BOARD[-1] not in positions:
                    for player in range(len(positions)):
                        # Roll the dice
                        positions[player] += settings.roll_dice()
                        settings.ROLLS[game] += 1
                        # Check if its a ladder
                        if positions[player] in settings.LADDERS:
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
        elif 'tricky-ladders' in sys.argv:
            tricky_ladders.run(games)
            print(f"Analysing {games} games Snakes and Ladders with Tricky Ladders\n")

        elif 'fair-game1' in sys.argv:
            fair_game1.run(games)
            print(f"Analysing {games} games Snakes and Ladders with Player 2 starting in position 7\n")
            
        elif 'fair-game2' in sys.argv:
            fair_game2.run(games)
            print(f"Analysing {games} games Snakes and Ladders with Player 2 immune to their first snake\n")

        player1_odds = round((settings.WINS[0] * 100)/settings.GAMES_PLAYED)
        print(f"In a two person game, the first player wins {player1_odds}% of the times")

        snakes_landed_avg = round(sum(settings.SNAKES_LANDED)/len(settings.SNAKES_LANDED))
        print(f"In average, {snakes_landed_avg} snakes are landed in each game")
        
        rolls_avg = round(sum(settings.ROLLS)/len(settings.ROLLS))
        print(f"In average, there are {rolls_avg} rolls per game\n")

    except Exception as e:
        print(f"{e}\n")
        print("To successfully run this application you must provide the number of games you want to simulate. To simulate the normal game, don't provide any other argument.\n")
        print("You can also change the rules by typing 'tricky-ladders', 'fair-game1' or 'fair-game2' as a thrid argument.\n")
        print("Tricky Ladders - when landed in a ladder, players have a 50% chance to take it")
        print("Fair Game 1 - Selects a starting position for player 2 that makes the game more fair")
        print("Fair Game 2 - To make the game more fair, gives immunity for player 2 in the first snake landed")

if __name__ == '__main__':
    main()