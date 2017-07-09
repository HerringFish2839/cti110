# File Display
# 7/5/17
# CTI-110 M6T1 - File Display
# Bryce Herring
#

# Open the file.
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Close the file.
myfile.close()
