"""
alphacode.py:  Convert PIN code to mnemonic alphabetic code

Authors: Nick Oka
Credits: 

CIS 210 assignment 1, Fall 2016.

Usage: python alphacode.py PIN_code
"""
import argparse      # Used in main program to get PIN code from command line
from test_harness import testEQ  # Used in CIS 210 for test cases

## Constants used by this program
CONSONANTS = "bcdfghjklmnpqrstvwyz"
VOWELS = "aeiou"


def alphacode(pin):
    """
    Convert numeric pin code to an
    easily pronounced mnemonic.
    args:
        pin:  code as positive integer
    returns:
        mnemonic as string
    """
    mnemonic = ""
    while pin > 0:
        if pin % 100 != 0:
            first_group = pin % 100
            pin = pin // 100
            vow1 = first_group % 5
            con1 = first_group // 5
            word1 = str(CONSONANTS[int(con1)])
            word2 = str(VOWELS[int(vow1)])
            mnemonic = word1 + word2 + mnemonic
    return mnemonic

def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    print("**** TESTING --- examples from course assignment page")
    testEQ("4327 => lohi", alphacode(4327), "lohi")
    testEQ("1298 => dizo", alphacode(1298), "dizo")
    print("***** Longer PIN codes ****")
    testEQ("1234567 => begomari?", alphacode(1234567), "begomari")
    testEQ("42424242 => lililili ?", alphacode(42424242), "lililili")
    testEQ("98765 => cuwira?", alphacode(98765), "cuwira")
    testEQ("987654 => zotenu?", alphacode(987654), "zotenu")
    testEQ("(same digit pairs, reverse order) 547698 => nutezo ?", alphacode(547698), "nutezo")
    print("**** Edge cases (robustness testing) ****")
    testEQ("0 => empty mnemonic ?", alphacode(0), "")
    testEQ("-42 and all negative numbers => empty mnemonic? ", alphacode(-42), "")
    print("*** End of provided test cases.  Add some of your own? ****")

def main():
    """
    Interaction if run from the command line.
    Magic for now; we'll look at what's going on here
    in the next week or two.
    """
    parser = argparse.ArgumentParser(description="Create mnemonic for PIN code")
    parser.add_argument("PIN", type=int,
                        help="personal identifier number (an integer)")
    args = parser.parse_args()  # gets arguments from command line
    pin = args.PIN
    mnemonic = alphacode(pin)
    print("Memorable PIN:", mnemonic)

if __name__ == "__main__":
    main()


