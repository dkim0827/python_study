print(abs(-5)) # 5 // absolute value
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

# will import everything from math library
from math import *
print(floor(4.99)) # 4
print(ceil(3.14)) # 4
print(sqrt(16)) # 4

# will imnport everything from math library
from random import *

print(random()) # 0.0 < 1.0
print(random() * 10) # 0.0 < 10.0
print(int(random() * 10)) # 0 < 10
print(int(random() * 10) + 1) # 1 <= 45

print(randrange(1, 45)) # 1 < 45
print(randint(1, 45)) # 1 <= 45