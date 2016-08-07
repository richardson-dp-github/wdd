# This was modeled on an actual collect of the owner's own devices.
# All channels were modeled via Wireshark and a Wi-Pi put into monitor mode via aircrack-ng
# Probe Requests are broadcast, so there is no indication of whether or not the Wi-Pi was successfully put in monitor mode


import random
# import datetime
import hashlib, csv
from scapy.all import *
import binascii



#Global header for pcap 2.4
pcap_global_header =   ('D4 C3 B2 A1'
                        '02 00'         #File format major revision (i.e. pcap <2>.4)
                        '04 00'         #File format minor revision (i.e. pcap 2.<4>)
                        '00 00 00 00'
                        '00 00 00 00'
                        'FF FF 00 00'
                        '01 00 00 00')

#pcap packet header that must preface every packet
pcap_packet_header =   ('AA 77 9F 47'
                        '90 A2 04 00'
                        'XX XX XX XX'   #Frame Size (little endian)
                        'YY YY YY YY')  #Frame Size (little endian)


probe_request_frame_header = ('00'                              # Header revision
                              '00'                              # Header pad
                              '12 00'                           # Header length
                              '2e 48 00 00'                     # Present flags
                              '00'                              # Flags
                              '02'                              # Data Rate (1.0 Mb/s)
                              '6c 09'                           # Channel frequency
                              'a0 00'                           # Channel type: 802.11b
                              'd9'                              # SSI signal
                              '01'                              # Antenna
                              '04'                              # Type/Subtype: Probe Request
                              '00'                              # Flags
                              '00 00'                           # Duration
                              'ff ff ff ff ff ff'               # Receiver/Destination Address (broadcast)
                              'e4 90 7e cb 0f 07'               # Transmitter Address
                              'ff ff ff ff ff ff'               # BSS ID
                              '40 06'                           # sequence number
                              '00'                              # tag number
                              '08'                              # tag length
                              '32 57 49 52 45 30 32 34'         # SSID parameter set
                              '01'                              # tag number: supported rates
                              '04'                              # tag length
                              '02'                              # Supported Rates: 1 (0x02)
                              '04'                              # Supported Rates: 2 (0x04)
                              '0b'                              # Supported rates: 5.5 (0x0b)
                              '16'                              # Supported Rates: 11 (0x16)
                              '32 08 0c 12 18 24 30 48 60 6c'   # Tag: Extended Supported Rates 6, 9, 12, 18, 24, 36,
                                                                #      48, 54 [Mbit/sec]
                              '2d'                              # Tag Number: HT Capabilities
                              '1a'                              # Tag length
                              '6e 01'                           # HT Capabilities Info
                              '03'                              # A-MPDU Parameters: 0x03
                              'ff 00 00 00  00 00 00 00'        # Rx Modulation and Coding Scheme (One bit per
                                                                #      modulation): 1 spatial stream
                              '00 00 00 00  00 00 00 00'        # (continued)
                              '00 00'                           # HT Extended Capabilities
                              '00 00 00 00'                     # Transmit Beam Forming (TxBF) Capabilities
                              '00')                             # Antenna capabilities


import binascii
from scapy.all import *


class PcapWriter():



    #Global header for pcap 2.4
    pcap_global_header =   ('D4 C3 B2 A1'
                            '02 00'         #File format major revision (i.e. pcap <2>.4)
                            '04 00'         #File format minor revision (i.e. pcap 2.<4>)
                            '00 00 00 00'
                            '00 00 00 00'
                            'FF FF 00 00'
                            '7F 00 00 00')

