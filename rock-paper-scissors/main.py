# rock, paper and scissors

import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(user)
    print(computer)

    if user == computer:
        return 'tie'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You win'

    return 'You lost'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
