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

wn = turtle.Screen()            # creates a graphics window
my_turtle = turtle.Turtle()     # create a turtle named myturtle

my_turtle.shape('turtle')       # shapes possible are 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
my_turtle.color('red')
#myturtle.hideturtle()

head = 0                       # initial heading for my_turtle
pen = 5                         # initial pensize for my_turtle
my_turtle.setheading(head)
my_turtle.pensize(pen)

my_turtle.forward(150)          # tell myturtle to move forward by 150 units
my_turtle.left(90)              # turn by 90 degrees
my_turtle.forward(75)           # complete the second side of a rectangle

wn.exitonclick()                # Added by Dr. Pearce. Closes the program when a user clicks in the window
