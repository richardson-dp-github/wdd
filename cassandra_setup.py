from cassandra.cluster import Cluster


cluster = Cluster(['192.168.1.106','192.168.1.105'])

session = cluster.connect()

# session.execute("CREATE KEYSPACE test0 WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 2}")

session.execute("USE test0")

session.execute("CREATE TABLE probes("
                "prb_id uuid primary key,"
                "prb_time text,"
                "prb_addr1 text,"
                "prb_ssid text);")





