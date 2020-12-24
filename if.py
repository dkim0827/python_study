weather = input("what is todays weather?") # save input as string
if weather == "rain" or weather == "snow":
    print("take umbrella with you")
elif weather == "dust":
    print("dont forget your mask")
else:
    print("nothing to take")


# temperature
temp = int(input("how hot today?")) # change string into int
if 30 <= temp:
    print("too hot dont go out")
elif 10 <= temp and temp < 30:
    print("pretty good weather")
elif 0 <= temp < 10:
    print("dont forget to take ur coat")
else:
    print("too cold dont go out")