class ProbeRequestPCAPEntry():

        #pcap packet header that must preface every packet
    def __init__(self,txmtr_address,ssid):

        #Global header for pcap 2.4
        self.pcap_global_header =   ('D4 C3 B2 A1'
                            '02 00'         #File format major revision (i.e. pcap <2>.4)
                            '04 00'         #File format minor revision (i.e. pcap 2.<4>)
                            '00 00 00 00'
                            '00 00 00 00'
                            'FF FF 00 00'
                            '7F 00 00 00')

        self.pcap_packet_header =   ('AA 77 9F 47'
                            '90 A2 04 00'
                            'XX XX XX XX'   #Frame Size (little endian)
                            'YY YY YY YY')  #Frame Size (little endian)

        self.pcap_packet_header_p1of2 =   ('AA 77 9F 47'
                            '90 A2 04 00')


        self.probe_request_frame_header = ('00'                              # Header revision
                                  '00'                              # Header pad
                                  '12 00'                           # Header length
                                  '2e 48 00 00'                     # Present flags

                                  '00'                              # Flags
                                  '02'                              # Data Rate (1.0 Mb/s)
                                  '6c 09'                           # Channel frequency
                                  'a0 00'                           # Channel type: 802.11b
                                  'd7'                              # SSI signal
                                  '01'                              # Antenna

                                  '00 00'                           # RX Flags
                                  '40'                              # Type/Subtype: Probe Request
                                  '00'                              # Flags
                                  '00 00'                           # Duration
                                  'ff ff ff ff ff ff' +             # Receiver/Destination Address (broadcast)
                                  txmtr_address +                   # Transmitter Address
                                  'ff ff ff ff ff ff'               # BSS ID
                                  'b0 ac'                           # sequence number
                                  '00' +                              # tag number
                                  '08' +                              # tag length
                                  # str(binascii.b2a_hex(len(ssid))) +
                                   '32 57 49 52 45 30 32 34'         # SSID parameter set
                                  #str(binascii.a2b_hex(ssid)) +
                                  '01'                              # tag number: supported rates
                                  '04'                              # tag length
                                  '02'                              # Supported Rates: 1 (0x02)
                                  '04'                              # Supported Rates: 2 (0x04)
                                  '0b'                              # Supported rates: 5.5 (0x0b)
                                  '16'                              # Supported Rates: 11 (0x16)
                                  '32 08 0c 12 18 24 30 48 60 6c'   # Tag: Extended Supported Rates 6, 9, 12, 18, 24, 36,
                                                                    #      48, 54 [Mbit/sec]
                                  '2d'                              # Tag Number: HT Capabilities
                                  '1a'                              # Tag length
                                  '6e 01'                           # HT Capabilities Info
                                  '03'                              # A-MPDU Parameters: 0x03
                                  'ff 00 00 00  00 00 00 00'        # Rx Modulation and Coding Scheme (One bit per
                                                                    #      modulation): 1 spatial stream
                                  '00 00 00 00  00 00 00 00'        # (continued)
                                  '00 00'                           # HT Extended Capabilities
                                  '00 00 00 00'                     # Transmit Beam Forming (TxBF) Capabilities
                                  '00')                             # Antenna capabilities
    def probe_request_frame_header_length(self):
        return self.getByteLength(self.probe_request_frame_header)

    def probe_request_frame_header_length_hex_for_pcap_entry(self):
        pcap_len = self.getByteLength(self.probe_request_frame_header)
        hex_str = "%08x"%pcap_len
        reverse_hex_str = hex_str[6:] + hex_str[4:6] + hex_str[2:4] + hex_str[:2]# four bytes long
        return reverse_hex_str

    def get_pcapentry(self):
        return ''.join(self.pcap_packet_header_p1of2 + self.probe_request_frame_header_length_hex_for_pcap_entry() + self.probe_request_frame_header)



    def getByteLength(self,str1):
        return len(''.join(str1.split())) / 2

    def writeByteStringToFile(self,bytestring, filename):
        bytelist = bytestring.split()
        bytes = binascii.a2b_hex(''.join(bytelist))
        bitout = open(filename, 'wb')
        bitout.write(bytes)

    def generatePCAP(self,pcapfile):


        pcap_len = self.getByteLength(self.probe_request_frame_header)
        hex_str = "%08x"%pcap_len
        reverse_hex_str = hex_str[6:] + hex_str[4:6] + hex_str[2:4] + hex_str[:2]
        pcaph = self.pcap_packet_header.replace('XX XX XX XX',reverse_hex_str)
        pcaph = pcaph.replace('YY YY YY YY',reverse_hex_str)

        bytestring = self.pcap_global_header + pcaph + self.probe_request_frame_header
        self.writeByteStringToFile(bytestring, pcapfile)

    #Splits the string into a list of tokens every n characters
    def splitN(str1,n):
        return [str1[start:start+n] for start in range(0, len(str1), n)]


