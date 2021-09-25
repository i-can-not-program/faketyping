#!/usr/bin/env python3
from time import sleep
import sys
import argparse

parser = argparse.ArgumentParser()
# TODO: fix TypeError: 'required' is an invalid argument for positionals
parser.add_argument("string", type=str, required=False,
                    help="The string that will be typed.")
parser.add_argument("-n", "--interval", type=float, default=0.2,
                    help="The interval between typing characters")
args = parser.parse_args()


# while len(string) == 0:
#     string = input("Enter a string to be typed: ")
# while True:
#     try:
#         wait_time = float(input("How long should it wait between characters: "))
#     except ValueError:
#         print("ValueError occurred! Your input is not a float!")
#         continue
#     else:
#         break
def fake_type(string):
    chars = list(string)
    sleep(args.interval)
    for char in chars:
        print(char, end="", flush=True)
        sleep(args.interval)
    print()


# Support for being piped into
if len(args.string) == 0:
    for line in sys.stdin:
        fake_type(line.rstrip())
else:
    # Type from string argument
    fake_type(args.string)
