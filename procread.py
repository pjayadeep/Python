from time import sleep

def readProc(file) :
        return getData()

def getFd(file) :
        fd =  open(file,'rb')
        return fd

def schedCollection(interval, count):

        prev = getData(interval)
        for c in range(0,count):
                sleep(interval)
                next = getData(interval)
                diff = calcDiff(prev, next)
                printDiff(diff)
                prev = next


def getData(interval, type = 'cpu'):
        item = {}
        fd = getFd('/proc/stat')
        for line in fd:
                fields = line.split()
                if fields[0].startswith(type):
                	item[fields[0]] =[int(i)/interval for i in fields[1:] ]
        return item

def calcDiff(prev,next):
        diff = prev
        for firstCol in prev:
                i = 0;
                for value in  next[firstCol]:
                        delta = value - prev[firstCol][i]
                        diff[firstCol][i] = delta
                        i = i+1
        return diff

def printDiff(it):
	colNames = ['cpu', 'usr', 'nice', 'sys', 'idle', 'iowait', 'irq', 'softirq', 'steal' ,'guest', '???']
	for each in colNames:
		print each.rjust(6),
	print 

        for item  in  it:
                print item.rjust(6) ,
		for col in it[item]:
			print repr(col).rjust(6),
		print 



schedCollection(1,5)

