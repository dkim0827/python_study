# input

# dir : show what is included in dir
print(dir())

import random 
print(dir())
import pickle
print(dir())

print(dir(random))
lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

import glob # search everyfile in that folder
print(glob.glob("*.py"))

import os # can do things that provide from operating system
print(os.getcwd()) # current directory

folder = "sample_dir"

if os.path.exists(folder):
    print("Folder already exists")
    os.rmdir(folder)
    print(folder, "deleted folder")
else:
    os.makedirs(folder) # create folder
    print(folder, "Folder has been created")


print(os.listdir())

# time related functions
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("Todays date is ", datetime.date.today())

# timedelta : tells date difference btw 2 days
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("Today is our 100th day", today + td)