######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T4: Unit Testing
# Purpose: Demonstration of using division and modulus operations,
# This program incorrectly calculates the largest number of
# quarters, dimes, nickels and pennies needed to make that change in coins.
# It is designed to show a subtle error and the value of unit tests.
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """

    # This function works correctly--it is verbatim from the text, chapter 6
    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def i_steal_pennies_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the is_i_steal_pennies() function,
    returning True only when the input is even.

    :return: None
    """
    print("\nRunning i_steal_pennies_test_suite()).")
    # Remember that I_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    testit(i_steal_pennies(0.88)==[3, 1, 0, 3]) # because 0.88 = 3*0.25 + 1*0.10 + 0*0.05 + 3*0.01
    testit(i_steal_pennies(0.89)==[3, 1, 0, 4]) # because 0.89 = 3*0.25 + 1*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.99)==[3, 2, 0, 4]) # because 0.99 = 3*0.25 + 2*0.10 + 0*0.05 + 4*0.01

    # TODO Add more unit tests here
    testit(i_steal_pennies(0.96)==[3, 2, 1, 1])  # because 0.96 = 3*0.25 + 2*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.86)==[3, 1, 1, 1])  # because 0.86 = 3*0.25 + 1*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.76)==[3, 0, 1, 1])  # because 0.76 = 3*0.25 + 0*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.66)==[2, 1, 1, 1])  # because 0.66 = 2*0.25 + 1*0.10 + 1*0.05 + 1*0.01
    testit(i_steal_pennies(0.56)==[2, 0, 1, 1])  # because 0.56 = 2*0.25 + 0*0.10 + 1*0.05 + 1*0.01
    testit(i_steal_pennies(0.46)==[1, 2, 1, 1])  # because 0.46 = 1*0.25 + 2*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.36)==[1, 1, 1, 1])  # because 0.36 = 1*0.25 + 1*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.26)==[1, 0, 1, 1])  # because 0.26 = 1*0.25 + 0*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.16)==[0, 1, 1, 1])  # because 0.16 = 0*0.25 + 1*0.10 + 0*0.05 + 1*0.01
    testit(i_steal_pennies(0.06)==[0, 0, 1, 1])  # because 0.06 = 0*0.25 + 0*0.10 + 1*0.05 + 1*0.01

    testit(i_steal_pennies(0.97)==[3, 2, 0, 2])  # because 0.97 = 3*0.25 + 2*0.10 + 1*0.05 + 2*0.01
    testit(i_steal_pennies(0.87)==[3, 1, 0, 2])  # because 0.87 = 3*0.25 + 1*0.10 + 0*0.05 + 2*0.01
    testit(i_steal_pennies(0.77)==[3, 0, 0, 2])  # because 0.77 = 3*0.25 + 0*0.10 + 0*0.05 + 2*0.01
    testit(i_steal_pennies(0.67)==[2, 1, 1, 2])  # because 0.67 = 2*0.25 + 1*0.10 + 1*0.05 + 2*0.01
    testit(i_steal_pennies(0.57)==[2, 0, 1, 2])  # because 0.57 = 2*0.25 + 0*0.10 + 1*0.05 + 2*0.01
    testit(i_steal_pennies(0.47)==[1, 2, 0, 2])  # because 0.47 = 1*0.25 + 2*0.10 + 1*0.05 + 2*0.01
    testit(i_steal_pennies(0.37)==[1, 1, 0, 2])  # because 0.37 = 1*0.25 + 1*0.10 + 0*0.05 + 2*0.01
    testit(i_steal_pennies(0.27)==[1, 0, 0, 2])  # because 0.27 = 1*0.25 + 0*0.10 + 0*0.05 + 2*0.01
    testit(i_steal_pennies(0.17)==[0, 1, 1, 2])  # because 0.17 = 0*0.25 + 1*0.10 + 1*0.05 + 2*0.01
    testit(i_steal_pennies(0.07)==[0, 0, 1, 2])  # because 0.07 = 0*0.25 + 0*0.10 + 1*0.05 + 2*0.01

    testit(i_steal_pennies(0.99)==[3, 2, 0, 4])  # because 0.99 = 3*0.25 + 2*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.89)==[3, 1, 0, 4])  # because 0.89 = 3*0.25 + 1*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.79)==[3, 0, 0, 4])  # because 0.79 = 3*0.25 + 0*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.69)==[2, 1, 1, 4])  # because 0.69 = 2*0.25 + 1*0.10 + 1*0.05 + 4*0.01
    testit(i_steal_pennies(0.59)==[2, 0, 1, 4])  # because 0.59 = 2*0.25 + 0*0.10 + 1*0.05 + 4*0.01
    testit(i_steal_pennies(0.49)==[1, 2, 0, 4])  # because 0.49 = 1*0.25 + 2*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.39)==[1, 1, 0, 4])  # because 0.39 = 1*0.25 + 1*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.29)==[1, 0, 0, 4])  # because 0.29 = 1*0.25 + 0*0.10 + 0*0.05 + 4*0.01
    testit(i_steal_pennies(0.19)==[0, 1, 1, 4])  # because 0.19 = 0*0.25 + 1*0.10 + 1*0.05 + 4*0.01
    testit(i_steal_pennies(0.09)==[0, 0, 1, 4])  # because 0.09 = 0*0.25 + 0*0.10 + 1*0.05 + 4*0.01


    print("Run of i_steal_pennies_test_suite() complete.")

