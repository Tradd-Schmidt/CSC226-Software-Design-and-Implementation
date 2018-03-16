import sys

from t12_dots_schmidtt_klenki import *

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

def dots_test_suite():
    """
    The dots_test_suite() is designed to test the following:
      calculate_size(num_dots)
      is_valid_size(dot_width, dot_height, distance, screen_width, screen_height)
      draw_board(dot_distance, dottie, height, width)
      user_input(screen_height, screen_width)
    :return: None
    """

    # Testing the calculate_size(num_dots) function
    print("\nTesting calculate_size(num_dots)")
    testit(calculate_size(100) == (10, 10))
    testit(calculate_size(72) == (8, 9))
    testit(calculate_size(55) == (5, 11))

    # Testing the is_valid_size(dot_width, dot_height, distance, screen_width, screen_height) function
    print("\nTesting is_valid_size(dot_width, dot_height, distance, screen_width, screen_height)")
    testit(is_valid_size(5, 5, 5, 1000, 1000) == True)
    testit(is_valid_size(100, 5, 100, 10, 1000) == False)
    testit(is_valid_size(5, 100, 100, 1000, 10) == False)
    testit(is_valid_size(100, 100, 100, 10, 10) == False)

dots_test_suite()
