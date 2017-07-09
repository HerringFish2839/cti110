# Random Number File Reader
# 7/8/17
# CTI-110 M6HW2 - Random Number File Reader
# Bryce Herring
#

import random

def main():
        more = 'y'

        while more.lower() == 'y':
                #Inputs a random number and adds the numbers to the output file.
                Rnumbers = open('crazy numbers.txt', 'w')
                NumbersToWrite = random.randint(1, 20)
                print(NumbersToWrite, 'numbers added to the output file: ')
                #Writes and adds the numbers together.
                for count in range(NumbersToWrite):
                      number = random.randint(1, 500)
                      print(number)
                      Rnumbers.write(str(number) + '\n')

                Rnumbers.close()

                Rnumbers = open('crazy numbers.txt', 'r')


                #Reads the added numbers in the file.

                line = Rnumbers.readline()
                number = 0
                total = 0

                while line:
                    number += int(line)
                    total += 1
                    line = Rnumbers.readline().rstrip("\n")
                #Tells the user the total amount of the numbers added to the file. Tells the user the total count of numbers read from the file.
                print("The total of the numbers: " + str(total))
                print("Total count of numbers read from file: " + str(number))
                #Asks the user to run the program again.
                more = input("Do you want to run the program again. (Y/N): ")
                Rnumbers.close()

        print("Thank you")


main()
