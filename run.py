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


def create_hangman():
    """will create a hangman in relation to how many lives are left"""
    global lives

    if lives == 6:
        print("+-------------+")
        print("I             I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 5:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 4:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I             I")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 3:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I             I--")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 2:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I           --I--")
        print("I")
        print("I")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 1:
        print("+-------------+")
        print("I             I")
        print("I             O")
        print("I           --I--")
        print("I             I")
        print("I            /")
        print("I")
        print("I")
        print("+-------+")
    elif lives == 0:
        print("#-------------")
        print("I             I")
        print("I             O")
        print("I           --I--")
        print("I             I")
        print("I            / \\")
        print("I")
        print("I")
        print("#-------#")


def one_valid_letter():
    """ This function makes sure that only one letter can be chosen at a time,
    and it will need to be a letter from a-z """
    is_letter_valid = False
    letter = ""
    while is_letter_valid is False:
        letter = input("Enter guess letter:\n")
        letter = letter.strip().upper()
        # the letter can not be less than 1 or more than one (an input of 0 is
        # invalid, so is an input of 2 and above!)
        if len(letter) <= 0 or len(letter) > 1:
            print("Invalid, letter has to be the length of 1")
        # the letter will be a letter from A-Z (no comma or number!)
        elif letter.isalpha():
            # if the letter has been chosen before it cannot be chosen again
            if letter in correct_guess_letter or letter in \
                    incorrect_guess_letter:
                print("Letter already guessed" + letter + "Please try again!")
            # if the letter passes every criteria above it will exit the
            # negative feedback loop and stand as valid
            else:
                is_letter_valid = True
        else:
            # an error message if the letter chosen is not a letter from a-z
            print("letter must be from a-z")

    return letter