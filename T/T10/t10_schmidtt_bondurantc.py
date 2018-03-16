######################################################################
# Author: Tradd Schmidt and Conner Bondurant     TODO: Change this to your names
# Username: schmidtt and bondurantc            TODO: Change this to your usernames
#
# Assignment: T10: Oh, the Places You'll Go!
#
# Purpose:  To create a map of locations
#           where the user is originally from or has visited,
#           and to use tuples and lists correctly.
######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle


def parse_file(filename):
    """
    Opens a text file, adds the contents into tuples, and then places the tuples into a list
    :param filename: name of the file
    :return: a list
    """
    # FIXME: Add an appropriate docstring for this function.

    file_content = open(filename, 'r')           # Opens file for reading

    str_num = file_content.readline()           # The first line of the file is the number of entries
    str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

    places_list = []
    for i in range(str_num):
        places_list.append(extract_place(file_content))         # Assembles the list of places

    file_content.close()
    return places_list


def extract_place(file_content):
    # FIXME: Add an appropriate docstring for this function
    """
    Takes contents of a file and puts them into a formated tuple
    :param file_content: the content of a file to be put into a tuple
    :return: a tuple
    """
    name = file_content.readline()
    name = name[:-1]
    desc = file_content.readline()
    desc = desc[:-1]
    x = file_content.readline()
    x = float(x[:-1])
    y = file_content.readline()
    y = float(y[:-1])
    color = file_content.readline()
    color = color[:-1]

    place_tuple = (name, desc, x, y, color)
    # TODO   Parse the file, line by line. You can read each line of the file using the code above on line 27.
    # TODO   The order of the lines are: name, location, latitude, longitude, and user color.
    # TODO   Just like above (line 28), you need to remove the last character (\n).
    # TODO   Place the elements into the tuple below, and return the tuple.
    return place_tuple


def place_pin(window, place):
    """
    This function places a pin on the world map.

    :param window: the window object where the pin will be placed
    :param place: a tuple object describing a place to be put on the map
    :return: None
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    pin = turtle.Turtle()
    pin.penup()
    pin.color(place[4])                     # Set the pin to user's chosen color
    pin.shape("circle")                     # Sets the pin to a circle shape

    # Logically, the denominator for longitude should be 360; lat should be 180.
    # These values (195 and 120) were determined through testing to account for
    # the extra white space on the edges of the map. You shouldn't change them!

    pin.goto((place[3] / 195) * window.window_width() / 2, (place[2] / 120) * window.window_height() / 2)
    pin.stamp()                             # Stamps on the location

    text = "{0}'s place:\n    {1}".format(place[0], place[1])   # Setting up pin label
    pin.write(text, font=("Arial", 10, "bold"))                 # Stamps the text describing the location


def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list
    to make iterating through all the t11_places and adding them to the map easier.

    :return: None
    """

    # The next three lines set up the world map
    wn = turtle.Screen()
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.bgpic("world-map.gif")

    # A sample file was created for you to use here: places.txt
    in_file = input("Enter the name of the file: ")
    place_list = parse_file(in_file)        # generates place_list from the file

    # Iterates through each item in the list, calling the place_pin() function
    for place in place_list:
        place_pin(wn, place)  # Adds ONE place to the map for each loop iteration

    print("Map created!")
    wn.exitonclick()


main()
