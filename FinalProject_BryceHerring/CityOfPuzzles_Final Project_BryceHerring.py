# CityOfPuzzles
# 7/13/17
# CTI-110 M9FinalProject - City Of Puzzles
# Bryce Herring
#

import random
import time

MyOptions = ['red','blue']

#Section 1 (Introduction)
def displayIntro():
    print('You have arrived in the City of Puzzles,')
    print('in the city, a fire ignites before you')
    print('the fire is half red and half blue. the fire tells you to choose a side')
    print('you asked the fire a question but no answer.')
    print()

def ChooseSide():
    Side = ''
    while Side != 'red' and Side != 'blue':
        print('The fire asks what side will you choose? type (red or blue)')
        Side = input()

    return Side

def CheckSide(ChosenSide):
    print('You choose a side...')
    time.sleep(2)
    print('You wait for an answer...')
    time.sleep(2)
    print('The fire glows and...')
    print()
    time.sleep(2)

    RandomSide = random.choice(MyOptions)

    if ChosenSide == str(RandomSide):
         print('Teleports you in the forest of red')
         import RedForest
    else:
         print('Teleports you in the blue dessert')
         import BlueDessert

def main():
    
    displayIntro()

    SideWord = ChooseSide()

    CheckSide(SideWord)

main()


