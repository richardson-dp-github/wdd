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
                                  #'08' +                              # tag length
                                  str(binascii.b2a_hex(len(ssid))) +
                                  # '32 57 49 52 45 30 32 34'         # SSID parameter set
                                  str(binascii.a2b_hex(ssid)) +
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


#test

ProbeRequestPCAPEntry('aabbccddeeff','testssid').generatePCAP('packets.pcap')
