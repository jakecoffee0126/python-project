# guess the number (computer guess the user number)

import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":

        # if low and high are equal, it will throw out an error
        # the reason we put this if condition here and not in the while loop,
        # because we want the user to say if computer choice correctly or not
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could high too, cuz low = high
        feedback = input(
            f'{guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print("Bingo, computer guessed your number, {guess}, correctly!!")


computer_guess(10)
