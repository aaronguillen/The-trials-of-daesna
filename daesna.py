#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created on Mon Feb 18 16:42:36 2019

@author: chuckdye and aaronguillen

Python 3.7.2
"""

from textwrap import wrap

# Global Variables
MAX_TEXT_WIDTH = 40

# Just a function to standardize our blocks of descriptive text
def decision_text(text):
	MAX_TEXT_WIDTH = 53
	print("~" * MAX_TEXT_WIDTH)
	for i in wrap(text, MAX_TEXT_WIDTH):
		print(i)
	print("~" * MAX_TEXT_WIDTH)

# Citation for the below function:
# https://stackoverflow.com/questions/2084508/clear-terminal-in-python
def clear_screen():
	from os import system, name
	system('cls' if name == 'nt' else 'clear')

# A function for checking input again a provided list of actions
def string_in_list(check_this_string, string_list):
	for i in string_list:
		# Make everything lower case, that was we don't have to worry about what case they used in their input
		if check_this_string.lower() == i.lower():
			return True
	return False


# Opening Banner
print("""
      WELCOME TO THE TRIALS OF DESNA...
                                 ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((
      """)


# Set our loop variable to something that will fail on the first iteration (so that we can enter the loop)
x = ""

while not string_in_list(x, ["yes", "no"]):
	x = input("Would you like to begin?\t==> ")
	if x.lower() == "no":
		print("Okay! Exiting. Bye!")
		exit()
	elif x.lower() == "yes":
		decision_text("You find yourself in your small town's local tavern. Your name is Pepe, and you are a failing bard slowly turning to alcohol and prostitution to make ends meet. In a moment of brief sobriety, you decide the path to creating your magnum opus and finding fame lies in having a grand adventure... And yet, you do not know where to find one.")
		input("(Press ENTER to continue)")
	else:
		print("I'm sorry, what?")

clear_screen()

# Reset input for the next loop
x = ""

# Same idea as above.
while not string_in_list(x,["leave", "order"]):
	decision_text("You find yourself talking to the bartender about your predicament. He lends a sympathetic ear, not because he cares, but because you are his best customer. He tells you, \"If your're looking for adventure. I know where you can start! The town has pulled some money together and set a bounty on anyone who can clear the local shrine of monsters! Be careful... It's real dangerous!")
	x = input("COMMANDS: LEAVE bar ORDER another drink\n==> ")
	clear_screen()

	if x.lower() == "leave":
		decision_text("You find new hope as you leave the bar. As you reach the door you hear someone shout, \"Wait!\" You turn around to see a rag-tag group of adventurers standing together. They ask to join you on your way to clear the shrine, as they had recently lost their homes. They introduce themselves... \"I'm Kat! I can steal any object from any hand!\" says a long, dark haired Half Elf with a black cat perched on her shoulder. \"And I am Boots!\" says a large half orc with a great ax strapped to his back. \"My name is Anna Lucia\" says a shy girl with straight, blonde hair.")
		input("(Press ENTER to continue)")
	elif x.lower() == "order":
		decision_text("You grab your mug and order it filled after the bartender is finished speaking. Behind you approaches a rag-tag group of travelers. They say they are interested in helping you clear out the shrine. You ask for their names and they introduce themselves... \"I'm Kat! I can steal any object from any hand!\" says a long, dark haired half elf with a black cat perched on her shoulder. \"And I am Boots!\" says a large half orc with a great ax strapped to his back. \"My name is Anna Lucia\" says a shy girl with straight, blonde hair.")
		input("(Press ENTER to continue)")
	else:
		print('I didnt catch that...\n')
