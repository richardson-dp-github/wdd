# PROTOTYPE IN DEVELOPMENT

# This file, and this function, will, upon being given a scapy packet list,
#  will convert that packet list to XML, using various parameters of interest for this particular
#  application

# At this time, this application is only interested in
# If Probe Request - Print time of request, MAC of requestor, SSID of request
#     Dot11ProbeReq
# If Association Request - Print time of request, MAC of requestor, SSID of request
# If Probe Response - Print time of response, MAC of responder, SSID
#     Dot11ProbeResp

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *





def scapyplist2xml(p):
    for i in p:
        for j in PacketsOfInterest:
            if i.haslayer(j):
                print "This is a packet of interest"
            else:
                print "No Packets of Interest"


def SniffExistingFile(f):
    return sniff(offline=f);



# -------------------------------------
# START Global Variables (for now)
# -------------------------------------

PacketsOfInterest = []

PacketsOfInterest.append(Dot11ProbeReq)
PacketsOfInterest.append(Dot11ProbeResp)

print PacketsOfInterest


# -------------------------------------
# END Global Variables (for now)
# -------------------------------------




# -------------------------------------
# Test out the function here
# -------------------------------------

y = SniffExistingFile('capture1-05.cap')

scapyplist2xml(y)





# --------------------------------------