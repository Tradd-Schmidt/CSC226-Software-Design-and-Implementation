######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# Assignment: A9 XHTML
#
# Purpose: To fix tag closing errors in html code
#
######################################################################
import sys


def ask_for_file():
    """
    Asks for the name of the file to be fixed
    :return: the file
    """
    filename = input("Enter the filename: ")
    try:
          file = open(filename, "r")
          return file, filename
    except:
          print("Invalid file name.")
          sys.exit()


def ask_for_new_name(in_file):
    """
    Asks the user what they want to name the output file
    :return: the name of the output file
    """
    name = input("What would you like the name of the output file to be?: ")
    if name == str(in_file):
        print("The new file name cannot be the same as old file name.")
        sys.exit()
    else:
        return name


def close_tag(line):
    """
    Reads a line and adds a closing tag if needed.
    :param file: file to be used
    :return: edited line
    """
    s = ""
    if "me" in line or "br" in line or "im" in line or "hr" in line:                  # Checks to see if the meta tag is used
        s += (line[:-2] + " />\n")
        error_count = 1
    else:
        s += line
        error_count = 0
    return s, error_count               # s is the line either with changes or without changes


def fix_tags(file):
    """
    Closes all open tags in html code
    :param file: The file that will be fixed
    :return: a string containing the entire updated file
    """
    s = ""
    error_count = 0
    a_line = file.readline()
    while a_line:                       # Parses each line and checks to see if a tag needs changing
        m, errors = close_tag(a_line)
        s += m
        error_count += errors
        a_line = file.readline()
    print(s)
    return s, error_count               # Returns a string containing all of the lines after they are fixed


def write_fixed_file(name, strng):
    """
    Writes a new file with the updated string
    :param name: Name of the new file
    :param strng: String to be written to the new file
    :return: None
    """
    out_file = open(name, "w")
    out_file.write(strng)


def main():
    in_file, file_name = ask_for_file()
    out_file = ask_for_new_name(file_name)
    fixed_html, errors = fix_tags(in_file)
    print("There were " + str(errors) + " errors in your code.")
    write_fixed_file(out_file, fixed_html)


main()
