# list []

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["kim", "cho", "park"]

# where cho is?
print(subway.index("cho"))

# when new one comes in
subway.append("ha")
print(subway)

# want to add jung btw kim and cho
subway.insert(1, "jumg")
print(subway)

# want to remove from back
print(subway.pop())
print(subway.pop())
print(subway)

# how to check how many people with same name
subway.append("kim")
print(subway)
print(subway.count("kim"))

# how to order
num_list = [5, 4, 1, 3, 2]
num_list.sort()
print(num_list)

# how to order back
num_list.reverse()
print(num_list)

# how to remove everything in the list
num_list.clear()
print(num_list)

# can put mutiple type in the list
num_list = [4,2,4,3,5]
mix_list = ["kim", 20, True]
print(mix_list)

# how to add list
num_list.extend(mix_list)
print(num_list)