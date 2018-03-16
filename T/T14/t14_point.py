######################################################################
# Author: Tradd Schmidt and Will Romano      TODO: Change this to your names
# Username: schmidtt and romanow            TODO: Change this to your usernames
#
# Assignment: T14: Crazy Shapes
#
#
# Purpose: Demonstrates a small Point class and related main()
######################################################################
# Acknowledgements:
#
# Much of the code is originally from: http://openbookproject.net/thinkcs/python/english3e/

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle # needed by both point class and main()
import random # needed by main()


class Point:
    """ Point class represents and manipulates x,y coordinates.
        Is dependent upon the turtle libraries for draw_point() method.
        In particular, a Screen must exist and the color mode should be set to 255"""

    def __init__(self, x=0, y=0): # Each Point object has its own x and y coordinates and possibly a turtle
        """
        Creates a new point at x, y. If no x, y are given, the point is created at 0, 0

        :param x: the x coordinate
        :param y: the y coordinate
        """
        self.x = x
        self.y = y
        self.turtle = None # To save space we only create a turtle if and when draw_point() is used

    def __str__(self):
        """
         Makes the str() function work with Points

        :return: a formatted string
        """
        return "({0}, {1})".format(self.x, self.y)

    def distance_from_origin(self):
        """
        Compute my distance from the origin.

        :return: a float representing the distance from (0, 0)
        """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def user_set(self):
        """
        Allows the user to change the x and y value of a Point.

        :return: None
        """
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))

    def draw_point(self, r=0, g=0, b=0, text = ""): # black is the default color
        """
        Instantiates a Turtle object and draws the Point on the Screen.

        :param r: the red channel
        :param g: the green channel
        :param b: the blue channel
        :param text: text to write to the screen
        :return: None
        """
        self.turtle = turtle.Turtle()
        self.turtle.color(r, g, b)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.showturtle()
        self.turtle.stamp()

        # This code was added from the original point.py class
        # to allow custom text to be written to the screen
        if text == "":
            self.turtle.write(str(self), True)
        else:
            self.turtle.write(text, True)
        self.turtle.hideturtle()
# end class


def main():
    """
    Program demonstrates use of the Point class, when calling the code directly
    :return: None
    """

    p = Point()             # Instantiate an object of type Point at (0, 0)
    print("point = "+ str(p))

    q = Point(30, 40)       # Make a second point at (30, 40)
    print("point = " + str(q))

    wn = turtle.Screen()
    wn.colormode(255)       # change color modes

    p.draw_point()          # draw Point p as the default color of black
    q.draw_point(255, 0, 0) # draw Point q as red (255, 0, 0)

    print("\nPlease enter x and y values. To end enter x = 0 and y = 0.")
    while q.x != 0 or q.y != 0:
        q.user_set()
        print("point = " + str(q))
        q.draw_point(random.randrange(256), random.randrange(256), random.randrange(256))

    wn.bye()  # closes turtle window without requiring user click

if __name__ == "__main__":
    main()
