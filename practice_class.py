class Unit:
    def __init__(self):
        print("Unit create")

class Flyable:
    def __init__(self):
        print("Flyable create")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() super only connect 1 super. when you connect more than 1 need to type each one
        Unit.__init__(self)
        Flyable.__init__(self)

# dropship
dropship = FlyableUnit()