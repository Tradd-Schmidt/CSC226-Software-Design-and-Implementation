######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# Assignment: P0: Final Project
#
# Purpose: Allow a user to input either binary or text into the function and return the ASCII form if it is text with the
# parity bit added on, or the binary with the parity bit added on if it is just binary.
#
######################################################################


class ASCIICode:
    """
    A class that is used to convert string into it's ASCII equivalent
    """
    def __init__(self, strng, binary=False):
        self.binary = binary
        self.text = strng

    def __str__(self):
        if not self.binary:
            return "{0}".format(self.text)
        else:
            return "{0}".format(self.binary)

    def is_binary(self):
        """
        Takes a string and tests to see if there are only 1s and 0s in the string
        :return: A boolean
        """
        for i in self.text:
            if i == "0" or i == "1":
                pass
            else:
                return False
        return True

    def is_div_by_sevens(self):
        """
        Checks to see if the length of a string is 7 characters long
        :return: A boolean
        """
        if len(self.text) % 7 != 0:
            return False
        else:
            return True

    def split_into_sevens(self):
        """
        Takes a string and splits the characters up and appends them to a list
        :return: a list
        """
        l = []
        for i in self.text:
            l.append(int(i))
        return l

    def extract_text(self, text):
        l = []
        for i in text:
                for b in i:
                    l.append(b)
        return l

    def add_parity(self, text):
        """
        Adds the parity bit to a string of binary
        :param text: the string that will have a parity bit added
        :return: the string with a parity bit
        """
        l = []
        for i in text:
            l.append(int(i))
        if sum(l) % 2 == 0:
            l_2 = [0]
            for i in l:
                l_2.append(i)
        elif sum(l) % 2 != 0:
            l_2 = [1]
            for i in l:
                l_2.append(i)
        return l_2

    def convert_to_ascii(self):
        """
        converts a string of letters to their ascii equivalents
        :return: a list pertaining all of the ascii characters
        """
        ascii_dict = {"NUL": "0000000", "SOH": "0000001", "STX": "0000010", "ETX": "0000011", "EOT": "0100", "ENQ": "0000101",
                      "ACK": "0000110", "BEL": "0000111", "BS": "0001000", "HT": "0001001", "LF": "0001010", "VT": "0001011",
                      "FF": "000111", "CR": "0001101", "SO": "0001110", "SI": "0001111", "DLE": "0010000", "DCL": "0010001",
                      "DC2": "0010010", "DC3": "0010011", "DC4": "0010100", "NAK": "0010101", "SYN": "0010110", "ETB": "0010111",
                      "CAN": "0011000", "EM": "00110001", "SUB": "0011010", "ESC": "0011011", "FS": "0011100", "GS": "0011101",
                      "RS": "0011110", "US": "0011111", " ": "0100000", "!": "0100001", '"': "0100010", "#": "0100011", "$": "0100100",
                      "%": "0100101", "&": "0100110", "'": "0100111", "(": "0101000", ")": "0101001", "*": "0101010", "+": "0101011",
                      ",": "0101100", "-": "0101101", ".": "0101110", "/": "0101111", "0": "0110000", "1": "0110001",
                      "2": "0110010", "3": "0110011", "4": "0110100", "5": "0110101", "6": "0110110", "7": "0110111",
                      "8": "0111000", "9": "0111001", ":": "0111010", ";": "0111011", "<": "0111100", "=": "0111101",
                      ">": "0111110", "?": "0111111", "@": "1000000", "A": "1000001", "B": "1000010", "C": "1000011",
                      "D": "1000100", "E": "1000101", "F": "1000110", "G": "1000111", "H": "1001000", "I": "1001001",
                      "J": "1001010", "K": "1001011", "L": "1001100", "M": "1001101", "N": "1001110", "O": "1001111",
                      "P": "1010000", "Q": "1010001", "R": "1010010", "S": "1010011", "T": "1010100", "U": "1010101",
                      "V": "1010110", "W": "1010111", "X": "1011000", "Y": "1011001", "Z": "1011010", "[": "1011011",
                      "\\": "1011100", "]": "1011101", "^": "1011110", "_": "1011111", "`": "1100000", "a": "1100001", "b": "1100010",
                      "c": "1100011", "d": "1100100", "e": "1100101", "f": "1100110", "g": "1100111", "h": "1101000",
                      "i": "1101001", "j": "1101010", "k": "1101011", "l": "1101100", "m": "1101101", "n": "1101110",
                      "o": "1101111", "p": "1110000", "q": "1110001", "r": "1110010", "s": "1110011", "t": "1110100",
                      "u": "1110101", "v": "1110110", "w": "1110111", "x": "1111000", "y": "1111001", "z": "1111010",
                      "{": "1111011", "|": "1111100", "}": "1111101", "~": "1111110", "DEL": "1111111"}
        ascii_list = []
        if self.binary == "True":
            if self.is_div_by_sevens():
                ascii_list = self.split_into_sevens()
                ascii_list = self.add_parity(ascii_list)
            elif not self.is_div_by_sevens():
                print("If you input a binary number, it needs to be seven characters long.")
        else:
            old_list = self.extract_text(self.text)
            for i in old_list:
                u = self.add_parity(ascii_dict[i])
                ascii_list.append(u)
        return ascii_list


def main():
    user_input = input("Please input what you would like converted to ASCII:")
    binary = input("This is binary? (True or False)")
    x = ASCIICode(user_input, binary)
    print(x.convert_to_ascii())


if __name__ == "__main__":
    main()
