'''
Created on Dec 7, 2015
@author: Ciarra Whisenhunt
'''

# Using Java or Python write a program that lets the user choose between 2 programs and play
#    
# (1) a program that plays Rock, Paper, Scissors.
# (2)a program that allows 2 players to play hangman. The first one enters the word and the 2nd person guesses

def start():
    playagainboolean = raw_input("Would you like to play Hangman (1) or Rock, Paper, Scissors (2)? ")
    if(playagainboolean != "1"):
        import RockPaperScissors  # @UnusedImport
        RockPaperScissors
        playagain()
    else:
        import Hangman  # @UnusedImport
        Hangman
        playagain()       

def playagain():
    playagainboolean = raw_input("Play Again? Enter yes or no \n")
    if(playagainboolean != "yes"):
        end()
    else:
        start()

#Define the function to end the game
def end():
    print "Thanks for playing!"
    return 0

start()

