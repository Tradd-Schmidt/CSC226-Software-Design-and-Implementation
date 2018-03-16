######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T4: Unit Testing
# Purpose: This program is designed to demonstrate testing of the of Boolean functions
# and the modulus (%) operator which gives the remainder following a division
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


def is_even(num):
    """
    Function intended to take an integer as input. Returns True if even and False if odd

    :param num: the integer to be tested
    :return: Boolean value representing if the number is even or not
    """
    if int(num) % 2 == 0:
        return True
    else:
        return False


def is_even_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the is_even() function, returning True
    only when the input is even.
    :return: None
    """
    print("\nRunning is_even_test_suite().")

    # testing of positive integers
    testit(is_even(1)==False)
    testit(is_even(2)==True)
    testit(is_even(10)==True)
    testit(is_even(99999)==False)

    # testing of 0 and negative integers
    testit(is_even(0)==True)
    testit(is_even(-1)==False)
    testit(is_even(-2)==True)
    testit(is_even(-11111)==False)

    print("Run of is_even_test_suite() complete.")


def main():
    """
    This main function is intended to test the correctness of the is_even function
    :return: None
    """

    is_even_test_suite()

main()
