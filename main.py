#!/usr/bin/env python3
from time import sleep
import sys
import argparse
import random

# Set up argparse
parser = argparse.ArgumentParser(description="Python program of which the output looks similar to typing.")
parser.add_argument("string", type=str, nargs="*",
                    help="The string that will be typed. If this argument is not specified, the input will be read "
                         "from stdin.")
parser.add_argument("-n", "--interval", type=float, default=0.2,
                    help="The interval between typing characters.")
parser.add_argument("-o", "--offset", type=float,
                    help="The maximum random offset. The minimum is the same, but converted to a negative number.")
args = parser.parse_args()
# Error if the interval is negative
if args.interval < 0:
    raise ValueError("interval must be a non-negative number")
# Set offset and give errors
if args.offset is None:
    args.offset = args.interval / 2
elif args.offset > args.interval:
    raise ValueError("offset must be less than the interval")
elif args.offset < 0 - args.interval:
    raise ValueError("offset must be greater than the interval converted to a negative number")


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
    # Type from string argument
    for word in args.string:
        fake_type(word + " ")
    # Print to add newline at the end
    print()
else:
    # Type each line in stdin
    for line in sys.stdin:
        fake_type(line)
