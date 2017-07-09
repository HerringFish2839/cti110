# Sum of Numbers
# 7/8/17
# CTI-110 M6LAB - Lab
# Bryce Herring
#

def main():
    try:
        numbersFile = open( "numbers.txt", "r" )
    #The error prints only if the file is not found.
    except Exception as error:
        print( "There was an error opening the file:", error )
    #Adds all the numbers in the numbers.txt file.
    else:
        total = 0

        for line in numbersFile:
            total = total + int( line )

        print( "The numbers in the file sum up to", total )

        numbersFile.close()

main()
