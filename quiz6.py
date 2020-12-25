'''
measure average weight

(equation)
male : height(m) * height(m) x 22
female : height(m) * height(m) * 21

'''

def std_weight(height, gender): # height is m(number), gender = string
    if gender == "male":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm
gender = "male"
weight = round(std_weight(height / 100, gender), 2) # round up at 2 sigfig
print(f"for {gender} with height {height}. Average weight is {weight}")


#################################

print("Python", "Java", sep=" or ", end=" ? ") # sep = value for each , default is " " end default is line change
print("What will be more fun?")

# import sys
# print("Python", "Fava", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

scores = {"Math":0, "English":50, "Coding":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust = to the left (8) 8 length // rjust = to the right with (4) length


for num in range(1, 21):
    print("Waiting_Num: " + str(num).zfill(3)) # take leng of 3 and fill the parts with 0

answer = input("put random value : ") # receive as string
print(f"value is {answer}")

print("{0: >10}".format(500)) # how to add empty spot at the start

print("{0: >+10}".format(500)) # how to add + or - infront of the number

print("{0:_<+10}".format(500)) # > add to left < add to right

print("{0:+,}".format(100000000000000)) # how to add , btw numbers if you want to add + or - infront of the number need to do 0:+,

print("{0:^<+30,}".format(10000000000000))

# decimal
print("{0:f}".format(5/3))

# decimal sigfig
print("{0:.2f}".format(5/3))