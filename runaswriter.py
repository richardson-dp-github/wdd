# import cassandradatabaseinterface

from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time
import pr_pcapgen as prgen
import os
import ntplib
import csv
import config_benchmark as cfg

verbose = cfg.verbose

timeconstant = 5

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

def creadallrowsthencount():
    t1 = time.time()
    rows = session.execute("select * from probes;")
    t2 = time.time()
    numrows = 0
    for r in rows:
        numrows = numrows + 1
    return (t1, t2, numrows)

def startwriting(timeconstant):
    try:
        try:
            if verbose:
                print "doing the initial"
            ccleartable()
            print "Reading all Rows..." + str(creadallrowsthencount())
        except:
            print "try to do the initial clear again"
            time.sleep(5)
            ccleartable()


        tlist = []
        for i in range(0,1000,100):
            print "running iteration " + str(i) + " at " + str(time.time())
            try:
                s = prgen.ScenarioGen1(i)
                s.run_probes()
                s.save_file()
            except:
                print "Not able to generate the scenario."
            try:
                time0 = time.time()
                cwriter(sniff(offline='test1.pcap'))
                time1 = time.time()
                try:
                    with open('output_writer.csv','a') as csvfile:
                        owriter = csv.writer(csvfile,delimiter = ',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
                        owriter.writerow([time0] + [time1] + [i])
                except:
                    print "couldn't write to the main file"
            except:
                print "couldn't write to database"

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
            time.sleep(timeconstant)
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
    os.system("ping -c 4 192.168.1.105")
    os.system("ping -c 4 192.168.1.106")
    os.system("ping -c 4 192.168.1.107")

    c=ntplib.NTPClient()
    response0 = c.request('192.168.1.105',version=3)
    response1 = c.request('192.168.1.106',version=3)
    response2 = c.request('192.168.1.107',version=3)
    print response0.offset
    print response1.offset
    print response2.offset
except:
    print "Couldn't run the pings"

try:
    open('output_writer.csv', 'w').close()
    with open('output_writer.csv','a') as csvfile:
        owriter = csv.writer(csvfile,delimiter = ',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        owriter.writerow(['timebeforewrite'] + ['timeafterwrite'] + ['datacount'])
    startwriting(timeconstant=timeconstant)
except:
    print "Oh no!  Something must be wrong."
    print e



