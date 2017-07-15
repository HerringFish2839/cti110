# CityOfPuzzles
# 7/13/17
# CTI-110 M9FinalProject - City Of Puzzles
# Bryce Herring
#

import random
import time

MyOptions2 = ['left','right']
#RedForest
def displayIntroThree():
    print('You are in a forest where everything is red,')
    print('you did not have any idea where to go,')
    print('you start walking in encounter two pathways.')
    print()

def ChooseSideThree():
    SideThree=''
    while SideThree != 'left' and SideThree != 'right':
        print('Which path will you walk? type (left or right)')
        SideThree = input()
    return SideThree
def CheckSideThree(ChosenSideThree):
    print('You hear the sound of leaves,')
    time.sleep(2)
    print('You see something...')
    time.sleep(2)
    print('As you got closer...')
    print()
    time.sleep(2)

    RandomSideThree = random.choice(MyOptions2)

    if ChosenSideThree == str(RandomSideThree):
         print('You see a sign that says "Welcome" ')
    else:
         print('You see a man in red')


def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        Playgame2()
        print('Do you want to play again? (yes or no)')
        playAgain = input()

def Playgame():

#RedForest
    displayIntroThree()

    SideWordThree = ChooseSideThree()

    CheckSideThree(SideWordThree)


main()
