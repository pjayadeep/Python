
import random

# The door hides a car or goat.
class door:
    def __init__(self, value) :
        self.has = value

    def reveal(self):
        return self.has

values = ["car","goat", "goat"]

#boxes = [door(v) for v in values]

carboxA = door("car")
goatB = door("goatA")
goatC = door("goatB")

doors = [carboxA, goatB, goatC]

def pickAbox(doors):
    return random.choice(doors)

def play(changeChoice=0):

    doors = [carboxA, goatB, goatC]
    selection  = pickAbox(doors)
    goatDoor = showDoor(selection)

    if changeChoice:
        doors.remove(goatDoor)
        doors.remove(selection)
        return doors[0]
    return selection

def showDoor(selection ):
    #print 'selection', selection.reveal()

    if selection == carboxA: #correct choice
        return  random.choice([goatB, goatC])
    elif  selection == goatB:
        return  goatC
    else :
        return goatB

def changeDoor(doors):
    return random.choice(doors)

stats =  {"car":0, "goatA":0, "goatB":0}
for i in range(1000):
    has = pickAbox(doors).reveal()
    stats[has] = stats[has] + 1


def montyHall(changeChoice=0):
    winloss = {"win":0, "loss":0}
    for i in range(100):
        if  play(changeChoice).reveal() == "car" :
            winloss["win"] = winloss["win"] + 1
        else:
            winloss["loss"] = winloss["loss"] + 1
    return winloss

print 'No Switch ', montyHall(0)
print 'Switch', montyHall(1)

