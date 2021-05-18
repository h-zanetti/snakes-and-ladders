import sys
import settings

def main():
    try:
        games = int(sys.argv[1])
        if 'tricky-snakes' in sys.argv:
            pass
        elif 'fair-game1' in sys.argv:
            pass
        elif 'fair-game2' in sys.argv:
            pass
        else:
            # Iteração dos jogos
            for game in range(0, games):
                positions = [1, 1]
                settings.ROLLS.append(0)
                settings.SNAKES_LANDED.append(0)
                while settings.BOARD[-1] not in positions:
                    # Iteração das rodadas
                    for player in range(0, len(positions)):
                        positions[player] += settings.roll_dice()
                        settings.ROLLS[game] += 1
                        if positions[player] in settings.LADDERS:
                            positions[player] = settings.LADDERS[positions[player]]
                        elif positions[player] in settings.SNAKES:
                            settings.SNAKES_LANDED[game] += 1
                            positions[player] = settings.SNAKES[positions[player]]
                        if positions[player] >= settings.BOARD[-1]:
                            settings.WINS[player] += 1
                            settings.GAMES_PLAYED += 1
                            positions[player] = settings.BOARD[-1]
                            break
            print(f"Analysing {settings.GAMES_PLAYED} games Snakes and Ladders\n")
            player1_odds = round((settings.WINS[0] * 100)/settings.GAMES_PLAYED)
            print(f"In a two person game, the first player wins {player1_odds}% of the times")
            snakes_landed_avg = round(sum(settings.SNAKES_LANDED)/len(settings.SNAKES_LANDED))
            print(f"In average, {snakes_landed_avg} snakes are landed in each game")
            rolls_avg = round(sum(settings.ROLLS)/settings.GAMES_PLAYED)
            print(f"In average, there are {rolls_avg} rolls per game\n")
    except:
        print("To successfully run this application you must provide the number of games you want to simulate.")
        # print("In order to simulate the normal game, just provide the number of matches you want to simulate.")
        # print("You also can change the rules by typing 'tricky-ladders', 'fair-game1' or 'fair-game2'.")
        # print("Tricky Ladders - when landed in a ladder, players have a 50% change to take it")
        # print("Fair Game 1 - Selects a starting position for player 2 that makes the game more fair")
        # print("Fair Game 2 - To make the game more fair, gives immunity for player 2 in the first snake landed")
            

if __name__ == '__main__':
    main()