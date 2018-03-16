######################################################################
# Author: Dr. Scott Heggen              TODO: Change this to your name, if modifying
# Username: heggens                     TODO: Change this to your username, if modifying
#
# Assignment: A2: Loopy Turtles
#
# Purpose: To demonstrate the turtle library
######################################################################
# Acknowledgements:
#
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html
# first modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle
import random

wn = turtle.Screen()
wn.colormode(255)

tList = []                      # makes an empty list
head = 0                        # facilitates geometric angles
numTurtles = 10                 # since the turtles spiral, numTurtles = # spirals

for i in range(numTurtles):
    nt = turtle.Turtle()        # Make a new turtle, initialize values
    nt.setheading(head)
    nt.pensize(2)

    nt.color(random.randrange(256),random.randrange(256),random.randrange(256))
    nt.speed(10)
    wn.tracer(30,0)             # modified by Dr. Heggen; in Python 3, is a method of Screen, not Turtle
    tList.append(nt)            # Add the new turtle to the list
    head = head + 360/numTurtles

dist = 15
for angle in range(100):        # moveTurtles(tList,dist,angle) function removed by Dr. Jan Pearce
    for tur in tList:           # Make every turtle on the list do the same actions.
        tur.forward(dist)
        tur.right(angle)

w = tList[0]
w.up()

w.setpos(0,40)                                                                                # was w.goto(-130,40) modified by by Dr. Pearce to make functional in Windows
w.write("How to Think Like a ",move=False,align='center',font=("Arial",30,("bold","normal"))) # altered by Dr. Pearce to make font size work in Windows
w.setpos(0,-35)                                                                               # was goto(-130,-35) modified by by Dr. Pearce to make functional in Windows
w.write("Computer Scientist",move=False,align='center',font=("Arial",30,("bold","normal")))  # altered by Dr. Pearce to make font size work in Windows

wn.exitonclick()



