"""
make lms system for real estate

3 different house
1. downtown apt buy 10m 2010
2. burnaby townhouse lease 5m 2007
3. newwest house monthly 500/50 2000

"""

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            ,self.price, self.completion_year)

houses = []
house1 = House("downtown", "apt", "buy", "10m", "2010")
house2 = House("burnaby", "townhouse", "lease", "5m", "2007")
house3 = House("newwest", "house", "montly", "500/50", "2000")
houses.append(house1)
houses.append(house2)
houses.append(house3)
print("Total {0} Houses are in the list".format(len(houses)))

for house in houses:
    house.show_detail()