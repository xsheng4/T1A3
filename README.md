# T1A3 - Terminal Application

This particular application simulates a game that is based off the British television show "Countdown".

Please refer to the [Help Documentation](#help-documentation) section on instructions to install the application and rules on how to play the game.

[Github Repository](https://github.com/xsheng4/T1A3)

## Features

This application contains six different scripts which all work in conjunction for a smooth experience and ensuring that all the main features of the application works.
There is also a text file which contains the current high score which can be changed/editted if a new high score appears.

The application's main purpose is for users to be able to play the game "Countdown" just from running the application.

### Random Letter Generator

Users are able to randomly generate letters up to nine times depending on their choice of "consonant" or "vowel". Users are prompted to enter "consonant" or "vowel" and based off the input, a random consonant or vowel is returned. This is repeated nine times.

### Dictionary API

The application also includes a dictionary API that can be used to look up the definition of the word or check if a word really exists in the English dictionary. The API utilises the free and publie API key that can be found on the Merriam-Webster developer website.

### High Score Sheet

This application features a high score sheet where the current high score can be displayed and editted. It utilises a separate text file that stores the high score, then uses a script to read the text file and print out the current high score. There is also an option to change or delete it if needed.

## Help Documentation

### Dependencies

You need to have Python 3 installed in order to run the application. The application will also automatically install and use the following upon launch:

- certifi==2024.2.2
- charset-normalizer==3.3.2
- colored==2.2.4
- idna==3.7
- requests==2.31.0
- urllib3==2.2.1

### Installation

To install this application, please download the **src** folder containing the source code of the project.

Run the **run.sh** bash script which will set up a virtual environment and start the application for you automatically.

> If you have trouble running the script. Try running the following command in your terminal to make the script executable

```bash
chmod +x run.sh 
```

---

### Using the Application

#### Main Menu

As soon as the application starts, you will be presented with the main menu. You are able to choose one of four options:

- Start the game
- Open the dictionary function
- View and edit the high score
- Exit the program

#### Playing the game

If you have selected option 1 to start the game, it will immediately commence a new game and prompt you to choose between a vowel or consonant.

Depending on your choice, a random vowel or consonant will be printed. This will then be repeated eight more times for a total of nine times. Each player can take turns choosing between a vowel or consonant. You can have as many players as you want!

Once all nine letters have been generated, players are then to attempt to spell out the longest word they can with the given letters using each letter only once. 

#### Dictionary Function

If option 2 has been selected, or all nine letters have been printed, it will prompt you if you need to open the dictionary function to check the spelling/definition of a word.

Simply enter the word you want the definition of and it will print out the definition given it is an actual word and/or is spelt correctly.

#### High Score

Selecting option 3 in the main menu, or after the dictionary step in the game will prompt you to enter a new high score if needed. 

The scoring of the game can be completely up to each player, but generally the player with the longest word usually gets one point and each additional time they win again, they get another point.

If a new score needs to be entered, or the high score needs to be editted/removed, the high score function will first prompt for an input depending on what action wants to be done.

"N" for a new high score, "E" to erase the existing high score or "Q" to exit.

If a new high score needs to be input, it will prompt you to enter the high score after the "N" is input.

It will then print and display the new high score.

