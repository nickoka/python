"""
draw_barcode.py: Draw barcode representing a ZIP code using Turtle graphics

Authors: Nick Oka

CIS 210 assignment 3, part 2, Fall 2016.

Usage: python draw_barcode.py zip_code
"""
import argparse	# Used in main program to obtain 5-digit ZIP code from command
                # line
import time	# Used in main program to pause program before exit
import turtle	# Used in your function to print the bar code

## Constants used by this program
SLEEP_TIME = 30	# number of seconds to sleep after drawing the barcode
ENCODINGS = [[1, 1, 0, 0, 0],	# encoding for '0'
             [0, 0, 0, 1, 1],	# encoding for '1'
             [0, 0, 1, 0, 1],   # encoding for '2'
             [0, 0, 1, 1, 0],	# encoding for '3'
             [0, 1, 0, 0, 1],	# encoding for '4'
             [0, 1, 0, 1, 0],	# encoding for '5'
             [0, 1, 1, 0, 0],	# encoding for '6'
             [1, 0, 0, 0, 1],	# encoding for '7'
             [1, 0, 0, 1, 0],	# encoding for '8'
             [1, 0, 1, 0, 0]	# encoding for '9'
            ]
SINGLE_LENGTH = 25	# length of a short bar, long bar is twice as long

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    sum = 0
    for i in range(len(digits)):
        sum = sum + digits[i]
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit

def draw_bar(my_turtle, digit):
    """
    Draws either a half or a full sized bar based on the value of digit
    args:
        digit: a value that indicates if a half or a full sized bar should be drawn
    returns:
        nothing, draws either a half or a full sized bar in the Turtle graphics window
    """
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()

def draw_zip(my_turtle, zip):
    """
    Indicates what bar to draw for use in ZIP barcodes.
    Requirements for the ZIP barcode:
       - Start and end with a full-height bar known as a frame bar
       - Between the frame bars, a representation of the digits that make up the zip code
       - Following the represention of the zip code, the representation of a check digit
    args:
        my_turtle: Turtle object to draw with
        zip: the ZIP code used for drawing the ZIP barcode
    returns: nothing, indicates what is required to draw for the zip code
    """
    list = [0,0,0,0,0]
    zip = str(zip)
    s_zip = len(zip)
    if s_zip < 5:
        first_num = (5 - s_zip)
        for i in range (first_num):
            zip = "0" + zip
    for i in range (5):
        list[i] = int(zip[i])
    check_digit = compute_check_digit(list)
    draw_bar(my_turtle, 1)
    for word_num in str(zip):
        num = int(word_num)
        for bars in ENCODINGS[num]:
            draw_bar(my_turtle, bars)
    num = int(check_digit)
    for bars in ENCODINGS[num]:
        draw_bar(my_turtle, bars)
    draw_bar(my_turtle, 1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ZIP", type=int)
    args = parser.parse_args()
    zip = args.ZIP
    if zip <= 0 or zip > 99999:
        print("zip must be > 0 and < 100000; you provided", zip)
    else:
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.goto(-150,0)
        my_turtle.pendown()
        draw_zip(my_turtle, zip)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
