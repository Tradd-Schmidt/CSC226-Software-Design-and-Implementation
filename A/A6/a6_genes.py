######################################################################
# Author: Tradd Schmidt     TODO: Change this to your names
# Username: schmidtt             TODO: Change this to your usernames
#
# Assignment: A6: It's in your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys


def testit(did_pass):
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


def genomics_test_suite():
    """
    The genomics_test_suite() is designed to test the following:
      is_nucleotide(sequence)
      num_times(sequence, nucleotide()
      complement_strand()
      amino_acid_chunks()
      sequence_gene()

    :return: None
    """

    # TODO   I highly suggest starting by building more test cases for each function.
    # TODO   If you can build accurate test cases, you can be confident that you understand
    # TODO   the intended functionality of each function.

    # The following tests test the is_nucleotide() function
    print("Testing is_nucleotide()")
    testit(is_nucleotide("CGTAGGCAT") == True)
    testit(is_nucleotide("CGTAFLCAT") == False)
    # FIXME: Add your own tests here

    # Testing the num_times() function
    print("Testing num_times()")
    testit(num_times("CGTAGGCAT",'T') == 2)
    testit(num_times("CGTAGGCAT",'G') == 3)
    testit(num_times("CGTCGTTCT",'A') == 0)
    testit(num_times("GGCA",'T') == 0)
    # FIXME: Add your own tests here

    # Testing the complement_strand() function
    print("Testing complement_strand()")
    testit(complement_strand("CC") == "GG")
    testit(complement_strand("CA") == "GT")
    testit(complement_strand("CGTAGGCAT") == "GCATCCGTA")
    testit(complement_strand("CGTAFLCAT") == "Sequencing Error")
    # FIXME: Add your own tests here

    # Testing the mRNA() function
    print("Testing mRNA()")
    testit(mRNA("GCATCCGTA") == "GCAUCCGUA")
    testit(mRNA("CCATTGGGTT") == "CCAUUGGGUU")
    testit(mRNA("AAGCACCG") == "AAGCACCG")
    # FIXME: Add your own tests here

    # Testing amino_acid_chunks()
    print("Testing amino_acid_chunks()")
    testit(amino_acid_chunks('AGA') == 'R')
    testit(amino_acid_chunks('AFA') == '?')
    # FIXME: (Optional) Add your own tests here. You'll need to dig into and
    # FIXME: understand the dictionary in this function to write more of these tests

    # Testing chunk_amino_acid()
    print("Testing chunk_amino_acid()")
    testit(chunk_amino_acid("CGUCAC") == ["CGU","CAC"])
    testit(chunk_amino_acid("CGUAGGCAUUU") == ["CGU","AGG","CAU"])      # note that the "extra two U's are discarded
    # FIXME: Add your own tests here

    # Testing sequence_gene()
    print("Testing sequence_gene()")
    testit(sequence_gene("T") == '')            # because input is not in a group of 3 nucleotides
    testit(sequence_gene("JAN") == '')          # because input is not a valid string of nucleotides
    testit(sequence_gene("CACGT") == 'V')       # because mRNA sequence is "GUGCA"
                                                # and ignoring the last two "extra" nucleotides,
                                                # this returns amino acid "V".
    testit(sequence_gene("CGTAGGCAT") == "ASV") # because mRNA sequence is "GCAUCCGUA"
                                                # taking the complement and then replacing the T nucleotide with U.
                                                # Grouping into triples, we  get the "ASV" amino acid sequence.
    # FIXME: (Optional) Add your own tests here. You'll need to dig into and
    # FIXME: understand the dictionary in amino_acid_chunks() to write more of these tests


def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence: A string
    :return:a boolean
    """
    check = "ACGT"
    for letter in sequence:
        if letter not in check:
            return False
        else:
            pass
    return True
    # FIXME: Finish the docstring above

    # FIXME: Add your code here to complete this function

    # FIXME: Clearly this should not always return True


def num_times(sequence, nucleotide):
    """
    Returns count of how many times nucleotide is found in sequence.

    :param sequence:
    :param nucleotide:
    :return:
    """
    # FIXME: Finish the docstring above

    count = 0

    #FIXME: Add your code here to complete this function

    # FIXME: Obviously, this should not always return 0
    return count


def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence: A string value
    :return: the complement of the sequence
    """
    # FIXME: Finish the docstring above

    complement = ""         # This can be used to "build" the complement

    for letter in sequence:
        if letter == "T":
            complement += "A"
        elif letter == "A":
            complement += "T"
        elif letter == "C":
            complement += "G"
        elif letter == "G":
            complement += "C"
        else:
            return "Sequencing Error"

    # FIXME: Add your code here to complete this function

    # FIXME: Obviously, this should not always return ""
    return complement


def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence: The complemented sequence
    :return: the sequence with all T's replaced with U's
    """
    # FIXME: Finish the docstring above

    # FIXME: Add your code here to complete this function

    mrna = ""
    for letter in sequence:
        if letter == "T":
            mrna += "U"
        else:
            mrna += letter
    # FIXME: Obviously, this should not always return ""
    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence: an rna sequence
    :return: the sequence in chunks of 3
    """
    # FIXME: Finish the docstring above

    # FIXME: Add your code here to complete this function
    count = 0
    num = len(sequence)
    list_of_chunks = []
    for letter in sequence:
        count += 1
        if num < 3:
            break


    # FIXME: Obviously, this should not always return an empty string
    return list_of_chunks


def amino_acid_chunks(threecharseq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character AminoAcid

    :param threecharseq: a sequence of three characters
    :return: A string representing the animo acid chunk for that sequence
    """

    ###################################################################
    #  This function is already completed correctly! No changes needed!
    ###################################################################

    # We haven't learned about dictionaries yet, but here is one for the extra curious.
    # You aren't expected to know what this is yet.
    translator = {"GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                        "AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                        "GAC":"D", "GAU":"D",
                        "AAC":"N", "AAU":"N",
                        "UGC":"C", "UGU":"C",
                        "GAA":"E", "GAG":"E",
                        "CAA":"Q", "CAG":"Q",
                        "GGA":"G", "GGC":"G", "GGU":"G", "GGG":"G",
                        "CAC":"H", "CAU":"H",
                        "AUA":"I", "AUC":"I", "AUU":"I",
                        "UUA":"L", "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                        "AAA":"K", "AAG":"K",
                        "AUG":"M",
                        "UUC":"F", "UUU":"F",
                        "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                        "AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                        "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                        "UGG":"W",
                        "UAC":"Y", "UAU":"Y",
                        "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                        "UAA":"*", "UAG":"*", "UGA":"*" }

    if threecharseq in translator.keys():
        return translator[threecharseq]     # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a a sequence of nucleotides:
    A, C, G, and T and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    ###################################################################
    #  This function is already completed correctly! No changes needed!
    ###################################################################

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = (chunk_amino_acid(mrna))            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + amino_acid_chunks(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function calls either the genomics_test_suite() or a direct function,
    which will test each of the supportive functions

    :return: None
    """
    # print(sequence_gene("CACGT"))         # Uncomment this line to use the function directly
    genomics_test_suite()                   # Uncomment this line to run the test suite to test all your functions

main() # call to main() function
