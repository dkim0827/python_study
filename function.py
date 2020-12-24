def open_account():
    print("New account has been created.")

def deposit(balance, money):
    print("transaction approved. your balance is {0}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("transaction has been approved. balance is {0}".format(balance - money))
        return balance - money
    else:
        print("declined. balance is {0}".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("commission is {0}, balance is {1}".format(commission, balance))


# how to set default value
def profile(name, age=17, main_lang="python"):
    print("name : {0}\tage : {1}\tmain language : {2}".format(name, age, main_lang))

profile("yoo", 24, "python")
profile("kim")

# keyword value
def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(name="yoo", main_lang="python", age=25)


def profile3(name, age, *language):
    print("name : {0}\tage : {1}\t".format(name, age), end=" ") # end with empty space makes next line in the same line
    for lang in language:
        print(lang, end=" ")
    print()

profile3("yoo", 20, "python", "c#", "c", "c+", "c++")
profile3("kim", 20, "python", "", "", "", "")


gun = 10

def checkpoint(soldiers):
    global gun # bring global gun
    gun = gun - soldiers
    print("gun quantity : {0}".format(gun))

# easier to maintain the code
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("gun quantity : {0}".format(gun))
    return gun



print("total gun : {0}".format(gun))
checkpoint(2)
print("gun quantity : {0}".format(gun))
