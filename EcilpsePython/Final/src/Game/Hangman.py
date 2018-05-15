'''
Created on Dec 7, 2015

@author: Ciarra Whisenhunt
'''

print '\nYou picked Hangman!\n'

def firsttry():
    global word
    global letters
    global win
    global loss
    global gword
    global final
    letters = raw_input("Enter a letter ")

    if len(letters) > 1:
        print 'One letter please'
        game()
    
    if letters in word:
        print 'Correct!'
        final = {letters}
        gword = {letters}
        correct()
    else:
        print 'Nice Try'
        final = {letters}
        incorrect()
    
def game():
    global word
    global letters
    global char
    global win
    global loss
    global gword
    global final

    letters = raw_input("Enter a letter ")

    if letters in final:
           print'No repeating letters :P!'
           game()
    if len(letters) > 1:
        print 'One letter please'
        game()
    if letters in word:
       print 'Correct!'
       gword.update(letters)
       final.update(letters)
       correct()
    else:
        print 'Nice Try'
        final.update(letters)
        incorrect()
        
def correct():
    global letters
    global win
    global loss
    global gword
    global word
    global char
    global final
    global baby
    win+=1
    baby = '_ '*len(word)
    
    if gword.issubset(word):
        baby = " ".join([char if char in gword else "_" for char in word])
    check()    
    
def status():   
    print '\nStatus: '
    print 'correct = ',win,', incorrect =',loss
    print 'all letters =',final,"\n"

    
def incorrect():
    global win
    global loss
    loss+=1
    print "Loss is ",loss
    if loss == 1:
        print'       _ _  '   
        print'      |   | '
        print'      |   o '
        print'      |   '
        print'      |   '
        print' _ _ _|_ _ _'
    elif loss == 2:
        print'       _ _  '   
        print'      |   | '
        print'      |   o '
        print'      |   | '
        print'      |    '
        print' _ _ _|_ _ _'
    elif loss == 3:
        print'       _ _  '   
        print'      |   | '
        print'      |   o '
        print'      |  /| '
        print'      |    '
        print' _ _ _|_ _ _' 
    elif loss == 4:
        print'       _ _  '   
        print'      |   | '
        print'      |   o '
        print'      |  /|\ '
        print'      |    '
        print' _ _ _|_ _ _'
    elif loss == 5:
        print'       _ _  '   
        print'      |   | '
        print'      |   o '
        print'      |  /|\ '
        print'      |  /  '
        print' _ _ _|_ _ _'
    elif loss == 6:
        print'       _ _  '   
        print'      |   | '
        print'      |   o '
        print'      |  /|\ '
        print'      |  / \ '
        print' _ _ _|_ _ _'
        print 'You have lost the game :c.'
        print 'The original word was:',word
    if loss <= 5:
           check()
           
def check():
       print "\nguess: ",baby
       if "_" not in baby:
              print"\nCONGRADULATIONS!! You beat hangman :D"
              print'     '   
              print'          '
              print'        \o/ '
              print'         | '
              print'        / \ '
              print'      - - - - '
              
       else:
              status()
              game()

def start():
    global word
    global letters
    global win
    global loss
    global gword
    global final
    global baby
    final = set()
    gword = set()
    win = 0
    loss = 0
    word = raw_input('Please, enter your word.')
    #To hide the word 
    print "\n"*50
    
    if len(word) < 12:
           if len(word) < 2:
              print "You can do better than that."
              start()
    else:
       print "Ohhh a tough one, try an slightly easier word" 
       start()
    baby = '_ '*len(word)
    firsttry()

start()
