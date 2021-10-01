#!/usr/bin/env python3
from time import sleep
import sys
import argparse
import random

# Set up argparse
parser = argparse.ArgumentParser(description="Python program of which the output looks similar to typing.")
parser.add_argument("string", type=str, nargs="*",
                    help="The string that will be typed. If this isn't specified, input will be read from stdin.")
parser.add_argument("-n", "--interval", type=float, default=0.2,
                    help="The interval between typing characters.")
parser.add_argument("-o", "--offset", type=float,
                    help="The maximum random offset. The minimum is this, but converted to a negative number.")
args = parser.parse_args()
# Error if the interval is negative
if args.interval < 0:
    parser.error("interval must be a non-negative number")
# Set offset and give errors
if args.offset is None:
    args.offset = args.interval / 2
elif args.offset > args.interval:
    parser.error("offset must be less than or equals to the interval")
elif args.offset < 0 - args.interval:
    parser.error("offset must be greater than or equals to the interval converted to a negative number")


# Create fake_type function
def fake_type(string):
    # Create a list of all the characters in the string argument
    chars = list(string)
    # For each character in the list, sleep and print it
    for char in chars:
        sleep(args.interval + random.uniform(0 - args.offset, args.offset))
        print(char, end="", flush=True)


# Test if the string argument is specified
if args.string:
    # Type from string argument, then print a newline (print() does it with no args)
    for word in args.string:
        fake_type(word + " ")
    print()
else:
    # Type each line in stdin
    for line in sys.stdin:
        fake_type(line)
