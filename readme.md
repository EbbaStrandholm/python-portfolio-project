<h1 align="center"> Hangman python game! </h1>

[View the live project here](https://ebba-strandholm-hangman.herokuapp.com/)

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

[Git](https://git-scm.com/) was used to commit to git and then pushed to github using the gitpod terminal
<br>

[Github](https://github.com/) was used to store the code for the project after it was pushed from git.
<br>
    
[Python template](https://github.com/Code-Institute-Org/python-essentials-template) from Code Institute was used to import and install the necessart libraries and other good files to make a good up and running python project

<br>

[Heroku](https://heroku.com) was used to deploy the project

</section>

<h2>TESTING</h2>

[PEP8](http://pep8online.com/) checks the projects code, both the listofwords.py file and the run.py file, was run through the pep8 online check without any notifications of any errors

<br>

<p>
The code was also continuously debugged inside gitpod, there are some warnings still active, which react to there being no assigned value to the global variable, but as the game runs these variable will update and the game runs smoothly, so I have decided to not mind these warnings as there has been no proof of them causing trouble for my project code. 
</p>

<br>

<p>
There is also some infos active which wants there to be a change in the naming style of the global variables, which I have decided against as the lower case naming style works just as well for this project, and makes (for me), an overall much cleaner look.
</p>

<br>

<p>
While in the early stages of testing my code in the terminal, no area for input was given and the game started, but couldn't be played by the user, this was solved by changing from the recommended enumerate function to an range(0, len(accepted words)) function. This is pointed out in the infos when debugging, but as the recommended enumerate would not work with this project I have decided to not use that recommendation and instead keep to the range fuunction previously mentioned. 
    <p>Another issue I ran into was that no matter if the letter was correctly guessed or not the computer would not count it as correct, and hence the player could only ever loose the game. This issue was solved as I found a typing error where I had mistakenly written append.lower() instead of the append.upper(). This made the computer compare two different things as it is case sensitive, once that was fixed the game ran smoothly without any issues.
    </p>
</p>

<h2>DEPLOYMENT</h2>
<h3>Github pages and Heroku</h3>
<p>

1. Log into github and locate the [Github Repository](https://github.com/EbbaStrandholm/python-portfolio-project)
2. At the top of the repository locate the settings button
3. Scroll down the page until you find the github pages sectino
4. Under "source" click the dropdown called "none" and select "master branch"
5. The page will refresh and published link will now be available
6. 

</p>

<h2>CREDITS</h2>

<p>
As this project is a resubmission I was a little short on time, so I chose to follow a tutorial for a hangman game on youtube but making a different list in a separate file, the words used for the game is different and so are the names of the definitions and style of comments as well.
</p>

1. [tutorial from CS students](https://www.youtube.com/watch?v=ynwB-QfOPRw&t=305s) This is the tutorial which I followed to get a working hangman game for this python project
2. [tutorial from kite](https://www.youtube.com/watch?v=m4nEnsavl6w&t=135s) This tutorial gave me the idea of creating a second python file which contains the words of which the computer will randomly choose from, but the contents of the list are my own.
3. [Python template](https://github.com/Code-Institute-Org/python-essentials-template) was referenced to create an appropriate readme.md file for this project

<h3>Acknowledgments</h3>

1. My mentor for continous support throughout this project
2. Friends and family for proof reading and testing my project to see if it works as a player and not the creator
3. The Code Institute student care team for the help with resubmission