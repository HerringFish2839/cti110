# Age Classifier
# 6/13/17
# CTI-110 M3HW1 - Age Classifier
# Bryce Herring 
#

person = int(input("Enter the person's age: "))

if person >= 20:
    print("The person is a adult.")
elif person >= 13:
    print("The person is a teenager.")
elif person > 1:
    print("The person is a child.")
else:
    print("The person is an infant.")
            
