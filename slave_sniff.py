# Slave Sniff and Send -- Test

import wifiri_sysconfig
import scapyplist2xml
from scapy.all import *
# Added in order to receive data
import socket
import sys, errno
import time

samplePeriod = wifiri_sysconfig.initialPeriodInSeconds

# Self
host = wifiri_sysconfig.slaveIPAddress
port = wifiri_sysconfig.slavePort

# Connect to the Central Server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
centralServerHost = wifiri_sysconfig.centralServerIPAddress
centralServerPort = wifiri_sysconfig.centralServerPort
s.connect((centralServerHost, centralServerPort))

def handle_packet(packet):
    sendp(packet)

for i in range(1,5):
    try:
        print 'starting sniff # '+str(i)+'...'
        x = sniff(offline=wifiri_sysconfig.sampleFile, count=15)
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