# Slave Sniff and Send -- Test

import config
import scapyplist2xml
from scapy.all import *
# Added in order to receive data
import socket
import sys, errno
import time

samplePeriod = config.initialPeriodInSeconds

# Self
host = config.slaveIPAddress
port = config.slavePort

# Connect to the Central Server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
centralServerHost = config.centralServerIPAddress
centralServerPort = config.centralServerPort
s.connect((centralServerHost, centralServerPort))

def handle_packet(packet):
    sendp(packet)

for i in range(1,5):
    try:
        print 'starting sniff # '+str(i)+'...'
        x = sniff(offline=config.sampleFile, count=15)
        print 'converting to XML...'
        try:
            filename = 'output_msg'+str(i)+'.xml'
            scapyplist2xml.scapyplist2xml(x, filename)
            print filename + ' saved.'
        except:
            print "unable to convert to XML"
        f = 'output.xml'
        print 'sending message '+str(i)
        try:
            s.send('message '+str(i)+'\n')
        except IOError as e:
            if e.errno == errno.EPIPE:
                print "Error Sending Message ID "+str(i)
    except:
        print "Error in Sniff and Forward Operation"