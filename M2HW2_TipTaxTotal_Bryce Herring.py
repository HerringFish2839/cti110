# A brief description of the project
# 6/8/17
# CTI-110 M2HW1 - Distance Traveled 
# Bryce Herring
#

FoodCharge = float( input( "Please enter the charge of the food: " ) )

Tip = 0.18 * FoodCharge

SalesTax = 0.07 * FoodCharge

Total = FoodCharge + Tip + SalesTax

print( "Food Charge: $" + format( FoodCharge, ",.2f"), "Tip: $" + \
       format( Tip, ",.2f" ), "Sales Tax: $" + format( SalesTax, ",.2f"), \
       "Total: $" + format( Total, ",.2f"), sep = "\n" )

