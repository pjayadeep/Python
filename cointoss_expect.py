# verify the runs of conitoss in 250 tosses

import random


class Coin:
    """Coin toss object"""
    coin = ["H", "T"]    
    freq = {"H":0, "T":0}
    hist=[]
    
    def __init__(self):
        self.freq = {hort:0 for hort in self.coin}
        self.hist=[]
                        
    def toss(self):
        self.value =  random.choice(self.coin)
        self.freq[self.value] += 1
        self.hist += self.value
        return self.value

    def hort(self):
        return self.value   
    
    def won(self, guess):
        return self.value == guess

def runSample(coin, count):

    runcount = maxcount = 1
    previous = coin.toss()

    for i in range(count - 1):
        result = coin.toss()
        if result == previous:
            runcount += 1
        else:
            runcount = 1
        if runcount > maxcount:
            maxcount = runcount
        previous = result
    return  maxcount

def histogram(freq):
    keys = freq.keys()
    keys.sort() 
    for  k in keys:
        if freq[k] > 0:
            print( k,freq[k]*'*', freq[k])

def runIteration(iterCount,tossCount):
    stats = {x:0 for x in xrange(iterCount)}
    for i in xrange(iterCount):
        stats[runSample(Coin(), tossCount)] += 1
    #histogram(stats)
    print sum ([ (x*stats[x]) for x in stats if  stats[x] > 0]) *1.0  /iterCount
    

runIteration(1000, 250)

exit()
runIteration(10, 4)
print runSample(Coin(), 1)
print runSample(Coin(), 2)
print runSample(Coin(), 10)
