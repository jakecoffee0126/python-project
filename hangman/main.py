# hangman

import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # keep searching the word, if word is '-' and ' '
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting user input
    while len(word_letters) > 0:  # geater than 0 means the user haven't guess all the letter yet

        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        # if this is the valid character in the alphabet that i haven't used yet
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in user_letter:
            print('You have alrady used that character, please try again')

        else:
            print("please type in valid character")


if __name__ == '__main__':
    hangman()
