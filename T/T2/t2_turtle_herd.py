######################################################################
# Author: Dr. Scott Heggen              TODO: Change this to your name, if modifying
# Username: heggens                     TODO: Change this to your username, if modifying
#
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html

# Assignment: T2: Exploring Turtles in Python
# Purpose: Introduces the use of the turtles library

######################################################################
# Acknowledgements:

# originally modified by Dr. Jan Pearce
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.

######################################################################

import turtle                   # allows us to use the turtles library

wn = turtle.Screen()            # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("tess & alex")

tess = turtle.Turtle()          # Create tess "instance" and set some attributes for tess
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()          # Create alex "instance"

tess.forward(80)                # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                  # Completes the triangle

tess.penup()
tess.right(180)                 # Turn tess around
tess.forward(80)                # Move her away from the origin


alex.forward(50)                # Make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

# for clean closing of Turtle Screen
wn.exitonclick()
