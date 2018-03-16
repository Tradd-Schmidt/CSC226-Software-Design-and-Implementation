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

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20
for i in range(30):          # range gives a list of 30 numbers from 0 to 29
    tess.stamp()             # Leave an impression on the canvas
    size = size + 3          # Increase the size on every iteration
    tess.forward(size)       # Move tess along
    tess.right(24)           #  ...  and turn her

# for clean closing of Turtle Screen
wn.exitonclick()
