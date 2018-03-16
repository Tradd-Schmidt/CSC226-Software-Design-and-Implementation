######################################################################
# Author: Dr. Scott Heggen      TODO: Tradd Schmidt
# Username: heggens             TODO: schmidtt
#
# Assignment: A1
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1984 and 1995. Also returns your compatibility
# with other animals.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Task 1
# TODO Ask user for their birth year

year = input("What is your birth year?:")

# TODO Check the year, print the correct animal for that year
if year == '1984':
    print('Your Chinese Zodiac is the Rat!')
elif year == '1985':
    print("Your Chinese Zodiac is the Ox!")
elif year == '1986':
    print("Your Chinese Zodiac is the Tiger!")
elif year == '1987':
    print("Your Chinese Zodiac is the Rabbit!")
elif year == '1988':
    print("Your Chinese Zodiac is the Dragon!")
elif year == '1989':
    print("Your Chinese Zodiac is the Snake!")
elif year == '1990':
    print("Your Chinese Zodiac is the Horse!")
elif year == '1991':
    print("Your Chinese Zodiac is the Goat!")
elif year == '1992':
    print("Your Chinese Zodiac is the Monkey!")
elif year == '1993':
    print("Your Chinese Zodiac is the Rooster!")
elif year == '1994':
    print("Your Chinese Zodiac is the Dog!")
elif year == '1995':
    print("Your Chinese Zodiac is the Pig!")
elif year == '1996':
    print('Your Chinese Zodiac is the Rat!')
elif year == '1997':
    print("Your Chinese Zodiac is the Ox!")
elif year == '1998':
    print("Your Chinese Zodiac is the Tiger!")
else:
    print("Sorry, that was an invalid year. Try inputing a year from 1984 to 1998.")
# Task 2
# TODO Ask the user for their friend's birth year
print()
friends_year = input('What is your friends birth year?')

# TODO Check the year, print the correct animal for that year
if friends_year == '1984':
    print("Your friend's Chinese Zodiac is the Rat!")
elif friends_year == '1985':
    print("Your friend's Chinese Zodiac is the Ox!")
elif friends_year == '1986':
    print("Your friend's Chinese Zodiac is the Tiger!")
elif friends_year == '1987':
    print("Your friend's Chinese Zodiac is the Rabbit!")
elif friends_year == '1988':
    print("Your friend's Chinese Zodiac is the Dragon!")
elif friends_year == '1989':
    print("Your friend's Chinese Zodiac is the Snake!")
elif friends_year == '1990':
    print("Your friend's Chinese Zodiac is the Horse!")
elif friends_year == '1991':
    print("Your friend's Chinese Zodiac is the Goat!")
elif friends_year == '1992':
    print("Your friend's Chinese Zodiac is the Monkey!")
elif friends_year == '1993':
    print("Your friend's Chinese Zodiac is the Rooster!")
elif friends_year == '1994':
    print("Your friend's Chinese Zodiac is the Dog!")
elif friends_year == '1995':
    print("Your friend's Chinese Zodiac is the Pig!")
elif friends_year == '1996':
    print("Your friend's Chinese Zodiac is the Rat!")
elif friends_year == '1997':
    print("Your friend's Chinese Zodiac is the Ox!")
elif friends_year == '1998':
    print("Your friend's Chinese Zodiac is the Tiger!")
else:
    print("Sorry, that was an invalid year. Try inputing a year from 1984 to 1998.")

my_birth_year = 1998            # TODO change this to your birth year

# Task 3
# TODO Check for compatibility between two birth years
# NOTE: You can assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.
print()
print("I myself am a Tiger")
if year == '1990':
    print('I ran some tests and turns out tigers pair well with your zodiac sign. We are a great match. ;)')
elif year == '1994':
    print('I ran some tests and turns out tigers pair well with your zodiac sign. We are a great match. ;)')
elif year == '1995':
    print('I ran some tests and turns out tigers pair well with your zodiac sign. We are a great match. ;)')
elif year == '1992':
    print("Sorry, you aren't cool enough to be my friend.")
else:
    print("You are ok. You can hang around me.")

__name__ = 3

# TODO print if you are a strong match, no match, or in between


