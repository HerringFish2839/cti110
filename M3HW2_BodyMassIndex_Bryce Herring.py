# Body Mass Index
# 6/13/17
# CTI-110 M3HW1 - Body Mass Index
# Bryce Herring 
#

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches : "))

BMI = weight * 703/height**2

print("Your BMI is" ,BMI)

if BMI > 25:
    print("You are overweight")
elif BMI < 18.5:
    print("You are underweight")
else:
    print("You are optimal")


