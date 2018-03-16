######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#

import turtle

wn = turtle.Screen()            #Creates Turtle screen
wn.bgcolor("black")             #Sets bg color to Aqua

friend = turtle.Turtle()
friend.hideturtle()
friend.speed(0)

friend.penup()
friend.right(180)
friend.forward(200)
for l in ("red", "yellow", "blue", "green", "purple", "orange", "pink", "brown", "grey", ):
    friend.pendown()
    friend.color(l)                 #Changes the color of the friend on each instance
    friend.left(45)                 #Creates the legs
    friend.forward(30)
    friend.forward(-30)
    friend.left(90)
    friend.forward(30)
    friend.forward(-30)
    friend.left(135)
    friend.forward(60)              #Creates the body
    friend.right(155)
    friend.forward(50)              #Creates the arms
    friend.forward(-50)
    friend.right(50)
    friend.forward(50)
    friend.forward(-50)
    friend.right(65)
    for i in range(120):            #Draws the head of the friends
        friend.forward(1)
        friend.right(3)
    friend.left(90)                 #Sets up for a new friend to be drawn
    friend.forward(60)
    friend.left(90)
    friend.penup()
    friend.forward(50)
    friend.right(180)
friend.color("#00FFFF")
friend.setpos(0, -100)
friend.write("My Friends", move=False, align='center', font=("Comic Sans", 20, ("bold", 'normal')))  #"Writes My Friends"

wn.exitonclick()
