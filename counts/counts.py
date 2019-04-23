"""
counts.py: Count the number of occurrences of each major code in a file.

Authors: Nick Oka
Credits: Python List Objects. Referenced for the list.count method. https://docs.python.org/3/tutorial/datastructures.html

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.

Usage: python counts.py majors.txt
"""

import argparse


def count_codes(majors_file):
    """
    Count the amount of students in each major
    1. Must be in alphabetical order
    2. Prints the number of students with the specific major next to it

    args: majors_file: candidate list of majors
    returns: a list of majors in order alphabetically with the amount of students in each major
    """
    majors = []

    for line in majors_file:
        majors.append(line.strip())
        
    if len(majors) == 0:
        print("File is empty")
        return
    
    majors = sorted(majors)
    count = 0
    s_list = 0
    s_list = len(majors)
    i = 0
    majors.append("This is not a valid major code")
    for major in majors:
        count = majors.count(major) #From the Python List Objects in docs.python.org
        l_word = majors[i + 1]
        if i < (s_list - 1):
            i = i + 1
        if major != l_word:
             print(major, count)

def main():
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)


if __name__ == "__main__":
    main()
