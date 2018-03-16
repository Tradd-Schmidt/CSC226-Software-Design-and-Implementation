######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T5: Buggy Fruit
# Purpose: A program to practice debugging on
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# Modified from: http://inventwithpython.com/chapter7.html
# for debugging practice
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random


def display_result(n1, n2, sum):
    """
    Displays the results of the calculation, and whether it is correct or not.

    :param n1: a random integer
    :param n2: another random integer
    :param sum: a third random integer
    :return: None
    """

    print ("The first number was ", n1)
    print ("The second number was ", n2)
    print ("The computer guessed ", int(n1), " + ", int(n2), " = ", int(sum))
    if sum == n1 + n2:
        print('Correct!')
    else:
        print('Wrong!')


def main():
    """
    Calculates the sum of two random numbers, compares it to a random sum. Should be correct 25% of the time

    :return: None
    """
    number1 = random.randint(1, 2)
    number2 = random.randint(1, 2)

    answer = random.random() * 4
    display_result(number1, number2, answer)

main()
