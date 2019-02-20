#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:42:36 2019
   hjkjhkjh
@author: chuckdye
"""
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


whil1 = 1
while whil1 > 0:
    x = input("would you like to begin?   ")
    if x == 'YES' or x == 'yes' or x == 'Yes':
        input("""
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              You find yourself in your small town's local tavern.
              Your name is Pepe, and you are a failing Bard slowly
              turning to alcohol and prostitution to make ends meet.
              In a moment of brief sobriety, You decide the path to
              creating your magnum opus and finding fame, lies in 
              having a grand adventure... And yet, you do not know
              where to find one. (press ENTER to continue)
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              """)
        
        whil1 -= 1
    else: print('I\'m sorry, What?')
whil2 = 1
while whil2 > 0:
    print(chr(27) + "[2J")
    x = input('''
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              You find yourself talking to the bartender about your
              predicament, He lends a sympathetic ear, not because 
              he cares, but because you are his best customer.
              He tells you \"If your\'re looking for adventure. I
              know where you can start! The town has pulled some 
              money together and set a bounty on anyone who can clear
              the local shrine of monsters! Be careful... It\'s real 
              dangerous! (COMMANDS: LEAVE bar ORDER another drink)
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              
              ''')
    if x == 'LEAVE' or x == 'Leave' or x == 'leave':
        print(chr(27) + "[2J")
        input('''
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              You find new hope as you leave the bar. As you reach
              the door you hear someone shout \'Wait!\' You turn 
              around to see a rag-tag group of adventurers standing
              together. They ask to join you on your way to clear
              the shrine, as they had recently lost their homes.
              They introduce themselves...\"I\'m Kat! I can steal any
              object from any hand!\" said the long dark haired Half
              Elf with a black cat perched on her shoulder. \'And I
              am Boots!\' said the large man with a great ax strapped 
              to his back. 'My name is Anna Lucia' said the shy girl 
              with blonde straight hair. (ENTER to continue...)
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ''')
        break
    elif x == 'ORDER' or x == 'Order' or x == 'order':
        print(chr(27) + "[2J")
        input('''
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              You grab your mug and order it filled after the bartender
              is finished speaking. Behind you approaches a rag-tag group
              of travelers. They say they are interested in helping you 
              clear out the shrine. You ask for their names and they 
              introduce themselves... \"I\'m Kat! I can steal any
              object from any hand!\" said the long dark haired Half
              Elf with a black cat perched on her shoulder. \'And I
              am Boots!\' said the large man with a great ax strapped 
              to his back. 'My name is Anna Lucia' said the shy girl 
              with blonde straight hair. (ENTER to continue...)
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ''')
        break
    else:
        print('I didnt catch that...')
