#!/usr/bin/env python3

# A rock paper scissors bot to play lonely games with

# Importing necessities
import random

# Prompting the player for their choice of rock, paper or scissors
print("Would you like to play rock, paper, or scissors?")
playerChoice = input()

# Defining array of possible choices
choices = ['rock','paper','scissors']

# Creating a dict full of all the possible matchups
strats = {
    'rock': {
        'scissors':'win',
        'paper':'lose',
        'rock':'draw'
    },
    'paper': {
        'rock':'win',
        'scissors':'lose',
        'paper':'draw',
    },
    'scissors': {
        'paper':'win',
        'rock':'lose',
        'scissors':'draw'
    },
}

# Randomized choice selection for bot
botChoice = random.choice(choices)

# Comparing bot choice to player choice
if playerChoice in choices:
    if strats[playerChoice][botChoice] == 'win':
        print("Player wins")
    elif strats[playerChoice][botChoice] == 'lose':
        print("Bot wins")
    else:
        print("It's a draw")
else:
    print(f"Sorry, {playerChoice} is not one of the possible plays. Please try again.")
