######################################################################
# Author: Tradd Schmidt and Nick Straub-Deck
# Username: schmidtt and straubdeckn
#
# Assignment: A7: UPC Bar Codes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################

import turtle


def check_code(code):
    """
    Checks to see if a user's input is a valid 12 digit code
    :param code: 12 digit code to be tested
    :return: True or False
    """
    if len(code) == 12:
        return True


def ask_for_input():
    """
    Asks a user to input a 12 digit number
    :return: The twelve digits as an integer
    """
    code = input("Please enter a 12 digit integer.")
    return code


def to_list(code):
    """
    Takes the twelve digit code and puts each number into a list
    :param code: twelve digit code as string
    :return: a list
    """
    l = []
    for i in code:
        l.append(i)
    return l


def check_upc(j):
    """
    Checks to see if the twelve digits is a valid UPC code
    :param j: a list
    :return: True
    """
    odd = int(j[0]) + int(j[2]) + int(j[4]) + int(j[6]) + int(j[8]) + int(j[10])
    even = int(j[1]) + int(j[3]) + int(j[5]) + int(j[7]) + int(j[9])
    odd *= 3
    sum = even + odd
    if sum % 10 != 0:
        modulo = 10 - (sum % 10)
    else:
        modulo = 0
    if modulo == int(j[11]):
        return True
    else:
        return False


def left_binary(num):
    """
    Takes a number and converts it to the corresponding left half binary
    :param num: an integer
    :return: return num in binary
    """
    x = 0
    if num == 0:
        x = "0001101"
    elif num == 1:
        x = "0011001"
    elif num == 2:
        x = "0010011"
    elif num == 3:
        x = "0111101"
    elif num == 4:
        x = "0100011"
    elif num == 5:
        x = "0110001"
    elif num == 6:
        x = "0101111"
    elif num == 7:
        x = "0111011"
    elif num == 8:
        x = "0110111"
    elif num == 9:
        x = "0001011"
    return x


def right_binary(num):
    """
    Takes a number and converts it to the corresponding right half binary
    :param num: an integer
    :return: return num in binary
    """
    x = 0
    if num == 0:
        x = "1110010"
    elif num == 1:
        x = "1100110"
    elif num == 2:
        x = "1101100"
    elif num == 3:
        x = "1000010"
    elif num == 4:
        x = "1011100"
    elif num == 5:
        x = "1001110"
    elif num == 6:
        x = "1010000"
    elif num == 7:
        x = "1000100"
    elif num == 8:
        x = "1001000"
    elif num == 9:
        x = "1110100"
    return x


def binary_to_list(str_list):
    """
    Takes a list of numbers converts to binary and then appends the binary numbers to a list
    :param str_list: a list of integers
    :return: a list of integers in binary
    """
    l = []
    count = 0
    for i in range(12):
        if count <= 5:
            l.append(left_binary(int(str_list[i])))
            count += 1
        else:
            l.append(right_binary(int(str_list[i])))
    return l


def make_turtle():
    """
    This is used to make a turtle.
    :return: A turtle object
    """
    sheldon = turtle.Turtle()
    wn = turtle.Screen()
    turtle.colormode(255)
    sheldon.color(0, 0, 0)
    sheldon.shape("square")
    sheldon.width(2)
    sheldon.speed(0)
    sheldon.penup()
    return (sheldon, wn)


def make_bar(turt, num, guardbar=False, length=5):
    """
    determines if a number will be a bar or space
    :param num: either 1 or 0
    :return: either a bar or space
    """

    if num == "0":
        turt.pu()
        turt.fd(2)
        turt.pd()
    elif num == "1":
        turt.pd()
        turt.left(90)
        turt.fd(50)
        turt.fd(-50)
        turt.right(90)
        turt.pu()
        turt.fd(2)
        turt.pd()
    if guardbar:
        if num == "0":
            pass
        elif num == "1":
            turt.pu()
            turt.fd(-2)
            turt.right(90)
            turt.pd()
            turt.fd(length)
            turt.fd(-length)
            turt.left(90)
            turt.pu()
            turt.fd(2)
            turt.pd()


def draw_barlines(turt, bc):
    """
    Takes a UPC code in binary form and draws the barcode for the UPC code
    :param turt: a turtle
    :param bc: a list or number as a string
    :return: none
    """
    turt.fd(-100)
    count = 0
    make_bar(turt, "1", True)
    make_bar(turt, "0", True)
    make_bar(turt, "1", True)

    for i in bc:
        count += 1
        if count == 7:
            make_bar(turt, "0", True)
            make_bar(turt, "1", True)
            make_bar(turt, "0", True)
            make_bar(turt, "1", True)
            make_bar(turt, "0", True)
        for num in i:
            make_bar(turt, num)
    make_bar(turt, "1", True)
    make_bar(turt, "0", True)
    make_bar(turt, "1", True)


def main():
    user_input = ask_for_input()
    while not check_code(user_input):
        print("That was not twelve digits long.")
        user_input = ask_for_input()
    (sheldon, wn) = make_turtle()
    if check_upc(to_list(user_input)):
        binary_upc = binary_to_list(to_list(user_input))
        draw_barlines(sheldon, binary_upc)
        sheldon.pu()
        sheldon.goto(0, -50)
        sheldon.write(user_input, move=False, align="center", font=("Arial", 25, ("bold", "normal")))
        sheldon.hideturtle()
        wn.exitonclick()
        sheldon.write
    else:
        sheldon.write("Error", move=False, align='center', font=("Arial", 30, ("bold", "normal")))
        wn.exitonclick()



main()
