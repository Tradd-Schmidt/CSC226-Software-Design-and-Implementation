######################################################################
# Author: Dr. Scott Heggen              TODO: Change this to your name, if modifying
# Username: heggens                     TODO: Change this to your username, if modifying
#
# Assignment: T3: Boustrophedon Turtles
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# original from http://openbookproject.net/thinkcs/python/english3e/functions.html
#
# Modifications by Dr. Jan Pearce
# converted to Windows, removed def function, added Screen for clean close
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def draw_multicolor_square(t, sz):
    """
    Draws a multicolor square of size sz
    :param t: a turtle object
    :param sz: the size of a side
    :return: None
    """
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)


def main():
    """Makes a multicolored spiralling set of squares"""
    wn = turtle.Screen()        # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    wn.title("Dancing Squares!")

    tess = turtle.Turtle()      # Create tess and set some attributes
    tess.pensize(3)

    size = 20                   # Size of the smallest square
    for i in range(15):
        draw_multicolor_square(tess, size)
        size = size + 10        # Increase the size for next time
        tess.forward(10)        # Move tess along a little
        tess.right(18)          #    and give her some turn

    wn.exitonclick()


main() # Calls the main function