def i_steal_pennies(to_change):
    """
    This function looks like it should take a floating point number to_change
    and return a list of how much change to give as [num_quarters, num_dimes, num_nickels, num_pennies]

    However, it compounds small truncation errors of the floating point arithmetic.
    Such errors are subtle and can be quite hard to debug, so unit tests are useful!
    A better algorithm would be to use integers instead of floats,
    but the point of this assignment is NOT just to fix the error.
    It IS to help you learn to use and to value unit tests.

    :param to_change: a float representing an amount of money
    :return: A list of the number of quarters, dimes, nickels,
             and pennies representing the amount of money above
    """
    # TODO DO NOT CHANGE THIS FUNCTION

    # Initialize values
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    # Compute numbers of each coin type
    if(to_change >= 0.25):
        num_quarters = int(to_change / 0.25)
        to_change = float(to_change % 0.25)
    if(to_change >= 0.1):
        num_dimes = int (to_change / 0.1)
        to_change = float(to_change % 0.1)
    if(to_change >= 0.05):
        num_nickels = int(to_change / 0.05)
        to_change = float(to_change % 0.05)
    if(to_change >= 0.01):
        num_pennies = int(to_change / 0.01)
    return([num_quarters, num_dimes, num_nickels, num_pennies]) #  this order will be retained


def print_change(coinlist):
    """
    This program expects an input coin list of [num_quarters, num_dimes, num_nickels, num_pennies]
    It will print the values out for the user.

    :param coinlist: A list of the number of quarters, dimes, nickels,
                     and pennies representing the amount of money above
    :return: None
    """

    print("Can you tell if I am an honest machine? ")
    print("Give out the following change: ")
    valuelist=["Quarter(s): ", "Dime(s): ", "Nickel(s): ", "Penny(s): "]
    for item in range(4):
        print(valuelist[item]+str(coinlist[item]))


def user_input_of_coins():
    """
    This function is created just for interactive fun--use the unit tests instead!

    :return: None
    """

    thetotal=float(input("Input total amount of dollars and cents (e.g., 2.45): "))
    print("You have asked how to make "+ str(thetotal)+ " in change.")
    list_of_change=i_steal_pennies(thetotal)
    print_change(list_of_change)


def main():
    """
    This main function is intended to test the correctness of the i_steal_pennies() function

    :return:
    """
    user_input_of_coins()    # can be used interactively just for fun, but use the test_suite to document your testing!
    i_steal_pennies_test_suite()

main()
