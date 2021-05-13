
from  math import ceil,sqrt

def sums(n):
    print "number=", n
    list = []
    for i in range(2, int(n/2)+1):
        list.append( (i,n-i))
    print list
    return list

def factors(n):
    print n
    list = []
    for i in range(2, int(ceil(sqrt(n))) ) :
            if n%i == 0:
                list.append((i,n/i))
    return list



def fact_sums(sum):
    list = sums(sum)
    print list
    list = [x*y for (x,y) in list]
    print list
    print

    for  m in list:
        factors_list =  factors(m)
        print factors_list
        print [x+y for (x,y) in factors_list] # if x <=20 and y <= 20]

fact_sums(75)
#print factors(36)

sums = [11,17,23,27,29,24]
sums = [17]
