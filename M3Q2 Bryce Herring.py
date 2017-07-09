# Question M3Q2_A-N
# Bryce Herring
# 6/13/17

sample = int(input("Enter your sample in Fahrenheit: "))

if sample > 212:
    print('The sample is steam and its state of matter is gas')
elif sample > 32:
    print('Its state of matter is liquid')
else:
    print('The sample is ice and its state of matter is solid')
