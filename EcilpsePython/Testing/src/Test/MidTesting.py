
#Define the playagain function to be used later when the game starts
def playagain():
    #note that we are using raw_input here instead of input to suppress errors
    playagainboolean = raw_input("Play Again? Enter y or n")
    if(playagainboolean != "y"):
        end()
    else:
        game()

#Define the function to end the game
def end():
    print "Thanks for playing!"
    return 0
    


#Calculating maximum and minimum
def maxmin():
    global guess
    global high
    global low
    high = max(numbers)
    low = min(numbers)
    
def repeat():
    global numbers
    import collections
    global rep
    global size
    numbers.append(guess)
    rep = [item for item, count in collections.Counter(numbers).items() if count > 1]
    size = len(rep)
    

#Amount of tries
def trys():
    if guess != number:
        global tries
        tries+= 1
        if tries > 15:
            print "This must be a hard number, If you're tired remember you can always quit."
def firsttry():
    #Checking the number
    global guess
    guess = 50
    print "\nP.S You are allowed to 'quit' at anytime but that's no fun and i'll win. :)"
    print "\n","My guess is",guess
    highlower()

def highlower():
    global guess
    global number
    global high
    global size
    global tries
    global numbers
    numbers = []
    tries = 0
    highlow = 0
    size = 0
    while (highlow != "equal" or guess != number):
        highlow = raw_input("Is your number higher, lower or equal to my guess\n")
        #Higher numbers and incrementing
        if highlow == "higher":
            if number < guess:
                check()
                break
            elif guess%25 == 0 and size == 0 and tries < 5:
                guess+= 25
            elif size < 2 and guess < 100 and guess+10 <=100:
                guess+= 10
            elif guess < 101:
                guess+=1
            #Calling varibles
            repeat()
            trys()
            maxmin()
            print "\n",'My new guess is',guess
        #Lower numbers and decrementing
        elif(highlow == "lower"):
            if number > guess:
                check()
                break
            elif guess%25 == 0 and size ==0 and tries < 4:
                guess-= 25
            elif size < 2 and guess > 0 and guess-10 >= 0:
                guess-= 10   
            elif guess > -1:
                guess-=1
            #Calling variables   
            trys()
            repeat()
            maxmin()
            print "\n",'My new guess is',guess
        #Equal numbers and optional quitting
        elif(highlow == "equal"):
            print "My guess was",guess
            print "Your number was",number
            check()
        elif(highlow == "quit"):
            print "\nAww that sucks :(. Better luck next time."
            print "I tried",tries," times."
            playagain()
            break
#Checking if you lied or not
def check():
    global guess
    global tries
    global high
    global rep
    global low
    #If you told the truth
    if guess == number:
        print 'Yay! I guessed your number in',tries,'tries'
        print "The max guess was ",high,'and the min guess was ',low
        print "\nRepeated numbers were: ",rep
        playagain()
    #If you lied
    elif guess != number:
        print '\nIt is not good to lie T-T'
        print 'Since you lied, My guesses start over :P'
        guess = 50
        print "\n",'My 1st guess is',guess, "\n"
        highlower()

#starts game
def game():
    global number
    number = input("Enter a positive number less than 100 ")
    if number < 100:
        if number > 0:
            print "Correct input", number
            firsttry()
        else:
            print "Try Again, it must be positive"
            game()
    else:
        print "Incorrect, must be under 100."
        game()
game()

