from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time
import pr_pcapgen as prgen
import os
import csv
from collections import Counter
import config_benchmark

verbose = True

acceptable_values = config_benchmark.acceptable_values

max_returns = 3


def creader():
    return creadallrowsthencount()

def creadallrowsthencount():
    t1 = time.time()
    rows = session.execute("select * from probes;")
    t2 = time.time()
    numrows = 0
    for r in rows:
        numrows = numrows + 1
    return (t1, t2, numrows)


try:
   cluster = Cluster(['192.168.1.106','192.168.1.105'])
   session = cluster.connect()
   session.execute("USE test0")
except:
   print "Can't instantiate the cluster.  Cassandra is probably not running..."

tlist=[]

filename = 'output_reader.csv'

open(filename, 'w').close()

with open(filename,'a') as csvfile:
    owriter = csv.writer(csvfile,delimiter = ',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
    owriter.writerow('beforeread,afterread,datacount')

limit_counter = Counter() #limit to n

for i in range(1,3000):
    time.sleep(0)
    try:
        c = creader()
        if verbose:
            print c, i
        try:
            limit_counter[c[2]] += 1
            if (c[2] in acceptable_values) and limit_counter[c[2]]<max_returns:
                with open(filename,'a') as csvfile:
                    owriter = csv.writer(csvfile,delimiter = ',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
                    owriter.writerow(c)
        except:
            print "couldn't write to file"
    except:
        print "An error occurred while trying to read."


print limit_counter