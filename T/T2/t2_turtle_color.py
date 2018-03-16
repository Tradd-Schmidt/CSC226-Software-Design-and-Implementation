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

wn = turtle.Screen()             # creates a graphics window--needed for a clean close

wn.bgcolor("lightgreen")        # Set the window background color
wn.title("Hello, Tess!")        # Set the window title

tess = turtle.Turtle()          # create a turtle named tess
tess.color("blue")              # Tell tess to change her color
tess.pensize(3)                 # Tell tess to set her pen width

tess.forward(50)                # Move tess around
tess.left(120)
tess.forward(50)

# for clean closing of the Screen
wn.exitonclick()
