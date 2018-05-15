#This allows us to create a random number late in the game using the random function
import random

#Define the playagain function to be used later when the game starts
def playagain():
    #note that we are using raw_input here instead of input to suppress errors
    playagainboolean = raw_input("Play Again? Enter y or n")
    if(playagainboolean != "y"):
        end()
    else:
        startgame()

#Define the function to end the game
def end():
    print "Thanks for playing!"
    return 0

#Define the function we called earlier to start the game
def startgame():
    print "The game is starting.."
    playagain()



#Tell the python interpreter to start the game with the playagain function - note that
#   until this point, no functions have been called so nothing will run.
playagain()
