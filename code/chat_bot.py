"""
This file contains source code of the application "Chat Bot".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary libraries

import sys
import os
import random


# Static variable

LETTERS: str = "abcdefghijklmnopqrstuvwxyz"


# Creating necessary functions


def generate_random_name():
    # type: () -> str
    res: str = ""  # initial value
    length: int = random.randint(4, 20)
    for i in range(length):
        res += LETTERS[random.randint(0, len(LETTERS) - 1)]

    return res


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function to run the application


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("BOT: Hello, what is your name?")
    name: str = input("Anonymous user: ")  # Asking the user to enter his/her name
    print("BOT: Nice to meet you, " + str(name).capitalize() + "!")
    while True:
        message: str = input(str(name).capitalize() + ": ")  # asking the user to enter a message
        # Detecting what the BOT will say based on your message
        if message[0:2].upper() == "IS" or message[0:3].upper() == "ARE":
            possible_answers: list = ["Yes", "No", "It depends", "I don't know"]
            print("BOT: " + str(possible_answers[random.randint(0, len(possible_answers) - 1)]))
        elif message[0:4].upper() == "WHEN":
            possible_answers: list = ["days ago", "months ago", "years ago", "yesterday", "today", "recently",
                                      "tomorrow", "never"]
            length: int = random.randint(2, 9999)
            p: float = random.random()
            if p <= 0.5:
                print("BOT: " + str(length) + " " + str(possible_answers[random.randint(0, 2)]))
            else:
                print("BOT: " + str(possible_answers[random.randint(3, len(possible_answers) - 1)]))
        elif message[0:3].upper() == "WHO":
            print("BOT: " + str(generate_random_name()).capitalize())
        elif message[0:5].upper() == "WHERE":
            print("BOT: " + str(generate_random_name()).capitalize())
        else:
            print("BOT: Sorry, I don't know what to say.")


if __name__ == '__main__':
    main()
