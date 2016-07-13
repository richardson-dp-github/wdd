# This was modeled on an actual collect of the owner's own devices.
# All channels were modeled via Wireshark and a Wi-Pi put into monitor mode via aircrack-ng
# Probe Requests are broadcast, so there is no indication of whether or not the Wi-Pi was successfully put in monitor mode

import random, datetime



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

class WiFiEmitterSet:

    def __init__(self, numEmitters):
        self.numEmitters = numEmitters
        self.emitters = []
        self.emitters.append(WiFiEmitter_DirectToDatabase)



