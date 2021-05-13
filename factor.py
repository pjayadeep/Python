
from  math import ceil,sqrt

domain=1971

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
        factors_list =  [(x,y) for (x,y) in factors(m) if x+y<domain]
        if len(factors_list) == 1:
            return True
    return False

def nonUniq(nos):
    l = []
    for i in nos:
        if not fact_sums(i):
            l.append(i)
    return l

def find_xy(nU):
    answers = []
    for n in  nU:
        freq_list = []
        freq = {}
        freq[1] = 0

        for (a,b) in sums(n):
            i = a*b
            adds =  [x+y for (x,y) in factors(i)]
            lst =  ([(x,y) for (x,y) in factors(i) if x+y in nU] )
            #print lst
            freq_list.append((len(lst), (a,b)))

        for f,item in freq_list:
            if f == 1:
                freq[1] += 1
                ans = item
        if freq[1] == 1:
            print 'Answer =', ans
            answers.append(ans)
        #print
    return answers
            

nU =  nonUniq(range(5,domain))
print "potential sums = ", nU
print find_xy(nU)
