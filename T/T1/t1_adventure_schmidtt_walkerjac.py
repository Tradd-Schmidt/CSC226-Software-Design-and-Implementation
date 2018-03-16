######################################################################
# Author: Dr. Scott Heggen      TODO: Tradd Schmidt and Jacob Walker
# Username: heggens             TODO: schmidtt and walkerjac
#
# Assignment: T1: Choose Your Own Adventure
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem

######################################################################
import time

delay = 3.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False

# TODO Ask the user to input their name. Make it adventurous, such as:
# TODO "What do they call you, worthy adventurer? "

username = input('Tell me, what do they call you stranger?')
#################################################################
# The following is the first part of the story. Don't change this.
#print()
#print("Welcome,", username, ", to the labyrinth")
#time.sleep(delay)
#print("Before you lies two paths.")
#print("One path leads to treasures of unimaginable worth.")
#print("The other, certain death. Choose wisely.")
#print()
#time.sleep(delay * 2)
#print("You are in a dark cave. You can see nothing.")
#print("Staying here is certainly not wise. You must find your way out.")
#print()
#time.sleep(delay)
#direction = input("Which direction would you like to go? [North/South/East/West]")

########################################################

# An example chapter, to start your user off on your adventure
# Author: Scott Heggen
#if direction == "North":
 #  print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
  # time.sleep(delay)
#elif direction == "South":
 #  print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
  # time.sleep(delay)
   #print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
   #print("Running seems like a good idea now. But... it's really, really dark.")
   #print()

  # speed = int(input("How many steps would you like to take?"))
   #if speed < 5:
     #  print("It appears you are more scared of the dark than a bear.")
      # time.sleep(delay*2)
      # print("Your fears were well-placed. The bear was hibernating, and your quiet exit pays off.")
  # else:
      # print("You run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
      # time.sleep(delay)
      # print("He eats you. You are delicious.")
      # dead = True
#else:
  # print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
  # time.sleep(delay)


# It is unusual to quit a program early like I do below. However, it serves us very well for this assignment,
# because it ends our story upon death. So we will use it. The alternative is a LOT of nested if/else statements,
# which would get messy by the last group. You will need this statement after your chapter is added.
#if dead == True:
 #   quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may not be coming right after the example above.
# TODO don't forget the two lines of code above!

# Author: Scott Heggen          TODO Change this!
print("Despite the grand wizard's warnings, you enter the forbidden forest.")
print()
time.sleep(delay)
print("After wandering for a bit you come upon a giant tree.")
time.sleep(delay)
print("The giant tree springs to life and you notice that this tree has a face!")
time.sleep(delay)
print('"Welcome wanderer. This entire forest is my domain."')
time.sleep(delay)
print('"If you wish to escape, follow the left path. If you wish to die, follow the right path."')
path = input('Which path do you choose?')
print()
if path == "left":
    print("You decide you need to check your inventory before you go down this path.")
    bombs = int(input("How many bombs do you have?"))
    if bombs < 3:
        print("You decide to trust the giant tree.")
        time.sleep(delay)
        print("You head down the left path not knowing what to expect.")
        time.sleep(delay)
        print("Suddenly, all the trees that are around you surround you with their branches!")
        time.sleep(delay)
        print("You start throwing bombs, but it is not enough.")
        time.sleep(delay)
        print("The branches start compressing you.")
        time.sleep(delay)
        print("Their pressure becomes too great, and you are crushed to death.")
    elif bombs >= 3:
        print("You decide to trust the giant tree.")
        time.sleep(delay)
        print("You head down the left path not knowing what to expect.")
        time.sleep(delay)
        print("Suddenly, all the trees that are around you surround you with their branches!")
        time.sleep(delay)
        print("You hurl a bunch of bombs at the trees.")
        time.sleep(delay)
        print("You throw just enough bombs to be able to escape.")
        time.sleep(delay)
        print("You sprint backwards on the path.")
        time.sleep(delay)
        print("This time you head down the right path.")
        time.sleep(delay)
        path = "right_two"
    dead = True
if path == "Left":
    print("You decide to trust the giant tree.")
    time.sleep(delay)
    print("You head down the left path not knowing what to expect.")
    time.sleep(delay)
    print("Suddenly, all the trees that are around you surround you with their branches!")
    time.sleep(delay)
    print("Their pressure becomes too great, and you are crushed to death.")
    dead = True
elif path == "right":
    print("You disregard the tree's warning.")
    time.sleep(delay)
    print("You head down the right path at a brisk pace.")
    time.sleep(delay)
    print("You find a break in the trees and you exit to a small village.")
elif path == "Right":
    print("You disregard the tree's warning.")
    time.sleep(delay)
    print("You head down the right path at a brisk pace.")
    time.sleep(delay)
    print("You find a break in the trees and you exit to a small village.")
elif path == "right_two":
    print("You head down the right path at a brisk pace.")
    time.sleep(delay)
    print("You find a break in the trees and you exit to a small village.")
else:
    print("You get really confused and spend hours trying to contemplate what to do.")
    time.sleep(delay)
    print("You end up passing out. (Try going left or right)")
if dead == True:
    quit()

#########################################################################################################
# TODO Once you've tested your code and it works, copy your code between the blocks of ###'s,
# TODO plus the death code above, into your Google Doc.
# TODO The instructor will be combining it all into the master program.
