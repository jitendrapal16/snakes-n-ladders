from colorama import Fore, init
import sys
import board
import players

# use Colorama to make Termcolor work on Windows too
init()

# function to setup and Initialize the player
def setup():
    GAME_SIZE=0      # Number of Players in the Game
    playerList = []     # Players List
    while GAME_SIZE < 2:
        try:
            GAME_SIZE = int(input("Enter the Number of participants [Default: 2] : ").strip())
        except:
            GAME_SIZE = 2
    for i in range(GAME_SIZE):
        playername = input("Please enter a valid name for first player [Default: Player{}] : ".format(i+1)).strip()
        if (not playername):
            playername = "Player{}".format(i+1)
        playerList.append(players.Player(playername, GAME_SIZE))
    # Return the List of Players
    return playerList

def custom_snake_ladder_config(gameboard):
    answer = input("Do you wanna do Snake and Ladder customization y/N[Default: N] : ").strip()
    if(answer.lower() == 'y'):
        # setting the boards ladder configuration
        gameboard.set_ladders_config()
        # setting the boards snakes configuration
        gameboard.set_snakes_config()


def start():
    # Initialize the players setup and get players
    players = setup()
    rank = 0                            # rank players on each player WIN
    total_players = len(players)        # total players
    is_done = False                     # flag to check game completion
    # Initialize board and setup board with default configurations
    gameboard = board.Board()
    # Customize Snake and ladder Configuration
    custom_snake_ladder_config(gameboard)
    # Starting the game
    while not is_done :
        for player in players:
            if(player.position < 100):
                final_position = gameboard.snake_ladder(player)
                # updating the player position, after getting the next move
                player.update_position(final_position)
            # elif will take, one more step to close the game after WIN at last 2(so used if)
            if(player.position == 100 and player.rank == total_players):
                rank += 1
                # updating the player rank after reaching target
                player.update_rank(rank)
                print("CONGRATS {}!!, YOU GOT RANK {}".format(player.name, player.rank))
                # checking is_done (game)
                if (total_players - rank == 1):
                    is_done = True
                    break
            print("-"*100)  # Using Separtor for each player move
    
    print("-"*100)  # Using Separtor for Result
    print("\nRESULT OF THE GAME : ")
    for player in players:
        print(Fore.LIGHTGREEN_EX + "{} got rank {}".format(player.name, player.rank))
    

if __name__ == "__main__":
    try:
        # start the game
        start()
    except KeyboardInterrupt:
        print("\nQuitting...")
    finally:
        sys.exit()
