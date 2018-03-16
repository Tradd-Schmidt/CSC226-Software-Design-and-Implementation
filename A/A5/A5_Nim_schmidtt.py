######################################################################
# Authors: Tradd Schmidt

# Username: schmidtt
#
# Assignment: A5: The Game of Nim
#
# Purpose: To allow someone to play  a game of Nim with a computer opponent
#######################################################################
# Acknowledgements:
# Original Author: Tradd Schmidt
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################


import random


def ask_for_balls():
    """
    Asks the user how many balls they want to use for the game
    :return: an integer
    """
    balls = 0

    while balls < 15:
        balls = int(input("How many balls do you want to use to play this game of Nim?"))
        if balls < 15:
            print("Please enter a number that is equal to or higher than 15.\n ")
    return balls


def player_number():
    """
    Asks how many balls the person would like to take.
    :return: an integer 1-4
    """
    number = int(input("How many balls will you take?"))
    while number < 1 or number > 4:
        number = int(input("That is an invalid number. Please enter a number between 1 and 4"))
    return number


def player_turn(subtract, balls_left):
    """
    Takes how many balls there are and a players choice of subtraction to subtract from the total number of balls
    :param subtract: How much will be subtracted
    :param balls_left: How many balls there are left
    :return: How many balls there are after the subtraction
    """
    if balls_left == 3:
        if subtract > 3:
            print("You cannot take more than 3. Pick a number between 1 and 3.")
        elif subtract == 3:
            balls_left -= subtract
            print("You take " + str(subtract) + " balls.")
            print("There are no balls left.")
        elif subtract == 2:
            balls_left -= subtract
            print("You take " + str(subtract) + " balls.")
            print("There is now 1 ball left")
        else:
            balls_left -= subtract
            print("You take " + str(subtract) + " ball.")
            print("There is now 2 balls left.")
    elif balls_left == 2:
        if subtract > 2:
            print("You can not take more than 2. Pick either 1 or 2.")
        elif subtract == 2:
            print("You take " + str(subtract) + " balls.")
            print("There are no balls left")
        else:
            balls_left -= subtract
            print("You take " + str(subtract) + " ball.")
            print("There is now 1 ball left")
    elif balls_left == 1:
        if subtract == 1:
            print("You take " + str(subtract) + " ball.")
            balls_left -= subtract
        else:
            print("You can only take one")
    else:
        balls_left -= subtract
        if subtract == 1:
            print("You take " + str(subtract) + " ball.")
            print("There is now " + str(balls_left) + " balls left.")
        else:
            print("You take " + str(subtract) + " balls.")
            print("There is now " + str(balls_left) + " balls left.")
    return balls_left


def comps_turn(balls_left):
    """
    Takes the correct number of balls away to win if it can, otherwise it takes a random number from 1 to 4
    :param balls_left: How many balls are left
    :return: How many balls are left after the subtraction
    """
    if balls_left % 5 != 0:
        if balls_left % 5 == 1:
            balls_left -= 1
            print("The computer takes 1 ball.")
            print("There is now " + str(balls_left) + " balls left.")
        elif balls_left % 5 == 2:
            balls_left -= 2
            print("The computer takes 2 balls.")
            print("There is now " + str(balls_left) + " balls left.")
        elif balls_left % 5 == 3:
            balls_left -= 3
            print("The computer takes 3 balls.")
            print("There is now " + str(balls_left) + " balls left.")
        else:
            balls_left -= 4
            print("The computer takes 4 balls.")
            print("There is now " + str(balls_left) + " balls left.")
    else:
        subtract = random.randint(1, 4)
        if subtract == 1:
            balls_left -= subtract
            print("The computer takes 1 ball")
            print("There is now " + str(balls_left) + " balls left.")
        else:
            balls_left -= subtract
            print("The computer takes " + str(subtract) + " balls.")
            print("There is now " + str(balls_left) + " balls left.")
    return balls_left


def main():
    balls = ask_for_balls()
    print("The game will start with " + str(balls) + " balls")
    while balls > 0:
        subtract = player_number()
        balls = player_turn(subtract, balls)
        if balls != 0:
            balls = comps_turn(balls)
        elif balls < 5 and balls > 0:
            print("You lose.")
        else:
            print("You win!")


main()
