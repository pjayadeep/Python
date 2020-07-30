
import random

# The door hides a car or goat.
class door:
    def __init__(self, value) :
        self.has = value

    def reveal(self):
        return self.has

car = door("car")
goatB = door("goatA")
goatC = door("goatB")

def pickAdoor(doors):
    return random.choice(doors)

def play(changeChoice=0):

    doors = [car, goatB, goatC]
    selection  = pickAdoor(doors)
    goatDoor = showDoor(selection)

    if changeChoice:
        doors.remove(goatDoor)
        doors.remove(selection)
        selection =  doors[0]

    return selection

# Monty Hall logic
#
def showDoor(selection ):

    if selection == car: #correct choice
        return  random.choice([goatB, goatC])
    elif  selection == goatB:
        return  goatC
    else :
        return goatB

def montyHall(changeChoice=0):
    winloss = {"win":0, "loss":0}
    for i in range(1000):
        if  play(changeChoice).reveal() == "car" :
            winloss["win"] = winloss["win"] + 1
        else:
            winloss["loss"] = winloss["loss"] + 1
    return winloss

print
print 'No Switch ', montyHall(0)
print 'With Switch', montyHall(1)

