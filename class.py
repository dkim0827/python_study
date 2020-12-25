# # marine
# name = "marine" # name of unit
# hp = 40 # health of unit
# damage = 5 # dmg of unit

# print("{} unit has been created".format(name))
# print("health is {0}, damage is {1}\n".format(hp, damage))

# # tank
# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35
# print("{} unit has been created".format(tank_name))
# print("health is {0}, damage is {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : attacking {1} direction. [damage {2}]".format(name, location, damage))

# attack(name, "1", damage)

from random import *

# Regular Unit
class Unit:
    def __init__(self, name, hp, speed): # constructor
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit has been created".format(name))

    def move(self, location):
        print("{0} : moves to {1} direction.[speed {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : took {1} damage".format(self.name, damage))
        self.hp -= damage
        print("{0} : remaining hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : unit has been destroyed".format(self.name))

# Attack Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # constructor
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : attacking to {1} direction. [damage {2}]"\
            .format(self.name, location, self.damage))
    
# Marine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5) # name, hp, speed, damage

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Using stimpack.[HP {1} left]".format(self.name, self.hp))
        else:
            print("{0} : HP is not enough to use stimpack[HP {0} left]".format(self.name, self.hp))

# Tank
class Tank(AttackUnit):
    seize_developed = False # is seize mode developed?

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35) # name, hp, speed, damage
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # if not seize mode
        if self.seize_mode == False:
            print("{0} : turn into seize mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : turn off seize mode".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# class who can fly
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : flying to {1} direction[speed : {2}]"\
            .format(name, location, self.flying_speed))
    
# how to receive from 2 diff class
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # ground speed is 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : disabled clocking mode".format(self.name))
            self.clocked = False
        else:
            print("{0} : enabled clocking mode".format(self.name))
            self.clocked = True

# method override  = how to use method in c hild class in the parent class

# # building
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# # supply depot
# supply_depot = BuildingUnit("supply depot", 500, "7olock")

def game_start():
    print("[notice]Starting new game")

def game_over():
    print("Player : GG")
    print("[Player] left the game")
    # pass # pretend code is done


# pretend game
game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# to control efficiently
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# move every units
for unit in attack_units:
    unit.move("1oclock")

# develop seize mode
Tank.seize_developed = True
print("[Notice]Tank seize mode developed")

# Prepare Attack
for unit in attack_units:
    if isinstance(unit, Marine): #if current unit is Marine
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# Attack
for unit in attack_units:
    unit.attack("1oclock")

# got damage
for unit in attack_units:
    unit.damaged(randint(5, 21)) # received damage btw 5 ~ 20

# end game
game_over()
