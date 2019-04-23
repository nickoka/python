"""
drawflower.py:  Draw flower from multiple squares using Turtle graphics
Authors: Nick Oka

CIS 210 Assignment 1, Fall 2016, University of Oregon

Usage: python drawflower.py num_of_squares length_of_sides
"""
import argparse      # Used in main program to get num_squares and side_length
                     # from command line
import time          # Used in main program to pause program before exit
import turtle        # using turtle graphics

## Constants used by this program

#draw_square function from drawSquare function on page 34 of Miller and Ranum
def draw_square(my_turtle, side_length):
    for i in range(4):
        my_turtle.forward(side_length)
        my_turtle.right(90)

def draw_flower(my_turtle, num_squares, side_length):
    """
    Draw flower shape using squares
    args:
        my_turtle:  Turtle object to draw with
        num_squares: number of squares to use for flower
        side_length: length of a side for each square
    returns:
        nothing, draws flower in the Turtle graphics window
    """
    #FIXME: Your code replaces the next line
    #print("code to draw flower should be here instead")
    for i in range(num_squares):
        draw_square(my_turtle, side_length)
        my_turtle.right(20)

def main():
    """
    Interaction if run from the command line.
    Magic for now; we'll look at what's going on here
    in the next week or two.
    """
    parser = argparse.ArgumentParser(description="Draw flower using squares")
    parser.add_argument("num_squares", type=int,
                        help="number of squares to use (an integer)")
    parser.add_argument("side_length", type=int,
                        help="length of side for each square (an integer)")
    args = parser.parse_args()  # gets arguments from command line
    num_squares = args.num_squares
    side_length = args.side_length
    #num_squares = 25
    #side_length = 100
    my_turtle = turtle.Turtle()
    draw_flower(my_turtle, num_squares, side_length)
    time.sleep(10)              # delay for 10 seconds

if __name__ == "__main__":
    main()


