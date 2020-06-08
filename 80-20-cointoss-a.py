
# Simulation of Jordan Henderson's analogy of natural classification
#
#Probllem:
#
#   Let us say the the probability of a head or tail during a coin toss is 
# equal (50 percent). 
#
# Let us also start a game in which every one has 100 rupees. If they all 
# trade with each other for a long time based on coin toss (1 rupee gain 
# for  head and 1 rupee loss for tail), will some people end up richer ? 
# Will some people end up with nothing ? Or will they end up with somewhat 
# equally (!around where they started ).
    
# This was a debate between Ravichandran and Dr Vishwanathan. Dr Vishwanathan
# apparently checked with a mathematics professor, who said that at the
# end of the trials, everyone will have the same amount of money, which is NOT
# correct. Though the distribution appears equal due to the 50% probabilty of
# head/tails, the distribution is in fact normal one.
# (see https://www.youtube.com/watch?v=zwpnmMCpKyU)
#
# There are 2 random variables involved, one that of coin toss whose probaility
# is 50%, and another of each person making at least half the right 
# calls out of it to get a 50% win/lose chance, which is (nC(n/2) / 2^n) 
# which drops # quite fast with large n. This causes a standard 
# distribution of wealth among the people.

# This is not so apparent from the way the quesiton is posed making people
# believe the chances of each individual winning/losing is 50%.
#
# But RC's argument of an 80/20 distribution is not correct either, it is
# just a normal distribution.

# Authorj - Jayadeep Purshothaman p_jayadeep@yahoo.com

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
    

def getPartner(people, eachPerson):
    while True:
        partner = random.choice(people)
        if partner.savings <= 0:
            continue
        if partner != eachPerson:
            break
    return partner

def trade(people):
    coin = Coin()
    for eachPerson in people:
        if  eachPerson.savings > 0:
            partner = getPartner(people,eachPerson)
            guess = coin.toss()
            eachPerson.trade(coin,guess,partner)


def startTrade(peopleCount, tradeCount):

    people = [Person() for i in range(peopleCount)]
    for count  in range(tradeCount):
        trade(people)
    #winlossStats(people)
    #verifyTrades(people)

    savingsList = [p.savings for p in people]
    #print savingsList

    return savingsList


def winlossStats(people):
    wins = [ person.wins for person in people]
    print( max(wins), min(wins), stat().mean(wins), stat().stddev(wins))
    print( wins, sum(wins) )
    print("")
    losses = [ person.losses for person in people]
    print( losses, sum(losses))
    print( float(sum(wins))/ sum(losses) )

def verifyTrades(people):
    trades = [ person.trades for person in people]
    print( trades, sum(trades))


def freqDist(list):
    
    #freq = Counter(list)
    freq = {p:list.count(p) for p in set(list)}
    values = [money for money,frequency in freq.items() ]

    def histogram(freq):
        keys = freq.keys()
        keys.sort() 
        for  k in keys:
            print( k,freq[k]*'*', freq[k])

    #histogram(freq) 
    return dict(zip(["mean", "stddev", "min", "max"], \
            [stat().mean(values), stat().stddev(values),min(values),max(values)]))
        
if __name__ == "__main__":

    # #people, #trades
    data = [(10,10), (10,100), (10,10000)]
    data = [(100,10), (100,100), (100,1000), (100,10000), ]

    for peopleCount, tradeCount in data:
        start_time = time()
        print  (peopleCount,'people',  tradeCount*peopleCount,'trades' )
        print (freqDist(startTrade(peopleCount,tradeCount)))
        print("--- %s seconds ---" % (time() - start_time))
        print("")

    exit()
