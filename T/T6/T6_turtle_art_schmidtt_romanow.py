######################################################################
# Author: Tradd Schmidt and Will Romano      TODO: Change this to your names
# Username: schmidtt and romanow             TODO: Change this to your usernames
#
# Assignment: T6: Turtle Art
# Purpose: Create beautiful works of art through code, namely iterations
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random


def draw_ngon(turt, sds, angle):
    # FIXME modify this function so that it's more generalized
    """
    Draws a randomly colored polygon using the turtle library

    :param turt: a turtle object to draw with
    :param sds: how many sides the ngon will have
    :param angle: the angle of each vertex
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))     # gives the turtle a random color

    turt.begin_fill()
    for num in range(sds):
        turt.forward(360//sds)
        turt.left(angle)           # the angle ensures a perfect hexagon
    turt.end_fill()


def calc_angle(sds):
    """
    Calculates the angle of the shape's vertices based on the number of sides
    :param sds: An input from the user which  is the number of sides for the shape
    :return: angle
    """
    angle = 360//sds
    return angle


def main():
    # FIXME modify the docstring so it's correct for your final code
    """
    The main function which draws 10 hexagons

    :return: None
    """
    t = turtle.Turtle()
    t.speed(0)
    wn = turtle.Screen()
    # Draws 10 hexagons
    while True:
        for num in range(10):
            sds = random.randint(3, 8)
            angle = calc_angle(sds)
            t.penup()
            # Move the turtle to a random place on the screen
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.pendown()
            draw_ngon(t, sds, angle)

    wn.exitonclick()

main()
