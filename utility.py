import random
from colorama import Fore
import time

def randomdigitnumber(length):
    minimum = pow(10, length-1)
    maximum = pow(10, length) - 1
    return random.randint(minimum, maximum)

def get_dice_value(playername, WAIT_FOR_ROLLING_DICE):
    dice_value = random.randint(1, 6)
    input(Fore.LIGHTCYAN_EX + playername + ": " + " Hit Enter to roll the dice: " + Fore.RESET)
    print("Rolling dice...")
    time.sleep(WAIT_FOR_ROLLING_DICE)
    print("Its a " + str(dice_value))
    return dice_value
