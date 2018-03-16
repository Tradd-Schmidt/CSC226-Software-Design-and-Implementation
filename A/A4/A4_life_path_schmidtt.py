######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# Assignment: A4: A Bug's Life
# Purpose: This program is designed to take specific inputs from a user and
# produce their life number.
######################################################################

def get_day():
    """
    Asks for an input for what day they were born
    :return: an integer
    """
    day = int(input("What day were you born?(e.g. 6)"))
    return day


def get_month():
    """
    Asks for an input for what month they were born
    :return: an integer
    """
    month = int(input("What month were you born? (e.g. 11)"))
    return month


def get_year():
    """
    Asks for an input for what year they were born
    :return: an integer
    """
    year = int(input("What year were you born? (e.g. 1998)"))
    return year


def input_to_list(year, month, day):
    """
    Takes the three integers and puts them into a list
    :param year: the year they were born
    :param month: the month they were born
    :param day: the day they were born
    :return: a list
    """

    str_year = str(year)
    str_month = str(month)
    str_day = str(day)
    digit_list = []
    for num in str_year:
        digit_list.append(int(num))
    for letter in (str_month, str_day):
        digit_list.append(int(letter))
    return digit_list


def input_to_list_2(initial_sum):
    """
    This is to do subsequent sums until the number is below 10
    :param initial_sum: the integer after the previous sum
    :return: all the digits in a list
    """
    new_list = str(initial_sum)
    digit_list = []
    for letter in new_list:
        digit_list.append(int(letter))
    return digit_list


def calc_life_number(list):
    """
    This takes an integer and sums the digits until it is a single digit, 11, 22, or 33.
    :param list: a list of integers
    :return: An integer which has been reduced to it's lowest form
    """
    sum = 0
    for num in list:
        sum += num
    return sum


def print_life_description(integer):
    """
    Prints a description of the final life number
    :param integer: the final life sum
    :return: a string which is the description
    """
    if integer == 1:
        desc=("A person with Life Path number 1 is hard working, a natural born leader, has a pioneering spirit that is\n"
              "full of energy, and a passion for art. They have a strong desire to be number one, which means a person\n"
              "with this number can manifest very easily. Due to their determination and self motivation, they won't\n"
              "let anything stand in their way of accomplishing a goal. Their drive allows them to overcome any\n"
              "obstacle or challenge they may encounter, and they have the desire to accomplish great things in their\n"
              "lifetime. Their only need is to focus on what they want in order to achieve it.")
    elif integer == 2:
        desc=("A person with Life Path number 2 seeks harmony and peace, and is symbolized by relationships,\n"
              "co-operation, and being considerate and thoughtful of others. People with a Life Path 2 are natural\n"
              "peacemakers, and because they see all the viewpoints in any situation, handle difficult situations with\n"
              "grace, and tend to be persuasive rather than forceful when trying to get their point across, people may\n"
              "often look to them to be a mediator in any argument.")
    elif integer == 3:
        desc=("People with a Life Path number 3 have a very high level of creativity and self expression. This\n"
              "abundance of creative energy, and the ease with which they are able to communicate in all areas, both\n"
              "written word and verbal, could lead them to become a poet, actor, writer, artist or musician. In fact\n"
              "many writers, radio broadcasters, actors, singers, performers, and counselors share this life path\n "
              "number.")
    elif integer == 4:
        desc=("People with a Life Path number 4 are the worker bees of society. If your Life Path is a 4 you are\n"
              "determined, practical and hard working. Down-to-earth is a term that is probably often used to describe\n"
              "you. You find hard work rewarding and don't look for the easy way to the top or to finding success.\n"
              "Not only do you work hard yourself, but you expect the same from those around you. ")
    elif integer == 5:
        desc=("Those with a Life Path of 5 seek freedom above all else. They are adventurers, having a restless\n"
              "nature, and being on the go, constantly seeking change and variety in life. They have a free spirit\n"
              "and need to have variety in their day. If they do not live the adventure, their lives become way too\n"
              "dramatic.")
    elif integer == 6:
        desc=('Those born with a Life Path number 6 are incredible nurturers. If men, they rescue damsels in distress.\n'
              'If women, they mother the "little boy" in their men.')
    elif integer == 7:
        desc=("Seven is a cerebral number, and those with a Life Path number 7 have a loner quality. They need\n"
              "to learn to have faith. If they do not have faith they tend to become very cynical and escape through\n"
              "drugs, alcohol, work, and geography. They have a love of natural beauty: ocean, green grass, plants,\n"
              "flowers, etc. . .")
    elif integer == 8:
        desc=("People with a Life Path number 8 do not feel safe unless they have found a way to establish financial\n"
              "security.")
    elif integer == 9:
        desc=("Those born with a Life Path number 9 are natural leaders, and they assume they are in charge even if\n"
              "they are not. If in a department store, people think they work there. They take care of everyone else\n"
              "but need to learn to speak up when they need help, love, and hugs. Nines often feel unloved or\n"
              "abandoned by their mother or father, or they feel completely responsible for them. It's hard for them\n"
              "to let go of the past.")
    elif integer == 11:
        desc=("Individuals with the Life Path number 11 are very intuitive, in fact it is the most intuitive of all\n"
              "numbers. They are sensitive and have a great understanding of others, and can sense a great deal about\n"
              "what is going on behind the scenes. For example, they will pick up on people's relationships and health\n"
              "without being told anything. They are here to use their gifts of intuition, and sensitivity to help\n"
              "others.")
    elif integer == 22:
        desc=("22 is considered the most powerful of all the numbers. Those with a Life Path number 22 have great\n"
              "spiritual understanding, and ability to apply knowledge in a practical way and achieve enormous success.")
    else:
        desc=("A birth date that reduces down to 33 is very rare. When it does happen you may be looking at a great\n"
              "and significant spiritual leader along the lines of the Dalai Lama (Life Path 22) or Gandhi\n"
              "(Life Path 9). Remember that a 33 is also a 6 life path, a very nurturing and responsible number. 33 is\n"
              "the Master Teacher. This individual's focus is on reaching the world and uplifting the loving energy\n"
              "of mankind. They are not concerned with personal ambition, and have great devotion to cause. ")
    return desc


def main():
    day = get_day()
    month = get_month()
    year = get_year()

    life_sum = input_to_list(year, month, day)
    life_sum = calc_life_number(life_sum)
    while life_sum > 10:
        if life_sum % 11 != 0:
            digit_list = input_to_list_2(life_sum)
            life_sum = calc_life_number(digit_list)
        else:
            break
    print(print_life_description(life_sum))


main()
