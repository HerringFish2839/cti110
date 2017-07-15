# CityOfPuzzles
# 7/13/17
# CTI-110 M9FinalProject - City Of Puzzles
# Bryce Herring
#

import random
import time

MyOptions1 = ['left','right']
#BlueDessert
def displayIntroTwo():
    print('The blue dessert is surronded by blue sand,')
    print('you are confused and have no where to go,')
    print('you begin make a move.')
    print()

def ChooseSideTwo():
    SideTwo=''
    while SideTwo != 'left' and SideTwo != 'right':
        print('Where will you start? type (left or right)')
        SideTwo = input()
    return SideTwo

def CheckSideTwo(ChosenSideTwo):
    print('You hear something')
    time.sleep(2)
    print('You start running...')
    time.sleep(2)
    print('You hear the sound coming closer and...')
    print()
    time.sleep(2)

    RandomSideTwo = random.choice(MyOptions1)

    if ChosenSideTwo == str(RandomSideTwo):
         print('A person appears')
    else:
         print('A horse appears')
             
def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        Playgame()
        print('Do you want to play again? (yes or no)')
        playAgain = input()
        
def Playgame():

#BlueDessert
    displayIntroTwo()

    SideWordTwo = ChooseSideTwo()

    CheckSideTwo(SideWordTwo)

main()
