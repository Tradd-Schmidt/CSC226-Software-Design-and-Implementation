from Final_Project import ASCIICode

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
      is_binary()
      is_div_by_sevens()
      split_into_sevens()
      extract_text(text)
    :return: None
    """
    test = ASCIICode("10011")
    # Testing the is_binary()
    print("Testing is_binary()")
    test_it(test.is_binary() == True)
    test.text = "0110310"
    test_it(test.is_binary() == False)

    # Testing the is_div_by_sevens()
    print("Testing is_div_by_sevens()")
    test.text = "1001011"
    test_it(test.is_div_by_sevens() == True)
    test.text = "Hello W"
    test_it(test.is_div_by_sevens() == True)
    test.text = "1101"
    test_it(test.is_div_by_sevens() == False)
    test.text = "Hello World"
    test_it(test.is_div_by_sevens() == False)

    # Testing the split_into_sevens()
    print("Testing split_into_sevens()")
    test.text = "0110000"
    test_it(test.split_into_sevens() == [0, 1, 1, 0, 0, 0, 0])
    test.text = "0110011"
    test_it(test.split_into_sevens() == [0, 1, 1, 0, 0, 1, 1])

    # Testing the extract_text(text)
    print("Testing extract_text(text)")
    test_it(test.extract_text("Hello World") == ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"])

    # Testing add_parity(text)
    print("Testing add_parity()")
    test_it(test.add_parity("1001011") == [0, 1, 0, 0, 1, 0, 1, 1])
    test_it(test.add_parity("0001000") == [1, 0, 0, 0, 1, 0, 0, 0])

    # Testing the convert_to_ascii()
    print("Testing convert_to_ascii()")
    test.text = "Okay!"
    test_it(test.convert_to_ascii() == [[1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 1]])
parity_test_suite()
