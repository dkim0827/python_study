from random import *

number_of_customer = 0

for i in range(1, 51):
    random_time = randrange(5, 51) # 5 - 50
    if 5 <= random_time <= 15:
        print("[O] {0}th customer(time spent : {1}min)".format(i, random_time))
        number_of_customer += 1
    else:
        print("[ ] {0}th customer(time spent : {1}min)".format(i, random_time))
print("Total number of customer : {0}".format(number_of_customer))