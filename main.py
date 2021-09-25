#!/usr/bin/env python3
from time import sleep

string, wait_time = "", ""
while len(string) == 0:
    string = input("Enter a string to be typed: ")
while True:
    try:
        wait_time = float(input("How long should it wait between characters: "))
    except ValueError:
        print("ValueError occurred! Your input is not a float!")
        continue
    else:
        break
chars = list(string)
sleep(wait_time)
for char in chars:
    print(char, end="", flush=True)
    sleep(wait_time)
print()
