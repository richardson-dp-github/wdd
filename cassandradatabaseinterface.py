from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time

cluster = Cluster(['192.168.1.106','192.168.1.105'])

session = cluster.connect()

# session.execute("CREATE KEYSPACE tutorialspoint WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 2}")

session.execute("USE test0")

def creader():
    t1 = time.time()
    rows = session.execute("select * from probes;")
    t2 = time.time()
    for r in rows:
        print r
    return t2-t1


def cwriter(plist):
    for p in plist:
        session.execute('insert into probes (prb_id, prb_time, prb_addr1, prb_ssid) values (%s, %s, %s, %s);',(uuid.uuid1(), str(p.time), p.addr2, p.info))


cwriter(sniff(offline='test1.pcap'))
print creader()




