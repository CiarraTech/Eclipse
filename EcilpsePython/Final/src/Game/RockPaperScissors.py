'''
Created on Dec 7, 2015

@author: Ciarra Whisenhunt
'''
print '\nYou picked Rock, Paper, Scissors!'
 
def start():
       global hwin
       global cwin
       global hloss
       global closs
       global ties
       global rounds
       
       cwin = 0
       hwin = 0
       closs = 0
       hloss = 0
       ties = 0
       rounds = 1
       human()

def computer():
       import random
       global compnum
       
       num = random.randrange(1,4)

       if num == 1:
              compnum = "rock"
       elif num == 2:
              compnum = "paper"
       elif num == 3:
              compnum = "scissors"
       else:
              print "Technical Error ...."
              start()
       print 'Computer choice is: ',compnum
       compare()
def human():
       global numh
       numh = raw_input("\nChoose rock, paper, or scissors: ")

       if numh == "rock":
              print '\nYou choose: ',numh
              computer()
       elif numh == "scissors":
              print '\nYou choose: ',numh
              computer()
       elif numh == "paper":
              print '\nYou choose: ',numh
              computer()
       else:
              print 'Try Again.'
              human()
       
def compare():
       global compnum
       global numh
       global ties
       global cwin
       global hwin
       global closs
       global hloss
       #TIE
       if compnum == numh:
              print "It's a tie!"
              ties+=1
              checkpoint()
       
       #Computer Wins#
       if compnum == "rock" and numh == "scissors":
              print 'The computer wins!'
              cwin+=1
              hloss+=1
              checkpoint()
       if compnum == "paper" and numh == "rock":
              print 'The computer wins!'
              cwin+=1
              hloss+=1
              checkpoint()
       if compnum == "scissors" and numh == "paper":
              print 'The computer wins!'
              cwin+=1
              hloss+=1
              checkpoint()
       #Human Wins#
       if numh == "rock" and compnum == "scissors":
              print 'You win!'
              hwin+=1
              closs+=1
              checkpoint()
       if numh == "paper" and compnum == "rock":
              print 'You win!'
              hwin+=1
              closs+=1
              checkpoint()
       if numh == "scissors" and compnum == "paper":
              print 'TYou win!'
              hwin+=1
              checkpoint()

def checkpoint():
       global cwin
       global hwin
       global closs
       global hloss
       global ties
       global rounds
       print '\n- - - Status - - - '
       print 'Ties:  ',ties
       print 'Comp:  ',cwin,'win  ',closs,'loss'
       print 'Human: ',hwin,'win  ',hloss,'loss\n'
       print 'ROUND :',rounds
       print '- - - - - - - - - - - -'
       rounds+=1
       results()

def results():
       global cwin
       global hwin
       global ties
       global rounds

       if rounds > 4:
              print "\nTime for the results!"
              if cwin == hwin and ties == 2:
                     print "TIE BREAKER!!!"
                     ties+=1
                     human()
              if cwin == hwin and ties > 2:
                     print "It's a tie!"
              #human()
              if cwin > hwin:
                     print "The computer wins the game! \nBetter luck next time!"
                     return 0
              elif hwin > cwin:
                     print "You won the game!! CONGRADULATIONS!"
                     return 0
       else:
              human()
#checkpoint()
start()
