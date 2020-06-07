
# Simulation of Jordan Henderson's analogy of natural classification
#

import random
from collections import Counter
from time import time


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
    """Coin toss object"""
    coin = ["H", "T"]    
    freq = {"H":0, "T":0}
    
    def __init__(self):
        self.freq = {hort:0 for hort in self.coin}
                        
    def toss(self):
        self.value =  random.choice(self.coin)
        self.freq[self.value] += 1
        return self.value

    def hort(self):
        return self.value   
    
    def won(self, guess):
        return self.value == guess



class Person:
    """People with 100Rs till they trade"""

    savings = 0
    trades = 0
    wins = 0
    losses = 0

    def __init__(self):
        self.savings = 100
        
    def trade(self, coin,guess,partner):
        """Trade with another partner, win - +1 rs, loss -1rs."""

        coin.toss()
        if coin.won(guess) :
            self.savings += 1
            self.wins += 1
            partner.savings -= 1
        else :
            self.savings -= 1
            partner.savings +=1
            self.losses += 1
        self.trades += 1
        
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

    def winlossStats():
        wins = [ person.wins for person in people]
        print max(wins), min(wins), stat().mean(wins), stat().stddev(wins)
        print wins, sum(wins) 
        print
        losses = [ person.losses for person in people]
        print losses, sum(losses)
        print float(sum(wins))/ sum(losses) 

    def verifyTrades():
        trades = [ person.trades for person in people]
        print trades, sum(trades)

    #winlossStats()
    #verifyTrades()

    savingsList = [p.savings for p in people]
    return savingsList


def freqDist(list):
    
    #freq = Counter(list)
    freq = {p:list.count(p) for p in set(list)}
    values = [money for money,frequency in freq.items() ]

    def histogram(freq):
        keys = freq.keys()
        keys.sort() 

        for  k in keys:
            print k,freq[k]*'*', freq[k]

    histogram(freq) 
    return dict(zip(["mean", "stddev", "min", "max"], \
            [stat().mean(values), stat().stddev(values),min(values),max(values)]))
        
if __name__ == "__main__":

    # #people, #trades
    data = [(100,10), (100,100), (100,1000), (100,10000), ]
    data = [(100,10)]

    for val in data:
        start_time = time()
        print freqDist(startTrade(val[0],val[1]))
        print("--- %s seconds ---" % (time() - start_time))

    exit()
