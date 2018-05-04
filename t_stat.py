import numpy as np
import sys

def sampleStdDev(lst):
        return np.std(lst,ddof=1)
def evalTStat(s1,s2):
        return (np.mean(s1)-np.mean(s2))/(np.sqrt((sampleStdDev(s1)**2/(len(s1)-1))+(sampleStdDev(s2)**2/(len(s2)-1))))
tcritical = sys.argv[1]
sample1 = [40,36,20,32,45,28]
sample2= [41,39,18,23,35]
tstatistic = evalTStat(sample1,sample2)
print "t-statistic for the 2 samples:",tstatistic
if(tstatistic>np.abs(float(tcritical))):
        print "Hence, reject NULL Hypothesis"
else:
        print "Hence, accept  NULL Hypothesis"
