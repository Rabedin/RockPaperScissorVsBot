# A rock paper scissors bot to play lonely games with

# Importing necessities
import random

# Prompting the player for their choice of rock, paper or scissors
playerChoice = input('Would you like to play Rock, Paper or Scissors')
# Debug line for print player choice
# print (f"The player's choice is {playerChoice}")

# Defining array of possible choices
choices = ['rock','paper','scissors']
# Debug line for print choices array
# print(f"The list named Choices is: {choices}")

# Random number generator for the bot's choice
botChoice = random.choice(choices)
# Debug line for print bot choice
# print (f"The bot selected option is {botChoice}")

# Comparing bot choice to player choice
if playerChoice in choices:
    if botChoice != playerChoice:
        if botChoice == 'rock':
            if playerChoice == 'scissors':
                print("Bot wins")
            else:
                print("Player wins")
        elif botChoice == 'scissors':
            if playerChoice == 'paper':
                print("Bot wins")
            else:
                print("Player wins")
        else:
            if playerChoice == 'rock':
                print("Bot wins")
            else:
                print("Player wins")
    else:
        print("It's a draw")
else:
    print(f"Sorry, {playerChoice} is not one of the possible plays. Please try again.")