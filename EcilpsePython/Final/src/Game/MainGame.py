'''
Created on Dec 7, 2015
@author: Ciarra Whisenhunt
'''

# Using Java or Python write a program that lets the user choose between 2 programs and play
#    
# (1) a program that plays Rock, Paper, Scissors.
# (2)a program that allows 2 players to play hangman. The first one enters the word and the 2nd person guesses

def start():
    #import subprocess
    playagainboolean = raw_input("\nWould you like to play Hangman (1) or Rock, Paper, Scissors (2)? ")
    if(playagainboolean == "2"):
        import RockPaperScissors
        end()
    elif(playagainboolean == "1"):
        import Hangman  
        end()
    else:
        start()


#Define the function to end the game
def end():
    print "\nThanks for playing!"
    return 0

start()

