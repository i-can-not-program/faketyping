#!/usr/bin/env python3
from time import sleep
import sys
import argparse

string = ""
wait_time = ""
parser = argparse.ArgumentParser()
parser.add_argument("string", help="The string that will be typed.", type=str)
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
chars = list(args.string)
sleep(args.interval)
for char in chars:
    print(char, end="", flush=True)
    sleep(args.interval)
print()
