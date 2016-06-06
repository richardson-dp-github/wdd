# Slave Sniff and Send -- Test

import wifiri_sysconfig
import scapyplist2xml
from scapy.all import *
# Added in order to receive data
import socket
import sys, errno
import time
import wifipiemail

# samplePeriod = wifiri_sysconfig.initialPeriodInSeconds

# Definitions
# host = wifiri_sysconfig.slaveIPAddress
# port = wifiri_sysconfig.slavePort
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# centralServerHost = ''
# centralServerPort = ''

# Connect to the Central Server
def connectToTheCentralServer():

    centralServerHost = wifiri_sysconfig.centralServerIPAddress
    centralServerPort = wifiri_sysconfig.centralServerPort
    s.connect((centralServerHost, centralServerPort))

def handle_packet(packet):
    sendp(packet)


def testSniff():
    for i in range(1, 5):
        try:
            print '============================='
            print '\/ \/ \/ \/ \/ \/ \/ \/ \/ \/'
            print 'starting sniff # '+str(i)+'...'
            x = sniff(offline=wifiri_sysconfig.sampleFile, count=30)
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
                # data = 'message '+str(i)+'\n'
                with open (f, 'r') as myfile:
                    data = myfile.read()


                #Send data
                # s.connect((centralServerHost, centralServerPort))
                s.sendall(data)

                #Receive Data From the Server
                received = s.recv(1024)



            except IOError as e:
                if e.errno == errno.EPIPE:
                    print "Error Sending Message ID "+str(i)
                else:
                    print "Unable to send message "+str(i)+" for unknown reason"
                received = 'Nothing received--ERROR!!!'
            # finally:
                # s.close()

            print "Sent:     {}".format(data)
            print "Received: {}".format(received)

            print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
            print '============================='
        except:
            print "Error in Sniff and Forward Operation"

def concludeConnection():
    s.close()

SSID_list = []
SSID_list.append('2WIRE024')

def PacketHandler(pkt):

  typeManagementFrame = 0
  subtypeAssociationRequest = 0
  subtypeProbeRequest = 4
  subtypeProbeResponse = 5

  if pkt.haslayer(Dot11):
    if (pkt.type == typeManagementFrame and (pkt.subtype in [subtypeAssociationRequest, subtypeProbeRequest])):
      if pkt.info in SSID_list:
        print "AP MAC: %s with SSID: %s [%s %s]" %(pkt.addr1, pkt.info, pkt.type, pkt.subtype)
        # wifipiemail.send_message('2wire024 detected: ' + pkt.addr1 + '|' + pkt.addr2 + '|' + pkt.info)
        print 'SSID of interest detected: ' + pkt.addr1 + '->' + pkt.addr2 + '|' + pkt.info


# sniff(prn = PacketHandler, offline='capture1-05.cap')

sniff(prn = PacketHandler)


# Adapted from https://gist.github.com/securitytube/5291959