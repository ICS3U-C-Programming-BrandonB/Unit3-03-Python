#!/usr/bin/env python3

# Created By: Brandon
# Date: October 20th, 2025
# This program asks the user for their number from 0-9 then determines if they guessed correctly or not
# then prints either a right or wrong message

import random


def main():

    # get the number from the user
    user_guess = int(input("Enter A Number Between 0-9: "))

    correct_number = random.randint(0, 9)

    # determine whether or not the user guessed correctly
    if user_guess == correct_number:
        print("You guessed the correct number!")
    else:
        print(
            "You have guessed the wrong number. The correct number was {}".format(
                correct_number
            )
        )


# outputs the function
if __name__ == "__main__":
    main()
