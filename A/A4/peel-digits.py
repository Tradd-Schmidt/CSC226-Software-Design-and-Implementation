#####################################################################################
# Author: Dr. Jan Pearce
# This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer

# Acknowledgements: None--original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random

def peel_digits(num):
    '''given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]'''
    str_num=str(num) # convert to string to utilize Python's strong string features
    digit_list=[] #create empty list
    for letter in str_num:
        digit_list.append(int(letter)) #Puts each digits into list
    # print(digit_list)
    return digit_list

def print_digits(digit_list): # takes a Python list as input
    '''given any Python list, this function prints each list element'''
    for digit in digit_list:
        print(digit)

def main():
    '''This main function is intended to display the capabilities of the peel_digits() and print_digit() functions'''
    year = random.randint(0, 2015)
    print("\nYear = "+ str(year))
    year_list=peel_digits(year) # put list returned from function into year_list
    print("\nDigits")
    print_digits(year_list)

main() # call main()