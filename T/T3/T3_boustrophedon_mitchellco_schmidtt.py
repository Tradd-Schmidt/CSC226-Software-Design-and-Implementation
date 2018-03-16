######################################################################
# Authors: Cody Mitchell
#          Tradd Schmidt

# Username: mitchellco
#           schmidtt
#
# Assignment: T3: Boustrophedon Turtles
#
# Purpose: To fill a square with alternating lines.
######################################################################
# Acknowledgements:
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle,random

def fillBox(t, s, ps):
    """
    Draws the filled box function
    :param t: the turtle used
    :param s:size of square
    :param ps: pensize
    :return: None
    """
    t.penup()
    t.pensize(ps)

    # DRAW FILLING
    in_s=s-(ps*2)                        # THE INNER SQUARE SIZE
    t.pencolor("blue")
    t.penup()
    t.setpos(-s/2+ps,-s/2+ps)
    t.pendown()
    for i in range(round(s/(ps*2))):     # LOOPS TO FILL THE SQUARE
        t.left(90)
        t.forward(in_s)
        t.right(90)
        t.forward(ps)
        t.right(90)
        t.forward(in_s)
        t.left(90)
        if i != round(s/(ps*2))-1:       # FINISHES THE END OF THE LOOP
            t.forward(ps)

    # DRAW SQUARE
    t.penup()
    t.setpos(-s/2,-s/2)
    t.pencolor("red")
    t.pendown()
    for i in range(4):
        t.forward(s)
        t.left(90)
    t.penup()

def main():
    wn=turtle.Screen()
    t=turtle.Turtle()
    t.speed(0)

    t.penup()
    for i in range(100):
        t.setpos(random.randint(-341,341),random.randint(-288,288))
        t.color("purple")
        t.write("CSC IS FUN", move=False, align="center", font=("Arial", random.randint(8,50), "normal"))

    fillBox(t,500,20)
    wn.exitonclick()


main()
