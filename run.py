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


def guess_letter():
    """ This fucntion will check wether the answer is correct or incorrect and
    update the global variables accordingly """
    global correct_guess_letter
    global incorrect_guess_letter
    global lives

    letter = one_valid_letter()
    # if the guessed letter is in the randomly chosen word, append the letter
    # to correct_guess_letter
    if letter in random_chosen_words:
        correct_guess_letter.append(letter)
    else:
        # if the the chosen word is incorrect remove one life and append to
        # the incorrect_guessed_letter
        incorrect_guess_letter.append(letter)
        lives -= 1


def check_game_over():
    """ This fucntion will check wether the player has won or
    lost the hangman game """
    global lives
    global is_game_over
    global correct_guess_letter

    # if the lives left are less than or equal to 0 then game over is true and
    # the hangman will be drawn
    if lives <= 0:
        is_game_over = True
        create_hangman()
        print("You lost! Correct:" + random_chosen_words + ". Try again!")
    else:
        all_letters_correct = True
        for letter in random_chosen_words:
            # if all_letters_correct is false then it will break out of the
            # positive feedback loop and check the next segment
            if letter not in correct_guess_letter:
                all_letters_correct = False
                break
        # if all the letters are correct and there are no more letters to
        # guess then a message will display showing that you have won the game
        if all_letters_correct:
            is_game_over = True
            print("You've won! Congratulations! Feel free to try again!")


def main():
    """ Will call the previously written fucntions into a game loop """
    global is_game_over

    print("!WELCOME TO HANGMAN!")
    random_word()

    while is_game_over is False:
        create_hangman()
        word_before_guess()

        if len(incorrect_guess_letter) > 0:
            print("Incorrect guesses: ")
            print(incorrect_guess_letter)

        guess_letter()
        check_game_over()


if __name__ == "__main__":
    main()
