# Bug Collector
# 6/14/17
# CTI-110 M4T1 - Bug Collector
# Bryce Herring
#

total = 0

for day in range(1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

print('You collected a total of', total, 'bugs.')
