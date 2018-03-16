import sys

from a6_genes_solved import *           # You may get red squiggly lines from PyCharm; it'll be okay though.

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

    # The following tests test the is_nucleotide() function
    print("\nTesting is_nucleotide()")
    testit(is_nucleotide("CGTAGGCAT") == True)
    testit(is_nucleotide("CGTAFLCAT") == False)

    # Testing the num_times() function
    print("\nTesting num_times()")
    testit(num_times("CGTAGGCAT",'T') == 2)
    testit(num_times("CGTAGGCAT",'G') == 3)
    testit(num_times("CGTCGTTCT",'A') == 0)
    testit(num_times("GGCA",'T') == 0)

    # Testing the complement_strand() function
    print("\nTesting complement_strand()")
    testit(complement_strand("CC") == "GG")
    testit(complement_strand("CA") == "GT")
    testit(complement_strand("CGTAGGCAT") == "GCATCCGTA")
    testit(complement_strand("CGTAFLCAT") == "Sequencing Error")

    # Testing the mRNA() function
    print("\nTesting mRNA()")
    testit(mRNA("GCATCCGTA") == "GCAUCCGUA")
    testit(mRNA("CCATTGGGTT") == "CCAUUGGGUU")
    testit(mRNA("AAGCACCG") == "AAGCACCG")

    # Testing amino_acid_chunks()
    print("\nTesting amino_acid_chunks()")
    testit(amino_acid_chunks('AGA') == 'R')
    testit(amino_acid_chunks('AFA') == '?')

    # Testing chunk_amino_acid()
    print("\nTesting chunk_amino_acid()")
    testit(chunk_amino_acid("CGUCAC") == ["CGU","CAC"])
    testit(chunk_amino_acid("CGUAGGCAUUU") == ["CGU","AGG","CAU"])      # note that the "extra two U's are discarded

    # Testing sequence_gene()
    print("\nTesting sequence_gene()")
    testit(sequence_gene("T") == '')            # because input is not in a group of 3 nucleotides
    testit(sequence_gene("JAN") == '')          # because input is not a valid string of nucleotides
    testit(sequence_gene("CACGT") == 'V')       # because mRNA sequence is "GUGCA"
                                                # and ignoring the last two "extra" nucleotides,
                                                # this returns amino acid "V".
    testit(sequence_gene("CGTAGGCAT") == "ASV") # because mRNA sequence is "GCAUCCGUA"
                                                # taking the complement and then replacing the T nucleotide with U.
                                                # Grouping into triples, we  get the "ASV" amino acid sequence.

genomics_test_suite()

# Notice the lack of a main? This is because this is a test suite; it's not intended to be run as a main() program.
# However, to run the test suite, you run this file. It should just work.