"""---Hangman Rules---
Once every game a random word will be chosen from the list in words.py
The player will have a total of 6 lives, if the player chooses 6 incorrect
    letters he/she/they will lose.
Only one letter can be guessed at a time
The letter that has been previously guessed incorrectly will be shown to the
    player so as not to be chosen again by mistake.
Before every guess the player will be shown a hangman to help keep the player
    on track with how many lives are left.
If all the letters were correctly guessed by the player before his/hers/their
    lives run out the player will win the game, which
    will be shown on screen.
If all lives has been lost, the hangman drawing will be completed and the
    player has lost. A message will display on screen
    telling the player of his/her/their loss."""
import random
import time
from listofwords import list_of_words


# variable for correctly guessed letters (global)
correct_guess_letter = []

# variable for incorrectly guessed letters (global)
incorrect_guess_letter = []

# variable for randomly chosen word (global)
random_chosen_words = ""

# variable for remaining lives left (global)
lives = 6

# variable for game over (global)
is_game_over = False


def random_word():
    """will return randomly chosen word for the hangman game"""
    global random_chosen_words

    random.seed(time.time())
    random_chosen_words = random.choice(list_of_words)
    random_chosen_words = random_chosen_words.upper()


def word_before_guess():
    """will print out dashes where the yet to be guessed letters of the word"""
    global correct_guess_letter
    global random_chosen_words

    for i in range(0, len(random_chosen_words)):
        letter = random_chosen_words[i]
        # print the correctly guessed letter
        if letter in correct_guess_letter:
            print(letter, end=" ")
        # print an a dash for the yet to be guessed letters
        else:
            print("_", end=" ")
    print("")