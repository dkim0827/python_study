'''
- doing 4 study // 3 online 1 offline
- need to make program that choose offline study date

1. need to pick random date
2. since each month has different date date need to be in 28th
3. need to exclude first 1~3 days of month due to preparation
'''

from random import *
skipdate = randint(1, 3)
date = randint(skipdate, 28)
print("offline study date is", date, "of every month")