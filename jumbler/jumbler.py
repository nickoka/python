"""
jumbler.py: Solve a jumble (anagram) by checking against each word in a dictionary
Authors: Nick Oka   

CIS 210 Assignment 4, Fall 2016, University of Oregon

Usage: python3 jumbler.py jumbleword wordlist.txt
"""

import argparse

def jumbler(jumble, dict_file_name):
    """
    Count the anagrams of the given word there are in the given dictionary
    args:
        jumble: a string used as the given word to look for anagrams in the dictionary
        dict_file_name = a text file containing dictionary words, one per line
    prints:
        If there are matching anagrams in the text file:
            - the anagrams found of jumble, one word per line
            - (Number of matches) 'matches in' (The amount of dictionary words) 'words'
        If there are no matching anagrams of jumble:
            - 'No matches'
    """

    dict_list = []
    for line in dict_file_name:
        dict_list.append(line.strip())
    if len(dict_list) == 0:
        print("File is empty")
        return
    num_words = 0
    NLINES = 0
    jumble = str(jumble.strip())
    for c_word in dict_list:
        c_word = str(c_word.strip())
        if sorted(jumble) == sorted(c_word):
            print(c_word)
            num_words += 1
        NLINES = NLINES + 1
        if NLINES >= len(dict_list) and num_words == 0:
            print("No matches")
    if num_words > 1:
        print (num_words, 'matches in', NLINES, 'words')
    if num_words <= 1:
        print (num_words, 'match in', NLINES, 'words')

def main():
    """
    collect command arguments and invoke jumbler()
    inputs:
        none, fetches arguments using argparse
    effects:
        calls jumbler()
    """
    parser = argparse.ArgumentParser(description="Solve a jumble (anagram)")
    parser.add_argument("jumble", type=str, help="Jumbled word (anagram)")
    parser.add_argument('wordlist', type=argparse.FileType('r'),
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # gets arguments from command line
    jumble = args.jumble
    wordlist = args.wordlist
    jumbler(jumble, wordlist)

if __name__ == "__main__":
    main()     

    

    

