from time import sleep

def readProc(file) :
        return getData()

def getFd(file) :
        fd =  open(file,'rb')
        return fd

def schedCollection(interval, count, collection, printF):
        prev = collection(interval)
        for c in range(0,count):
                sleep(interval)
                next = collection(interval)
                diff = calcDiff(prev, next)
                printF(diff)
                prev = next


def cpuData(interval, type = 'cpu'):
        item = {}
        fd = getFd('/proc/stat')
        for line in fd:
                fields = line.split()
                if fields[0].startswith(type):
               		item[fields[0]] =[int(i)/interval for i in fields[1:] ]
        return item


def diskData(interval, type = ''):
        item = {}
        fd = getFd('/proc/diskstats')
        for line in fd:
                fields = line.split()
                if fields[2].startswith(type):
               		item[fields[2]] =[int(i)/interval for i in fields[3:] ]
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

def printCpu(it):
	colNames = ['cpu', 'usr', 'nice', 'sys', 'idle', 'iowait', 'irq', 'softirq', 'steal' ,'guest', '???']
	printDiff(it,colNames)

def printDisk(it):
	colNames = ['Device', 'rrqm/s' ,  'wrqm/s',     'r/s',     'w/s',   'rsec/s',   'wsec/s', 'avgrq-sz', 'avgqu-sz',  'await',  'svctm',  '%util' ]
	printDiff(it,colNames)

def printDiff(it,colNames):
	for each in colNames:
		print each.rjust(6),
	print 

        for item  in  it:
                print item.rjust(6) ,
		for col in it[item]:
			print repr(col).rjust(6),
		print 


schedCollection(1,1,cpuData,printCpu)
schedCollection(1,1,diskData,printDisk)

