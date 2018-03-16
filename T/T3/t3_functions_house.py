######################################################################
# Author: Dr. Scott Heggen              TODO: Change this to your name, if modifying
# Username: heggens                     TODO: Change this to your username, if modifying
#
# Assignment: T3: Boustrophedon Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes and using images for shapes
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Dr. Jan Pearce - this file is modified from her original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library


def make_roof(wn, shape):
    """
    A new roof! (Made from an image of bricks)

    :param wn: a turtle screen object
    :param shape: a turtle object
    :return: None
    """
    wn.register_shape("Bricks.gif")         # Registers a shape so it can be used by the turtle library
    shape.setpos(80, 80)
    shape.shape("Bricks.gif")               # Sets the shape to the image registered above
    shape.stamp()

def make_main_house(shape):
    """
    Makes the main house rectangle.

    :param shape: a turtle object
    :return: None
    """

    shape.setpos(30, 47)
    shape.color('#3333FF')
    shape.begin_fill()
    for side in range(2):
        shape.forward(100)
        shape.right(90)
        shape.forward(140)
        shape.right(90)
    shape.end_fill()


def make_window(shape, x, y):
    """
    Adds a window to the house.

    :param shape: a turtle object
    :param x: the x coordinate of the window
    :param y: the y coordinate of the window
    :return: None
    """
    shape.penup()
    shape.setpos(x, y)             # TODO fix this to use X, Y
    shape.pendown()
    shape.color('#00ff22')
    shape.begin_fill()
    for side in range(2):
        shape.forward(30)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()


def make_door(shape):
    """
    Adds a door to the house.

    :param shape: a turtle object
    :return: None
    """
    shape.penup()
    shape.setpos(70, -42)
    shape.pendown()
    shape.color('#00ff22')
    shape.begin_fill()
    for side in range(2):
        shape.forward(20)
        shape.right(90)
        shape.forward(50)
        shape.right(90)
    shape.end_fill()


def make_deck(wn, shape):
    """
    Adds a deck to the house.

    :param wn: a turtle screen object
    :param shape: a turtle object
    :return: None
    """
    wn.register_shape("deck.gif")
    shape.penup()
    shape.setpos(175, -47)
    shape.shape("deck.gif")
    shape.stamp()
    shape.up()


def make_text(shape, txt):
    """
    writes text.

    :param shape: a turtle object
    :return: None
    """
    shape.color("#0F00F0")
    shape.setpos(70,120)
    shape.write(txt,move=False,align='center',font=("Arial",30,("bold","normal")))


def main():
    """
    Draws a house at x, y on the screen.

    :return: None
    """

    turtle.colormode(255)           # change color modes

    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgpic("Lighthouse.gif")      # Sets background to an image; must be a gif!
    shape = turtle.Turtle()
    shape.hideturtle()

    make_roof(wn, shape)
    make_main_house(shape)
    make_window(shape, 45, 0)
    make_window(shape, 88, 0)
    make_door(shape)
    make_deck(wn, shape)
    make_text(shape, "Dr. Jan's Chateau")

    wn.exitonclick()  # wait for a user click on the canvas


main() # call main()
