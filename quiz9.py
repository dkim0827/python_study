chicken = 10
waiting = 1

class SoldOutError(Exception):
    pass

while(True):
    try:
        print(f"Quantity of Chicken : {chicken}")
        order = int(input("How many chicken do you want to order? : "))
        if order > chicken:
            print("Not enough chicken sorry")
        elif order <= 0:
            raise ValueError
        else:
            print(f"Waiting Number : {waiting} | Ordered : {order}")
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("Wrong Input Sorry")
    except SoldOutError:
         print("All chickens are sold. We don't take more orders sorry")
         break