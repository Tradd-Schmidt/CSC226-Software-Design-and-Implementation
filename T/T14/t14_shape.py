import turtle


class Shape:
    """
    A class to draw a shape
    """
    def __init__(self, side_length, num_of_sides, color=(0, 0, 0), posn=(0, 0), speed=9):
        """
        Initializes a shape with starting point as start_point, size as side length, number of sides as num_of_sides,
        and color values as color
        :param color: an tuple which will change the color of the turtle
        :param posn: an integer which is the starting point of the shape
        :param side_length: an integer which is the length of each side
        :param num_of_sides: an integer which is how many sides there will be
        """
        self.x, self.y = posn
        self.size = side_length
        self.sides = num_of_sides
        self.color = color
        self.speed = speed


    def draw_shape(self):
        """
        Draws a shape based on the number of sides there will be and the length of the sides
        :return:
        """
        t = turtle.Turtle()
        t.color(self.color)
        t.speed = self.speed
        t.pu()

        t.goto(self.x, self.y)
        t.pd()
        for i in range(self.sides):
            t.fd(self.size)
            t.left(360 / self.sides)
        t.hideturtle()
