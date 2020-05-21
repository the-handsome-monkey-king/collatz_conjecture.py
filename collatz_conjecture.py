#!/usr/bin/env python
"""collatz_conjecture.py

A Python implementation of the Collatz Conjecture

Star with a number n>1. Find the number of steps it takes to reach
one using the following process: 
    - if n is even, divide it by 2
    - if n is odd, multiply it by 3 and add 1
"""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

def process(n):
    iterations = 0
    while(n != 1):
        if(n % 2 == 0):
            n /= 2
            iterations += 1
        else:
            n = (n * 3) + 1
            iterations += 1
    print("Steps to one: {}".format(iterations))


def main():
    try:
        n = int(raw_input("Enter an integer greater than one: "))
        if(n > 1):
            process(n)
        else:
            raise ValueError
    except ValueError:
        print("Not a valid input.")

if __name__ == "__main__":
    main()
