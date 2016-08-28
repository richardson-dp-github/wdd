from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time
import pr_pcapgen as prgen
import os

# session.execute("CREATE KEYSPACE tutorialspoint WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 2}")

#For me, Cassandra's path is ~/Documents/thesis/apache-cassandra-3.7/bin/
def startcassandra(cassandraspath="~/Documents/thesis/apache-cassandra-3.7/bin/"):
    cmd = "cd " + cassandraspath
    os.system(cmd)
    print "Executing Command" + cmd
    os.system("./cassandra")


def creader(session):
    t1 = time.time()
    rows = session.execute("select * from probes;")
    t2 = time.time()
    for r in rows:
        print r
    return t2-t1

def ccleartable(session):
    session.execute("delete from probes where 1;")

def cwriter(plist, session):
    for p in plist:
        session.execute('insert into probes (prb_id, prb_time, prb_addr1, prb_ssid) values (%s, %s, %s, %s);',(uuid.uuid1(), str(p.time), p.addr2, p.info))

'''
try:
   startcassandra()
except:
   print "can't start cassandra"
   print e

try:
   cluster = Cluster(['192.168.1.106','192.168.1.105'])
   session = cluster.connect()
   session.execute("USE test0")
except:
   print "Can't instantiate the cluster.  Cassandra is probably not running..."


try:
    tlist = []
    for i in range(0,100,10):
        s = prgen.ScenarioGen1(i)
        s.run_probes()
        s.save_file()
        cwriter(sniff(offline='test1.pcap'))
        tlist.append(creader())
    print str(tlist)
except:
    print "Can't write to the database from the pcap file.  Cassandra is probably not running..."
'''


