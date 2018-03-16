######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: A7: UPC Bar Codes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import string, sys


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def reverse_list_test_suite():
    print("Testing clean_string_to_list() function")
    testit(clean_string_to_list("A test string") == ["a", "test",  "string"])
    testit(clean_string_to_list("A string, with punctuation? It's true!") == ["a", "string", "with", "punctuation", "its", "true"])

    print("Testing reverse() function")
    testit(reverse(["a", "list", "in", "order"]) == ["order", "in", "list", "a"])
    testit(reverse(["another", "fine", "example"]) == ["example", "fine", "another"])

    print("End of the test suite")


def clean_string_to_list(in_string):
    """
    Removes all punctuation from the list, and converts it to a list.
    Typically, you wouldn't combine two functions in one (removing punctuation AND converting to list).
    :param in_string: A string to strip and convert
    :return: A list, representing each word in the original string
    """
    # Code modified from Chapter 8 on Strings; how to strip punctuation
    s_without_punct = ""
    for letter in in_string:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct.lower().split()          # I did something cute here with two methods. Do you see it?


def reverse(input_list):
    """
    Reverses a list

    :param input_list: A list of strings (any list would work though)
    :return: A list, in reverse order
    """
    output_list = []
    list_length = len(input_list)
    for index in range(list_length-1, -1, -1):      # Pay attention to the range here; why'd I do this?
        # print input_list[index]                   # For testing purposes only
        output_list.append(input_list[index])
    return output_list


def main():
    """
    A program to strip a string of punctuation and reverse it
    :return: None
    """
    in_string = "Enter a string's text here, to test the string!"
    converted_string = clean_string_to_list(in_string)
    reversed_list = reverse(converted_string)
    print(" ".join(reversed_list))

    # reverse_list_test_suite()                     # Uncomment this test suite to test the fruitful functions.


main()
