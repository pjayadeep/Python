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
            if runcount > maxcount:
                maxcount = runcount
            runcount = 1
        previous = result
        if runcount > maxcount:
            maxcount = runcount

    #print coin.hist
    return  maxcount

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
        stats[runSample(Coin(), tossCount)] += 1

    #print [ (x,stats[x]) for x in stats if  stats[x] > 0]
    #histogram(stats)

    print sum ([ (x*stats[x]) for x in stats if  stats[x] > 0]) *1.0  /iterCount
    

runIteration(10000)
exit()

print runSample(Coin(), 1)
print runSample(Coin(), 2)
print runSample(Coin(), 10)
