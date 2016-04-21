#Author: Daniel Richardson with the guidance of John Pecarina
#Description:
#  The purpose of this code 'sniffs' (or parses) an existing file, 'capture1-05.pcap' and
#  displays any Probe Requests, Association Requests, and Probe Responses.  See the below pseudocode:

# If Probe Request - Print time of request, MAC of requestor, SSID of request
#     Dot11ProbeReq
# If Association Request - Print time of request, MAC of requestor, SSID of request
# If Probe Response - Print time of response, MAC of responder, SSID
#     Dot11ProbeResp


import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def SniffExistingFile(f):
    return sniff(offline=f);

y = SniffExistingFile('capture1-05.cap')

print "=============================================="
print "Probe Requests"
print "=============================================="
for i in y:
    if i.haslayer(Dot11ProbeReq):
        print "Time: {}, MAC of Requestor: {}, SSID: {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.time)), i.addr2, i.info)

print "=============================================="
print "Probe Responses"
print "=============================================="
for i in y:
    if i.haslayer(Dot11ProbeResp):
        print "Time: {}, MAC of Requestor: {}, SSID: {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.time)), i.addr2, i.info)

print "=============================================="
print "Association Requests"
print "=============================================="
for i in y:
    if i.type==0 and i.subtype==0:
        print "Time: {}, MAC of Requestor: {}, SSID: {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i.time)), i.addr2, i.info)




# The following sources were consulted:

# https://pen-testing.sans.org/blog/2011/10/13/special-request-wireless-client-sniffing-with-scapy
# http://hackoftheday.securitytube.net/2013/03/wi-fi-sniffer-in-10-lines-of-python.html
# https://github.com/0x90/uberscapy/blob/master/examples/wifi/sniffers/sniffer.py
#  In particular, I used this line to clue me into the filters.
#  lfilter=lambda p: p.haslayer(Dot11Beacon) or p.haslayer(Dot11ProbeResp) or p.haslayer(Dot11ProbeReq))
# https://thepacketgeek.com/importing-packets-from-trace-files/