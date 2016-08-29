from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time
import pr_pcapgen as prgen
import os

def creader():
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

for i in range(1,100):
    time.sleep(0)
    try:
        print creader()
    except:
        print "An error occurred while trying to read."


