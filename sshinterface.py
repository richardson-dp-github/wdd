import os

remotehosts = []
remotehosts.append("192.168.1.105")
remotehosts.append("192.168.1.107")


def findrphosts():
    # somehow mine the results of an nmap scan if ssh port is open
    x = []
    remotehosts = []
    remotehosts.append("192.168.1.105")
    remotehosts.append("192.168.1.107")
    return "192.168.1.105"

def findcassandrafolder():
    return '~/cassandra/apache-cassandra-3.0.8/bin'


def sshintohost(ipaddress):
    sshcommand = "ssh " + ipaddress
    os.system(sshcommand)

#For me, Cassandra's path is ~/Documents/thesis/apache-cassandra-3.7/bin/
def startcassandra(cassandraspath="~/Documents/thesis/apache-cassandra-3.7/bin/"):
    cmd = "cd " + cassandraspath
    os.system(cmd)
    print "Executing Command" + cmd
    os.system("./cassandra")

'''
for host in remotehosts:
    host.startcassandra()
'''