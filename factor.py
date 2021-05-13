
from  math import ceil,sqrt

def sums(n):
    #print "number=", n
    list = []
    for i in range(2, int(n/2)+1):
        list.append( (i,n-i))
    return list

def factors(n):
    #print "factors of", n
    list = []
    for i in range(2, int(ceil(sqrt(n))) ) :
            if n%i == 0:
                list.append((i,n/i))
    return list


def fact_sums(sum):
    list = sums(sum)
    #print list
    list = [x*y for (x,y) in list]
    #print list

    for  m in list:
        factors_list =  [(x,y) for (x,y) in factors(m) if x+y<101]
        if len(factors_list) == 1:
            #print factors_list
            #print [x+y for (x,y) in factors_list] # if x <=20 and y <= 20]
            return True

    return False

#for n in  [x*y for (x,y) in sums(57)]:
    #print factors(n)


l = []

def nonUniq(nos):
    for i in nos:
        if not fact_sums(i):
            l.append(i)
    return l

nU =  nonUniq(range(5,101))
print "potential sums = ", nU
setB = set(nU)
for n in  nU:
    freq_list = []
    #print sums(n)
    #for i in  [x*y for (x,y) in sums(n)]:
    freq = {}
    freq[1] = 0
    for (a,b) in sums(n):
        i = a*b
        #print factors(i)
        adds =  [x+y for (x,y) in factors(i)]
        #print(adds), '(', i, ')', factors(i)
        lst =  ([(x,y) for (x,y) in factors(i) if x+y in nU] )
        #print lst
        freq_list.append((len(lst), (a,b)))
    #print freq_list

    for f,item in freq_list:
        if f == 1:
            freq[1] += 1
            ans = item
    if freq[1] == 1:
        print 'Answer =', ans
        
