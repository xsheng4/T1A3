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

