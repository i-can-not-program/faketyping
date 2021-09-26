#!/usr/bin/env python3
from time import sleep
import sys
import argparse

# Set up argparse
parser = argparse.ArgumentParser(description="Python program of which the output looks similar to typing.")
parser.add_argument("string", type=str, nargs="*",
                    help="The string that will be typed. If this argument is not specified, the input will be read "
                         "from stdin.")
parser.add_argument("-n", "--interval", type=float, default=0.2,
                    help="The interval between typing characters")
args = parser.parse_args()


# Create fake_type function
def fake_type(string):
    chars = list(string)
    for char in chars:
        sleep(args.interval)
        print(char, end="", flush=True)


# If the string argument is not specified, read from stdin
if not args.string:
    # Type each line in stdin
    for line in sys.stdin:
        fake_type(line)
else:
    # Type from string argument
    for word in args.string:
        fake_type(word + " ")
    # Print to add newline at the end
    print()

