cabinet = {3: "yoo", 100: "kim"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# when 5 is not there it throw error and stops there
# print(cabinet[5])
# when 5 is not there it return as None
print(cabinet.get(5, 'available'))


print(3 in cabinet) # True
print(5 in cabinet) # False

# new customer
print(cabinet)
cabinet[3] = "kim2"
cabinet["c-20"] = "cho"
print(cabinet)

# customer left
del cabinet[3]
print(cabinet)

# only key
print(cabinet.keys())

# only value
print(cabinet.values())

# key, value
print(cabinet.items())

# closed cabinet
cabinet.clear
print(cabinet)