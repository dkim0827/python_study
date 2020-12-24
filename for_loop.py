for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("waiting_number : {0}".format(waiting_no))


starbucks = ["ironman", "thor", "iamgroot"]

for customer in starbucks:
    print(f"{customer}, your order is ready")


# while
customer = "thor"
index = 5
while index >= 1:
    print("{0}, coffee is ready. {1} times left".format(customer, index))
    index -= 1
    if index == 0:
        print("coffee has been thrown away")



#
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

# students name to length
students = ["Iron man", "Thor", "I am groot"]
students = [len(name) for name in students]
print(students)