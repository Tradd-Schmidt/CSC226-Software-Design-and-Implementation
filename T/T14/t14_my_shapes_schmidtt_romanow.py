import turtle
import t14_shape as shape


def main():
    wn = turtle.Screen()
    wn.colormode(255)
    x = shape.Shape(1, 360, speed=0)
    x.draw_shape()
    x.size = .1
    x.color = (100, 255, 150)
    x.x = -25
    x.y = 75
    x.draw_shape()
    x.x = 25
    x.y = 75
    x.draw_shape()
    x.sides = 2
    x.x = -10
    x.y = 20
    x.draw_shape()
    wn.exitonclick()


main()
