# Simulation of Jordan Henderson's analogy of natural classification
#

import random
from collections import Counter

# statistics code from stackoverflow
#
class stat :

    def mean(self, data):
        """Return the sample arithmetic mean of data."""
        n = len(data)
        if n < 1:
            raise ValueError('mean requires at least one data point')
        return sum(data)/float(n)

    def _ss(self,data):
        """Return sum of square deviations of sequence data."""
        c = self.mean(data)
        ss = sum((x-c)**2 for x in data)
        return ss

    def stddev(self, data, ddof=0):
        """Calculates the population standard deviation
        by default; specify ddof=1 to compute the sample
        standard deviation."""
        n = len(data)
        if n < 2:
            raise ValueError('variance requires at least two data points')
        ss = self._ss(data)
        pvar = ss/(n-ddof)
        return pvar**0.5

#####

class Coin:
    coin = ["H", "T"]    
    freq = {"H":0, "T":0}
    
    def __init__(self):
        self.freq = {hort:0 for hort in self.coin}
                        
    def toss(self):
        self.value =  random.choice(self.coin)
        #self.value = "T"
        self.freq[self.value] = self.freq[self.value]+1
        return self.value

    def hort(self):
        return self.value   
    
    def won(self, guess):
        return self.value == guess



class Person:
    savings = 0
    def __init__(self):
        self.savings = 100
        
    def trade(self, coin,guess,partner):
        coin.toss()
        if coin.won(guess) :
            self.savings = self.savings + 1
            partner.savings = partner.savings -1
        else :
            self.savings = self.savings -1
            partner.savings = partner.savings + 1
    def balance(self):
        return self.savings
    

def startTrade(peopleCount, tradeCount):
    coin = Coin()

    print peopleCount,'people',  tradeCount*peopleCount,'trades' 
    print

    people = [Person() for i in range(peopleCount)]

    for count  in range(tradeCount):
        for eachPerson in people:
            while True:
                partner = random.choice(people)
                if partner != eachPerson:
                    break

            guess = coin.toss()
            eachPerson.trade(coin,guess,partner)
    return people


def freqDist(people):
    
    savingsList = [p.savings for p in people]

    freq = Counter(savingsList)
    freq = {p:savingsList.count(p) for p in set(savingsList)}
    values = [money for money,frequency in freq.items() ]

    #print histogram
    def histogram(freq):
        for k,v in freq.items():
            print k,v*'*', v

    #histogram(freq) 
    return dict(zip(["mean", "stddev", "min", "max"], \
            [stat().mean(values), stat().stddev(values),min(values),max(values)]))
        
if __name__ == "__main__":

    print freqDist(startTrade(50,1000))
    exit()

    print freqDist(startTrade(100,10))
    print freqDist(startTrade(100,100))
    
    print freqDist(startTrade(100,200))
    print freqDist(startTrade(100,300))
