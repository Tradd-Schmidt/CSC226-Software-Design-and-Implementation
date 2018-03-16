######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Exam 2
#
# This code simulates a television. Update the class, and use it appropriately.
# ######################################################################
# Acknowledgements:
#
# Original code written by Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
#
# Instructions (25 points total):
# 1) Update the Television class so you can store the size of the Television as an instance variable (3 points)
# 2) Update the Television class so the size of the television (e.g., 42) is an input parameter in the initializer(3 points)
# 3) Create a class method that allows the user to turn the television on and off (4 points)
# 4) Complete the six TODOs in the main() function (12 points; 2 points per TODO)
# 5) Make sure the docstring is up-to-date for any method you create or update (3 points)
#
####################################################################################


class Television:
    """
    A class to describe a Television.
    """
    def __init__(self, channel, size, state=False):
        """
        Initializer method for creating new televisions
        :param channel: the current channel
        :param size: the size of the t.v.
        :param state: the state of the television, True = on, False = off
        """

        self.state = state          # True is on, False is off
        self.current_channel = channel
        self.volume = 10
        self.size = size

    def change_channel(self, up_or_down):
        """
        Changes the channel either up ("+") or down ("-")
        :param up_or_down: "+" or "-" for up or down
        :return: None
        """
        if up_or_down == "+":
            self.current_channel += 1
            print("You are on channel {0}".format(self.current_channel))
        elif up_or_down == "-":
            self.current_channel -= 1
            print("You are on channel {0}".format(self.current_channel))
        else:
            print("Error: Invalid channel operation")

    def change_volume(self, up_or_down):
        """
        Changes the volume either up ("+") or down ("-")
        :param up_or_down: "+" or "-" for up or down
        :return: None
        """
        if up_or_down == "+":
            self.volume += 1
            print("The volume is at {0}".format(self.volume))
        elif up_or_down == "-":
            self.volume -= 1
            print("The volume is at {0}".format(self.volume))
        else:
            print("Error: Invalid volume operation")

    def power(self):
        """
        Allows the user to turn the tv on and off
        :return: None
        """
        if self.state:
            self.state = False
            print("The power is now off.")
        elif not self.state:
            self.state = True
            print("The power is now on.")
# end class


def main():
    """
    The main function, for creating new televisions and using them
    :return: None
    """

    # A new TV!
    # TODO Update the tv object below to indicate it is a 42 inch television.
    tv = Television(5, state=True, size=42)            # Turns the television on to channel 5

    # TODO Change the channel to channel 8
    tv.change_channel("+")
    tv.change_channel("+")
    tv.change_channel("+")

    # TODO Turn the volume to 7
    tv.change_volume("-")
    tv.change_volume("-")
    tv.change_volume("-")
    # TODO Turn off the tv object. Time to go shopping!
    tv.power()
    # TODO Time for an upgrade. Create a new Television object, and set its size to 50 inches
    new_tv = Television(0, 50)
    # TODO turn on your new tv, and enjoy the rest of your Wednesday.
    new_tv.power()
if __name__ == "__main__":
    main()
