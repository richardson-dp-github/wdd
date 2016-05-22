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

import xml.etree.ElementTree as ET #for XML conversion
# from xml.etree.ElementTree import ElementTree


def scapyplist2xml(p, oFile):
    root = ET.Element("PacketList")
    for i in p:
        for j in PacketsOfInterest:
            if i.haslayer(j):
                pkt = ET.SubElement(root, "Packet")

                packettype1 = ET.SubElement(pkt, "Type")
                packettype1.text = str(j)

                time1 = ET.SubElement(pkt,"Time")
                time1.text = str(i.time)
                addr1 = ET.SubElement(pkt,"Addr1")
                addr1.text = str(i.addr1)
                addr2 = ET.SubElement(pkt,"Addr2")
                addr2.text = str(i.addr2)
                info1 = ET.SubElement(pkt,"Probe")
                info1.text = str(i.info)

    tree = ET.ElementTree(root)
    tree.write(oFile)

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

# y = SniffExistingFile('capture1-05.cap')

# scapyplist2xml(y)

#



# --------------------------------------


# References ===============================================

# This was the basis for XML

# https://docs.python.org/2/library/xml.etree.elementtree.html

# I used the tutorial below to clarify a few things that were unclear
#   from the python documentation above.

# http://effbot.org/zone/element-index.htm

# ===========================================================