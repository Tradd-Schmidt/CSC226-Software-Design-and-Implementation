######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: A4: A Bug and a Crash
# Purpose: demonstration of using integer division and modulus operations,
# it calculates the largest number of quarters, dimes, nickels and pennies
# needed to make that change in coins.
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Mario Nakazawa and Dr. Jan Pearce
#
# original code structure: http://stackoverflow.com/questions/621062/python-function-find-change-from-purchase-amount
# modifications:
#   (1) function returns a string, omitting denominations with zero number
#   (2) function uses modulus operator to find the remaining change
#   (3) added lots of comments to explain how the function works
#   (4) converted to Python 3
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################


def make_change(amount):
    """
    Calculate the number of quarters, dimes, nickels and pennies needed to make change.

    :param amount: amount in cents as an int
    :return: A string sentence describing how many of each coin is needed
    """
    outputStr = ""
    for coin in [25, 10, 5, 1]:
        # integer division to find the number of each kind of coin
        num = amount//coin
        # modulus (remainder) operator to find out how much remains
        amount = amount % coin

        # add the number of each denomination if necessary to output string
        if( num > 0 ):
            outputStr += str(num) + " of the " + str(coin) + " cent coins.\n"

    return outputStr

def main():
    """
    A program to calculate how many coins are needed to make change, given a number of cents

    :return: None
    """

    print("Welcome to the coin calculating machine!")
    total = int(input("Input total amount, in cents: "))

    # notice that we use the str() function to convert the total before
    # concatenating it to a string
    print( "\nFor "+str(total)+", the denominations are:\n"+ make_change ( total ) )

main()  # call main
