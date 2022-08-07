<h1 align="center"> Hangman python game! </h1>

<h2>USER EXPERIENCE</h2>
<p>
    <ul>
    <li>First of all, I want the user to simply enjoy a very simple game of hangman, which should run without issues, and if any unnacceptable guesses are entered an appropriate message will be displayed to tell the player of what they must do in order to get a valid guess, for example "The letter must be from a-z"
    </li>
    <li>Secondly, I want the player to be able to play the game a couple of times without getting the same five words in a row, hence time and random was imported and then a function was used to seed the randomness into the game, making it seem like the computer chooses a word randomly from the list of words it has been given
    </li>
    <ul>Thirdly, I want the player to have an easy time differentiating between what is the hangman drawing and where they can input their guess. Hence appropriate guiding text will show where the input will be, as well as if a letter is guessed incorrectly it will be dislpayed above, so the player will know what they have already guessed.
    </li>
    </ul>
    <h3>Design</h3>
    <p>
    The design is rather simple, as it is a game run only in the commandline interface created only using python, with no HTML and CSS as a backbone, however using the keys on the keyboar the hangman was "drawn" with the style of ascii to provide visual support of how many tries/lives the player has left before they either loose the game or win it.</p>
</p>

<h2>FEATURES</h2>
<p>
This is a simple game of hangman played in the terminal of the code, the game chooses a random word from the file called listofwords.py (the randomness is seeded into the code using the imports of time and random to build a randomness function). The words will, before any guesses, be displayed by dashes to show how long the chosen word will be. depending on if the guess from the player is incorrect or correct it will be appended to either the correct list of words or the incorrect list of words. The computer will compare the guesses to the chosen word and if the player guesses all the letters before all the lives has been lost (aka the hangman has been fully drawn) the game will display a "You win!" message, if not guessed before the hangman has been completeda different message will be displayed telling the player of their loss.
</p>
<ul>
    <li>An appropriate message will show for the user if an invalid input has been made</li>
    <li>A hangman will be drawn everytime the player makes an incorrect guess, until there are no lives left and the player will loose</li>
    <li>The list of words used in the game is in a separate file for a cleaner look when there are a larger amount of words</li>
</ul>

<h2>TECHNOLOGIES</h2>
<section>
    <h3>Languages</h3>
    <ul>
        <li>Python</li>
    </ul>
</section>
<section>
    <h3>Frameworks, libraries and programs used</h3>
    <ul>
        <li> [Git](https://git-scm.com/) was used to commit to git and then pushed to github using the gitpod terminal </li>
        <li> [Github](https://github.com/) was used to store the code for the project after it was pushed from git. </li>
        <li> [Python template](https://github.com/Code-Institute-Org/python-essentials-template) from Code Institute was used to import and install the necessart libraries and other good files to make a good up and running python project </li>
    </ul>
</section>

