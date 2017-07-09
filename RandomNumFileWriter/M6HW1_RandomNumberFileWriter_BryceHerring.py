# Random Number File Writer
# 7/8/17
# CTI-110 M6HW1 - Random Number File Writer
# Bryce Herring
#

import random

infile = open("Multi Numbers.txt", "w" )
#Writes the numbers counted based on the inputed number.
for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 500))
    infile.write(line)
    print(line)

infile.close()
#Prints how many numbers the file will hold based on the written numbers.
print("\nReading the file now." )
infile = open("Random.txt", "r")
print(infile.read())
infile.close()
