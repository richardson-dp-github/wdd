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


def scapyplist2xml(p, writefilename):
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
                info1 = ET.SubElement(pkt,"SSID")
                info1.text = str(i.info)

    tree = ET.ElementTree(root)
    tree.write(writefilename)

def SniffExistingFile(f):
    return sniff(offline=f);

# f is the pcap file
# will save an XML at writefilename
def pcap2xml(f, writefilename='output.xml'):
    scapyplist2xml(SniffExistingFile(f),writefilename)


# -------------------------------------
# START Global Variables (for now)
# -------------------------------------

PacketsOfInterest = []

PacketsOfInterest.append(Dot11ProbeReq)
PacketsOfInterest.append(Dot11ProbeResp)
PacketsOfInterest.append(Dot11AssoReq)

print PacketsOfInterest


# -------------------------------------
# END Global Variables (for now)
# -------------------------------------




# -------------------------------------
# Test out the function here
# -------------------------------------

pcap2xml('capture1-05.cap', "output.xml")

# --------------------------------------


# References ===============================================

# This was the basis for XML

# https://docs.python.org/2/library/xml.etree.elementtree.html

# I used the tutorial below to clarify a few things that were unclear
#   from the python documentation above.

# http://effbot.org/zone/element-index.htm

# ===========================================================