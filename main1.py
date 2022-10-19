# importing module for random number generation
import random

# range of the values of a dice
min_val = 1
max_val = 6

# to loop the rolling through user input
roll_again = "yes"

# loop
while roll_again == "yes":
    print("Rolling The Dices...")
    print("The Values are :")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))

    # asking user to roll the dice again. Any input other than yes will terminate the loop
    roll_again = input("Roll the Dices Again? ")
