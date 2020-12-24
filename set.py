# set
# not able to have multiple times, no order
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {"jaeppa", "joon", "kim"}
python = set(["yoo", "jaeppa"])

# print person who can do both java and python
print(java & python)
print(java.intersection(python))

# person who can do either python or java
print(java | python)
print(java.union(python))

# person who only can do java
print(java - python)
print(java.difference(python))

# now more people can do python
python.add("kim")
print(python)

# forgot java
java.remove("joon")
print(java)