class ProbeRequest:
    # the plan is to keep everything in hex, and then create get and set to translate in and out
    # This makes the most sense, since this is closely related to what the packets actually look like.

    def __init__(self):
        self.headerrevision = '00'
        self.headerpad = '00'
        self.headerlength = 'aa 00'
        self.presentflags = '2e 48 00 00'
        self.flags = '00'
        self.datarate = '02'
        self.channelfrequency = '6c 09'
        self.channelflags = 'a0 00'
        self.ssisignal = 'db'
        self.antenna = '01'
        self.rxflags = '00'
        self.typesubtype = '0040' #type/subtype probe request
        self.duration = '0000'
        self.receiveraddress = 'ff ff ff ff ff ff'
        # self.destinationaddress = 'ff ff ff ff ff ff'
        self.transmitteraddress = 'e4 90 7e cb 0f 07'
        self.bssid = 'ff ff ff ff ff ff'
        self.sequenceandfragnumber = '80 d2' # 0=frag number 3368=sequence number
        self.tagssidparameterset = '00'
        self.tagssidparametersetlength = '06'
        self.tagssidparametersetitem0 = '70 72 61 67 75 65'  #default is prague
        self.tagsupportedrates = '01 04 02 04 0b 16'
        self.tagextendedsupportedrates = '32 08 0c 12 18 24 30 48 60 6c'
        self.taghtcapabilities = '2d 1a 6e 01  03 ff 00 00 00 00 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00'

    # Reset the transmitter address
    #   This is a simple operation because this action will not change the size of the packet.
    def set_transmitter_address(self, mac_addr):

        self.transmitteraddress = mac_addr

    # set the ssid in a string format
    #   It requires the size of the tag to be reset as well as the size of the entire packet.
    def set_ssid_ascii(self, ssidinascii):
        #possible error checking for later might include limiting the length here
        self.tagssidparametersetitem0 = binascii.b2a_hex(ssidinascii)
        self.tagssidparameterlength = format(len(ssidinascii),'02x')
        self.recalculate_and_reset_headerlength()

    def recalculate_and_reset_headerlength(self):
        headerlength = self.get_header()
        hex_str = format(len(headerlength),'04x')
        reverse_hex_str = hex_str[2:4] + hex_str[:2]
        self.headerlength = reverse_hex_str

    def get_ssid(self):
        return binascii.a2b_hex(self.tagssidparametersetitem0.replace(" ",""))


    def get_header(self):
        return (''.join(self.headerrevision +
                       self.headerpad +
                       self.headerlength +
                       self.presentflags +
                       self.flags +
                       self.datarate +
                       self.channelfrequency +
                       self.channelflags +
                       self.ssisignal +
                       self.antenna +
                       self.rxflags +
                       self.typesubtype +
                       self.duration +
                       self.receiveraddress +
                       self.transmitteraddress +
                       self.bssid +
                       self.sequenceandfragnumber +
                       self.tagsupportedrates +
                       self.tagextendedsupportedrates +
                       self.taghtcapabilities)).replace(' ','')










class AccessPoint:
    SSID = ''
    SSIDHash = ''
    MACAddress = ''


    def __init__(self, SSID=''):
        self.SSID=self.generateSSID()

    def generateSSID(self):
        self.SSID = self.rtnRandomSSID(True)

    def rtnRandomSSID(self,common=True):
        CommonSSIDPool = ['xfinitiwifi', 'linksys', 'BTWiFi-with-FON', 'NETGEAR', 'dlink', 'Ziggo', 'BTWifi-X', 'default', 'FreeWiFi', 'hpsetup']
        RareSSIDPool_base = ['myqwest????','home-????','belkin.???.guests'] # '?' will be replaced by digits 0-9
        if common:
            SSID = random.choice(CommonSSIDPool)
        if not common:
            SSID = random.choice(RareSSIDPool_base)
            for char in SSID:
                if (char == '?'):
                    SSID=SSID.replace('?',str(random.randint(0,9)),1)
        return SSID


    def assignRandomMACAddress(self):
        self.MAC = ''
        for i in range(0, 6):
            for j in range(0, 2):
                self.MAC = self.MAC + random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
            if i < 6 - 1:
                self.MAC = self.MAC + ':'

    def getSSIDHash(self):
        return self.SSIDHash.hexdigest()








