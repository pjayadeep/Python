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

    if changeChoice:
        doorSelection = {car:random.choice([goatB, goatC]), goatC:goatB, goatB:goatC}
        goatDoor = doorSelection[selection]
        doors.remove(goatDoor)
        doors.remove(selection)
        selection =  doors[0]

    return selection


def montyHall(changeChoice=0):
    winloss = {"win":0, "loss":0}
    for i in range(1000):
        if  play(changeChoice).reveal() == "car" :
            winloss["win"] += 1
        else:
            winloss["loss"] += 1
    return winloss

print
print 'No Switch ', montyHall(0)
print 'With Switch', montyHall(1)

