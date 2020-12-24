'''
Quiz > doing coding contest
doing comment event
one of commenter gets chicken coupon, and other 3 receives coffee coupon
create a progream

1. 20 people wrote review, their id is 1 ~ 20
2. doing random pick but not same person
3. need to use shuffle and sample from random module

'''

from random import *
users = range(1, 21) # 1 to 20
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # in 4 people 1 is chicken , 3 are coffee

print("-- winners --")
print("chicken : {0}".format(winners[0]))
print("coffee : {0}".format(winners[1:]))
print("-- congratz --")