class WiFiEmitter_DirectToDatabase:

    SSIDPool = ['2WIRE024','Dunkin Guest','Panera','DubPub','Fly Dayton Public Wifi','Dublin Airport Free Wifi','prg.aero-free','WiFi2GO_007','prague','Hajnovka wifi','lavdis','Salanda','InternetAcko','MUNI','Hotel International Free']

    def __init__(self, freqInSeconds):
        self.savedSSIDProfiles = []
        self.freqInSeconds = 40
        self.MAC = "e4:90:7e:cb:0f:07"  #my phone


    def defineSSIDProfile(self):
        k = random.randint(3,6)
        self.savedSSIDProfiles = random.sample(self.SSIDPool,k)



    def assignRandomMACAddress(self):
        self.MAC = ''
        for i in range(0, 6):
            for j in range(0, 2):
                self.MAC = self.MAC + random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
            if i < 6 - 1:
                self.MAC = self.MAC + ':'

    def probe(self):
        tableEntries = []
        for i in self.savedSSIDProfiles:
            tableEntries.append((datetime.datetime,self.MAC,i))
        return tableEntries

class WiFiEmitter:

    def __init__(self, freqInSeconds):
        self.savedSSIDProfiles = []
        self.freqInSeconds = 40
        self.MAC = "e4:90:7e:cb:0f:07"  #my phone

    def defineSSIDProfile(self):
        k = random.randint(3,6)
        self.savedSSIDProfiles = random.sample(self.SSIDPool,k)

    def addPreferredAccessPoint(self, SSID):
        self.savedSSIDProfiles.append(SSID)


    def assignRandomMACAddress(self):
        self.MAC = ''
        for i in range(0, 6):
            for j in range(0, 2):
                self.MAC = self.MAC + random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
            if i < 6 - 1:
                self.MAC = self.MAC + ':'




    def probe(self):
        tableEntries = []
        for i in self.savedSSIDProfiles:
            tableEntries.append((datetime.datetime,self.MAC,i))
        return tableEntries

class WiFiEmitterSet:

    def __init__(self, numEmitters):
        self.numEmitters = numEmitters
        self.emitters = []
        for i in range(0,numEmitters):
            self.emitters.append(WiFiEmitter(40))
        for j in self.emitters:
            j.addPreferredAccessPoint("ap1")
            j.addPreferredAccessPoint("ap2")

class Scenario:

    def __init__(self, numEmitters=1):
        self.ws = WiFiEmitterSet(numEmitters)
        self.buf = scapy.plist.PacketList()



    # copied from online
    def writeByteStringToFile(self, bytestring, filename):
        bytelist = bytestring.split()
        bytes = binascii.a2b_hex(''.join(bytelist))
        bitout = open(filename, 'wb')
        bitout.write(bytes)

    def run_probes(self, max_time, pcapfile='collect.pcap'):
        bytestring = pcap_global_header
        pdump = scapy.utils.PcapWriter('collect.pcap', append=True, sync=True)
        for t in range(0,max_time):
            for e in self.ws.emitters:
                if divmod(t,e.freqInSeconds) == 0:
                    for ssid in e.savedSSIDProfiles():
                        p = scapy.layers.dot11.Dot11ProbeReq()
                        p.addr1 = e.MAC
                        p.info = ssid
                        pdump.write(p)

        # bytestring += str(self.buf.hexdump())
        # self.writeByteStringToFile(bytestring,pcapfile)



#test



