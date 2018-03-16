######################################################################
# Author: Tradd Schmidt and Will Romano      TODO: Change this to your names
# Username: schmidtt and romanow         TODO: Change this to your usernames
#
# Assignment: T14: Crazy Shapes
#
#
# Purpose: A class for creating rectangles. Collaborates with the Points class
######################################################################
# Acknowledgements:
#
# Much of the code is originally from: http://openbookproject.net/thinkcs/python/english3e/

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


class Rectangle:
    """
    A class to manufacture rectangle objects.
    """

    def __init__(self, posn, w, h):
        """
         Initialize rectangle at posn, with width w, height h
        :param posn: a Point object representing the starting point of the rectangle
        :param w: the rectangle width
        :param h: the rectangle height
        """
        self.corner = posn          # A Point object to hold the bottom left corner of the rectangle
        self.width = w
        self.height = h

    def __str__(self):
        '''
        Overridden string class which allows the user to use str() to print cleanly.

        :return: A formatted string
        '''

        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """
        Grow (or shrink) this object by the deltas

        :param delta_width: change in the width
        :param delta_height: change in the height
        :return: None
        """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """
        Move this object by the deltas.

        :param dx: change in the x coordinate
        :param dy: change in the y coordinate
        :return: None
        """
        self.corner.x += dx
        self.corner.y += dy

    def draw_rectangle(self, r=0, g=0, b=0, angle=0, text = ""): # black is the default color
        """
        Instantiates a Turtle object and draws the Rectangle on the Screen at an angle, and tags it with a text.
        Notice the turtle is implemented differently here than in the Point class,
        as a demonstration of the many ways in which we can implement the same thing.

        :param r: the red channel
        :param g: the green channel
        :param b: the blue channel
        :param angle: the angle to draw the turtle
        :param text: any additional text to write
        :return: None
        """
        turt = turtle.Turtle()
        turt.color(r, g, b)
        turt.penup()

        # self.corner refers to a Point object, so self.corner.x refers to the x-coordinate;
        # self.corner.y refers to the y-coordinate
        turt.goto(self.corner.x, self.corner.y)

        # rotates to turtle by angle degrees
        turt.left(angle)
        turt.showturtle()
        turt.pendown()

        # draws the rectangle to the screen
        for i in range(2):
            turt.forward(self.width)
            turt.left(90)
            turt.forward(self.height)
            turt.left(90)

        # writes custom text to the screen if provided;
        # else prints the starting coordinates, width, and height of the rectangle
        if text == "":
            turt.write(str(self), True)
        else:
            turt.write(text, True)
        turt.hideturtle()
# end class
