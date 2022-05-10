"""Task 3: Input guesses of a random number between 1 and 100 and keep count of the guesses"""

def guessing_game():
    #inport ranodom
    import random
    #make a counter for the user guesses
    guess = 0
    #Generate a random interger between 1 and 100
    random_num = random.randint(1,101)
    #make a while loop for the game
    game = 0
    while game != 1:
        #ask the user for an input
        user_guess = int(input("Please enter a guess between 1 and 100: "))
        #check if the users inout was the same as the random number
        if user_guess != random_num:
            #if not diplay try again message and add onme to the guess counter
            guess = guess + 1
            print("Incorrect guess, please try agian")
        else:
            #if guess correct
            #print well done message
            #display number of guesses
            print("well done that guess was correct")
            print("your had", guess, "guess(es)")
            #complete while loop
            game = game + 1
            
guessing_game()