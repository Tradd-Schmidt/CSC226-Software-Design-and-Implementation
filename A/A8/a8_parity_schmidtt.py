
######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# Assignment: A8: Error Detection
#
# Purpose: TODO: update this later
#
######################################################################


import sys


def test_it(did_pass):
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


def parity_test_suite():
    """
    The parity_test_suite() is designed to test the following:
      is_binary(strng)
      is_div_by_sevens(strng)
      split_into_sevens(strng)
    :return: None
    """
    # Testing the is_binary(strng)
    print("Testing is_binary(strng)")
    test_it(is_binary("0110000") == True)
    test_it(is_binary("0110001") == True)
    test_it(is_binary("0110310") == False)
    test_it(is_binary("1010700") == False)
    test_it(is_binary("1011100") == True)

    # Testing the is_div_by_sevens(strng)
    print("Testing is_div_by_sevens(strng)")
    test_it(is_div_by_sevens("0110000") == True)
    test_it(is_div_by_sevens("01100011") == False)
    test_it(is_div_by_sevens("0110010") == True)
    test_it(is_div_by_sevens("10100") == False)
    test_it(is_div_by_sevens("1011100") == True)

    # Testing the split_into_sevens(strng)
    print("Testing split_into_sevens(strng)")
    test_it(split_into_sevens("0110000") == [0, 1, 1, 0, 0, 0, 0])
    test_it(split_into_sevens("0110011") == [0, 1, 1, 0, 0, 1, 1])
    test_it(split_into_sevens("1010001") == [1, 0, 1, 0, 0, 0, 1])
    test_it(split_into_sevens("0110110") == [0, 1, 1, 0, 1, 1, 0])
    test_it(split_into_sevens("0101010") == [0, 1, 0, 1, 0, 1, 0])


def is_binary(strng):
    """
    Takes a string and tests to see if there are only 1s and 0s in the string
    :param strng: a string to be tested
    :return: A boolean
    """
    for i in strng:
        if i == "0" or i == "1":
            pass
        else:
            return False
    return True


def is_div_by_sevens(strng):
    """
    Checks to see if the length of a string is 7 characters long
    :param strng: a string to be tested
    :return: A boolean
    """
    if len(strng) > 7 or len(strng) % 7 != 0:
        return False
    else:
        return True


def split_into_sevens(strng):
    """
    Takes a string and splits the characters up and appends them to a list
    :param strng: a string
    :return: a list
    """
    l = []
    for i in strng:
        l.append(int(i))
    return l


def main():
    parity_test_suite()
    bin = "0110011"
    is_binary(bin)
    is_div_by_sevens(bin)
    split = split_into_sevens(bin)
    if sum(split) % 2 == 0:
        split_2 = [0]
        for i in split:
            split_2.append(i)
    elif sum(split) % 2 != 0:
        split_2 = [1]
        for i in split:
            split_2.append(i)
    print(split_2)


main()
