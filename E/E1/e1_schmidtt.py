######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# Assignment: E1 - Coding Portion
# Purpose: Evaluate your ability to write code in Python
# Value: 25 points total
#
####################################################################################
#
# Instructions: The following code is incomplete.
#
# A successful student will have completed the following tasks:
#
#   1) TODO     Refactor the existing code to properly use a main() function (3 pts)
#   2) TODO     Eliminate any unnecessary code from the highest level of the program (no indentation) (2 pts)
#   3) TODO     Create and use a function that draws a parallelogram (8 pts)
#   4) TODO     Create and use a fruitful function to calculate the angles of the parallelogram (8 pts)
#   5) TODO     Incorporates docstrings and comments which details the program's operation (4 pts)
#
# Upon completion, save this file as e1_username.py (replacing username with your username)
# and upload the document to Moodle before the end of your class period
####################################################################################
#
# A parallelogram is a four-sided shape where the opposite sides are always parallel to each other.
# A square and a rectangle are both parallelograms. So is this shape:
#
#      ----------
#     /         /
#    /         /
#   /         /
#  -----------
# Your task is to refactor the code below to draw a parallelogram
#
####################################################################################


import turtle


# TODO      Refactor the below code into a function that is able to draw a parallelogram.
# TODO      Your function should likely take in a minimum of two parameters:
# TODO      a turtle object, and the angle of one corner of the parallelogram.
#
# TODO      Using the angle provided to the above function, you can determine the other angle
# TODO      of the parallelogram by subtracting that angle from 180.
# TODO      Create a second function (a fruitful function) to perform and return this angle calculation.

# Draws a parallelogram
def draw_parallelogram(turt, angle):
    """
    Draws a parallelogram using a user defined angle
    :param turt: a turtle
    :param angle: user's defined angle
    :return: a drawing of a parallelogram
    """
    for num in range(2):
        turt.forward(100)
        turt.left(angle)
        turt.forward(50)
        turt.left(calc_angle(angle))


def get_angle():
    """
    Asks for an angle input for the parallelogram
    :return: an integer
    """
    angle = int(input("What do you want the angle of the parallelogram to be?"))
    return angle

def calc_angle(angle):
    """
    Takes an orignal angle and calculates its supplementary angle
    :param angle: The original angle
    :return: an integer
    """
    newangle = 180-angle        # this gets the supplementary angle of the original angle
    return newangle

# TODO      Before submitting, be sure to check the instructions above in the header
# TODO      to ensure you completed all five requirements



def main():
    turt = turtle.Turtle()
    window = turtle.Screen()
    angle = get_angle()
    draw_parallelogram(turt, angle)
    window.exitonclick()

main()
