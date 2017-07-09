# Random Number Guessing Game
# 6/17/17
# CTI-110 M5HW2 - Random Number Guessing Game
# Bryce Herring
#

#Supports the random number code.
import random

#Generates a random number.
def gen_num():
    random_num = random.randint( 1, 100 )
    return random_num

#The player picks a number.
def ask_num( message = "Pick a number: " ):
    user_num = int( input( message ) )
    return user_num

#Checks the player's number.
def check_num( user_num, random_num ):
    if user_num > random_num:
        return "Lower"
    elif user_num < random_num:
        return "Higher"
    else:
        return "Great Job!"

#Counts the number of attempts the player took to get to the correct guess.
def main():
    UserWon = False
    LetsPlay = True

    while UserWon or LetsPlay:
        guess_num = 0 
        random_num = gen_num()
        user_num = ask_num()
        guess_num += 1
        message = check_num( user_num, random_num )

        while message != "Great Job!":
            print( message )
            user_num = ask_num( "Try again: " )
            guess_num = guess_num + 1
            message = check_num( user_num, random_num )
        
        print()
        print( message, "You guessed: ", guess_num,\
           " times to guess correctly\n" )
        UserWon = True

main()
