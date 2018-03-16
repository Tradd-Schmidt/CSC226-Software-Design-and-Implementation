#####################################################################################
# Author: Dr. Jan Pearce
# This program is designed to demonstrate the use of Boolean functions
# and the modulus (%) operator which gives the remainder following a division

# Acknowledgements: None--original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random

def is_even(num):
    '''Boolean function takes an integer as input. Returns True if even and False if odd'''
    if int(num) % 2 == 0:
        return True
    else:
        return False


def main():
    '''This main function is intended to display the capability of the is_even function'''
    year = random.randint(0, 2015)
    print("\nA random year is "+ str(year) +".")
    if is_even(year):
        print(str(year)+ " is even.")
    else:
         print(str(year)+ " is odd.")

main()