import random
die = range(1,7)
die2 = range(1,7)
toss = random.choice(die)
#print toss

result = [ (first,second,third) for first in die for second in die 
         for third in die 
            if toss in (first,second,third) ]

result = [ (first,second) for first in die for second in die 
            if toss in (first,second) ]

print len(result), len(die)**3
prob = float(len(result))/len(die)**3
print prob
print toss, result

