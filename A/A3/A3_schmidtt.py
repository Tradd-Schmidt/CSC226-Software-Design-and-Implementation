######################################################################
# Author: Tradd Schmidt     TODO: Change this to your names
# Username: schmidtt           TODO: Change this to your usernames
#
# Assignment: A3: A Pair of Psychedelic Functional Robotic Turtles

import turtle

def make_turtle():
    """

    This is used to make a turtle.
    Returns a turtle.

    :return: A turtle object
    """
    sheldon = turtle.Turtle()
    turtle.colormode(255)
    sheldon.color(0, 200, 240)
    sheldon.speed(0)
    sheldon.penup()
    return sheldon

def make_foundation(t):
    """

    Makes a square which is the base of the house
    :param t: turtle

    :return:
    """
    t.pendown()
    for sz in range(4):
        t.fd(150)
        t.left(90)
    t.penup()

def make_roof(t):
    """

    Makes a triangle which is the top of the house
    :param t: A turtle
    :return:

    """
    t.pendown()
    t.right(30)
    for sz in range(3):
        t.fd(150)
        t.right(120)
    t.right(60)
    t.penup()

def make_window(t):
    """

    Makes a square with a horizontal and vertical line
    :param t: a turtle
    :return:

    """
    t.pendown()
    for sz in range(4):             # makes the square
        t.forward(20)
        t.left(90)
    for sz in range(2):             # makes the horizontal and vertical lines
        t.fd(10)
        t.left(90)
        t.fd(20)
        t.left(90)
        t.fd(10)
        t.left(90)
    t.penup()

def make_door(t):
    """

    Makes a door by making a rectangle and a circle for the handle
    :param t: A turtle
    :return:

    """
    t.pendown()
    for sz in range(2):             # makes the rectangle
        t.fd(40)
        t.left(90)
        t.fd(65)
        t.left(90)
    t.left(90)                      # sets up for the handle
    t.penup()
    t.fd(30)
    t.right(90)
    t.forward(10)
    t.pendown()
    for sz in range(36):            # makes the handle
        t.fd(1)
        t.left(10)
    t.penup()

def make_chimney(t):
    """

    Makes a chimney and cloud
    :param t: a turtle
    :return:

    """
    t.pendown()
    t.fd(60)                    # draws the first half of the chimney
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(3)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.fd(35)
    t.fd(-2)
    t.left(90)
    t.fd(10)
    t.right(90)
    t.fd(40)
    for sz in range(8):         # makes the cloud
        for i in range(45):
            t.forward(1)
            t.left(4)
        t.right(154)
    t.right(118)                # puts the turtle back to where it left off on the chimney
    t.right(90)
    t.fd(52)
    t.right(90)
    t.fd(12)
    t.left(90)
    t.fd(33)
    t.right(90)                 # finishes the chimney
    t.fd(5)
    t.right(90)
    t.fd(3)
    t.left(90)
    t.fd(81)
    t.right(90)
    t.fd(89)

def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    sheldon = make_turtle()
    sheldon.left(45)            # sets up for the foundation
    sheldon.fd(-100)
    sheldon.right(45)
    make_foundation(sheldon)    # makes the foundation
    sheldon.left(90)            # sets up for the roof
    sheldon.fd(150)
    make_roof(sheldon)          # makes the roof
    sheldon.right(90)           # sets up for the left window
    sheldon.fd(75)
    sheldon.left(90)
    sheldon.fd(30)
    make_window(sheldon)        # make the left window
    sheldon.left(90)            # sets up for the right window
    sheldon.fd(20)
    sheldon.left(90)
    sheldon.fd(50)
    make_window(sheldon)        # makes the right window
    sheldon.fd(20)              # sets up for the door
    sheldon.left(90)
    sheldon.fd(30)
    sheldon.right(90)
    sheldon.fd(5)
    make_door(sheldon)          # makes the door
    sheldon.fd(-65)             # sets up for the chimney and smoke
    sheldon.right(90)
    sheldon.fd(115)
    sheldon.right(90)
    make_chimney(sheldon)       # makes the chimney and smoke
    sheldon.hideturtle()        # hides the turtle so you can see the house

    wn.exitonclick()

main()
