# Slave Sniff and Send -- Test

import test_config
import scapyplist2xml
from scapy.all import *
# Added in order to receive data
import socket
import sys, errno
import time

samplePeriod = test_config.initialPeriodInSeconds

# Self
host = test_config.slaveIPAddress
port = test_config.slavePort

# Connect to the Central Server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
centralServerHost = test_config.centralServerIPAddress
centralServerPort = test_config.centralServerPort
s.connect((centralServerHost, centralServerPort))

for i in range(1,5):
    try:
        print 'starting sniff # '+str(i)+'...'
        x = sniff(offline=test_config.sampleFile,count=5)
        print 'converting to XML...'
        scapyplist2xml.scapyplist2xml(x, 'output_msg'+str(i)+'.xml')
        f = 'output.xml'
        print 'sending message '+str(i)
        s.send('message '+str(i)+'\n')
    except IOError as e:
        if e.errno == errno.EPIPE:
            print "Error Sending Message ID "+str(i)




