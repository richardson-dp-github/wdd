# import cassandradatabaseinterface

from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time
import pr_pcapgen as prgen
import os

# session.execute("CREATE KEYSPACE tutorialspoint WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 2}")
'''
#For me, Cassandra's path is ~/Documents/thesis/apache-cassandra-3.7/bin/
def startcassandra(cassandraspath="~/Documents/thesis/apache-cassandra-3.7/bin/"):
    cmd = "cd " + cassandraspath
    os.system(cmd)
    print "Executing Command" + cmd
    os.system("./cassandra")
'''
# Assume Cassandra is already started, manual or otherwise

def ccleartable():
    session.execute("truncate probes;")

def cwriter(plist):
    for p in plist:
        session.execute('insert into probes (prb_id, prb_time, prb_addr1, prb_ssid) values (%s, %s, %s, %s);',(uuid.uuid1(), str(p.time), p.addr2, p.info))

def startwriting(timeconstant):
    try:
        tlist = []
        for i in range(1,100,10):
            print "running iteration " + str(i)
            try:
                s = prgen.ScenarioGen1(i)
                s.run_probes()
                s.save_file()
            except:
                print "Not able to generate the scenario."
            try:
                cwriter(sniff(offline='test1.pcap'))
            except:
                print "program was not able to write the data from the file"
            #wait for the time constant, this will give the reader some time to catch up just in case
            time.sleep(timeconstant)
            try:
                ccleartable()
            except:
                print "initial attempt failed to clear the table...trying one more time..."
                time.sleep(timeconstant)
                try:
                    ccleartable()
                except:
                    print "tried twice...not able to clear the data in the table"
        # print str(tlist)
    except:
        print "Can't write to the database from the pcap file.  Cassandra is probably not running..."

try:
    cluster = Cluster(['192.168.1.106','192.168.1.105'])
    session = cluster.connect()
    session.execute("USE test0")
except:
    print "Can't instantiate the cluster.  Cassandra is probably not running..."

try:
    startwriting(timeconstant=1)
except:
    print "Oh no!  Something must be wrong."
    print e
