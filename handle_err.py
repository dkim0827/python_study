try:
    print("calculator for divison") 
    num1 = int(input("first number :"))
    num2 = int(input("second number :"))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("Error! Wrong Value")

except ZeroDivisionError as err:
    print(err)

except Exception as err:
    print("Unknown error has been occured")
finally:
    print("Thank you for using")