sentence = 'im a boy'
print(sentence)

sentence2 = "python is easy"
print(sentence2)

sentence3 = """
im a boy
ptyhon is easy
"""
print(sentence3)

jumin = "990120-1234567"
print("sex : " + jumin[7])
print("year : " + jumin[0:2]) # 1 more than where you want to stop
print("month : " + jumin[2:4])
print("day : " + jumin[4:6])

print("DOB : " + jumin[:6]) # when it starts of index 0 dont need to put 0
print("last 7 digits : " + jumin[7:]) # also works other way round
print("last 7 digit reverse : " + jumin[-7:])

python = "Python is Amazing"
print(python.lower()) # to lower
print(python.upper()) # to upper
print(python[0].isupper()) # isupper() true or false
print(len(python)) # length of variable

print(python.replace("Python", "Java")) # find "Python" and replace with "Java"

index = python.index("n") # find where variable python includes n
print(index)
index = python.index("n", index + 1)

print(python.find("Java")) # if variable does not include Java it comes out as -1
# print(python.index("Java")) # throw error in index, give -1 in find

print(python.count("n")) # find how many times it came out in the varaible

# way 1
print("i am %dyears old" % 20) # d is int
print("i love %s" % "Python") # s is string
print("Apple start with %c" % "A") #c only include 1 letter

print("i love %s and %s color" % ("red", "blue"))

# way 2
print("im {}years old".format(20))
print("i love {} and {} color".format("red", "blue"))
print("i love {0} and {1} color".format("red", "blue"))
print("i love {1} and {0} color".format("red", "blue"))

# way 3
print("i am {age}age old, i love {color} color".format(age = 20, color="red"))

# way 4(available from v3.6 or higher)
age = 20
color = "red"
print(f"I am {age} old, I love {color}")



####################################################
# \n : lane change
print("you know how cool you are? \n nope!!!!")


# \" : make "" in the string
print("I am \"Daniel\"")

# \\ : turn into \ in the string
print(":C\\Users\\Documents")

# \r : move cursor to very front
print("Red Apple\rPine") # PineApple

# \b : backspace
print("Redd\bApple") # RedApple

# \t : tab
print("Red\tApple")