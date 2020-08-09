# verify the runs of conitoss in 250 tosses

import random


class Coin:
    """Coin toss object"""
    coin = ["H", "T"]    
    freq = {"H":0, "T":0}
    hist=[]
    
    def __init__(self):
        self.freq = {hort:0 for hort in self.coin}
                        
    def toss(self):
        self.value =  random.choice(self.coin)
        self.freq[self.value] += 1
        self.hist += self.value
        return self.value

    def hort(self):
        return self.value   
    
    def won(self, guess):
        return self.value == guess


def runSample(count):

    coin = Coin()

    runs = []
    runcount = 1
    previous = coin.toss()

    for i in range(count - 1):
        result = coin.toss()
        if result == previous:
            runcount += 1
        else:
            runs.append(runcount)
            runcount = 1
        previous = result

    runs.append(runcount)

    #print coin.hist
    return  max(runs)

def histogram(freq):
    keys = freq.keys()
    keys.sort() 
    for  k in keys:
        if freq[k] > 0:
            print( k,freq[k]*'*', freq[k])

tossCount = 250

def runIteration(iterCount):
    stats = { }
    for x in range(iterCount):
        stats[x] = 0
    for i in range(iterCount):
        stats[runSample(tossCount)] += 1

    #print [ (x,stats[x]) for x in stats if  stats[x] > 0]
    #histogram(stats)
    print sum ([ (x*stats[x]) for x in stats if  stats[x] > 0]) *1.0  /iterCount
    

runIteration(1000)

#print runSample(1)
