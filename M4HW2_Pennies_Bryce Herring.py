
# A brief description of the project
# 6/15/17
# CTI-110 M4HW2 - Pennies for Pay 
# Bryce Herring
#

#Days Worked
DW = int(input("Enter how many days you worked; "))
#Total amount of Pennies
TP = 0

print()

print( "Day\tSalary\n-----\t---------" )
for x in range( DW ):
    PD = 2 ** x
    #Pennies per Day
    TP += PD
    print( x + 1, "\t" , PD )

total = TP * 0.01

print( "\nTotal pay: $", total, sep = "" )
    
