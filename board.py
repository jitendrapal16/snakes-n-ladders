from colorama import Fore
import utility

class Board:
    def __init__(self):
        # ladder takes up from 'key' to 'value'
        self.ladders = {
            1:38, 4:14, 9:31, 21:42, 28:84, 36:44, 51:67, 71:91, 61:81
        }
        # snakes takes down from 'key' to 'value'
        self.snakes = {
            16:6, 49:11, 62:19, 87:24, 47:26, 56:53, 64:60, 93:73, 95:75, 98:78
        }
        # Target to WIN
        self.TARGET = 100
        # Wait to Roll Dice
        self.WAIT_FOR_ROLLING_DICE = 1
    
    def set_ladders_config(self):
        total_ladders = int(input("\nEnter Number of ladders [key-value pairs] : ").strip())
        print(Fore.MAGENTA + "------> LADDER TAKES YOU UP from 'KEY' to 'VALUE' , so mention accordingly" + Fore.RESET)
        self.ladders.clear()
        for i in range(total_ladders):
            try:
                key, value = [int(input) for input in input("Enter key values pair for Ladder {}: [eg. key value] ".format(i+1)).split()]
                self.ladders.update({key: value})
            except ValueError:
                print("Got " + ValueError.__name__)
                print("Value will not be Considered")
        print("-"*100)  # Using Separtor for each step
    
    def set_snakes_config(self):
        total_snakes = int(input("\nEnter Number of Snakes [key-value pairs] : ").strip())
        print(Fore.MAGENTA + "------> SNAKES TAKES YOU DOWN from 'KEY' to 'VALUE' , so mention accordingly" + Fore.RESET)
        self.snakes.clear()
        for i in range(total_snakes):
            try:
                key, value = [int(input) for input in input("Enter key values pair for Snake {}: [eg. key value] ".format(i+1)).split()]
                self.snakes.update({key: value})
            except ValueError:
                print("Got " + ValueError.__name__)
                print("Value will not be Considered")
        print("-"*100)  # Using Separtor for each step
    
    def snake_bit(self, old_value, current_value, player_name):
        print(Fore.RED + "~~~~~~~~> " + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value) + Fore.RESET)


    def ladder_climb(self, old_value, current_value, player_name):
        print(Fore.LIGHTGREEN_EX + "######### " + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value) + Fore.RESET)

    def snake_ladder(self, player):
        # get the current position, which is old value for player, in this turn
        old_value = player.position
        # Roll dice to reach current value
        new_value = utility.get_dice_value(player.name, self.WAIT_FOR_ROLLING_DICE)
        # getting the current value after dice roll up
        current_value = old_value + new_value

        if current_value > self.TARGET:
            print("You need " + str(self.TARGET - old_value) + " to win this game. Keep trying!!")
            return old_value        # Return the old value, because Target Exceed(No update)

        print(Fore.LIGHTYELLOW_EX + player.name + " moved from " + str(old_value) + " to " + str(current_value) + Fore.RESET)
        if current_value in self.snakes.keys():
            final_value = self.snakes.get(current_value)    # Update the final value after snake bit
            self.snake_bit(current_value, final_value, player.name)

        elif current_value in self.ladders.keys():
            if (new_value == 6):
                updated_value = self.ladders.get(current_value) # get the updated value
                player.update_position(updated_value)           # update position after getting 6
                self.ladder_climb(current_value, updated_value, player.name)
                final_value = self.snake_ladder(player)
            else:
                final_value = self.ladders.get(current_value)
                self.ladder_climb(current_value, final_value, player.name)

        else:
            if (new_value == 6):
                updated_value = current_value                   # get the updated value
                player.update_position(updated_value)           # update position after getting 6
                final_value = self.snake_ladder(player)         # set the updated value with one more Dice Roll
            else:
                final_value = current_value
        # Return the final value
        return final_value

