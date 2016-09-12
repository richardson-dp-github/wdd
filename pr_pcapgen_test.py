import pr_pcapgen as t
'''
p = t.ProbeRequest()

print p.get_header()
print p.tagssidparametersetitem0
print 'header length = ' + p.headerlength

print 'header length = ' + p.headerlength
print p.get_ssid()
p.set_ssid_ascii('paris')
print p.get_ssid()
print p.tagssidparametersetitem0
print 'header length = ' + p.headerlength
print hex(6).split('x')[1]
print format(6,'02x')
print format(len('prague'),'02x')
print format(1000,'04x')
hex_str = format(1000,'04x')
print 'hexstring = ' + hex_str

print 'Tag SSID Parameter Length'
print p.tagssidparametersetlength
p.set_ssid_ascii('2WIRE024')
print p.tagssidparametersetlength
print p.get_header()

pr0 = t.ProbeRequestPCAPEntry(p)

pf0 = t.PCAPFile()

pf0.addPacket(pr0)
pf0.addPacket(pr0)


x = []
x.append('first entry')
x.append('second entry')
print x

print pf0.pcap_entries
# pf0.generatePCAP('test.pcap')

pf0.generatePCAP('test.pcap')


# reverse_hex_str = hex_str[6:] + hex_str[4:6] + hex_str[2:4] + hex_str[:2]
reverse_hex_str = hex_str[2:4] + hex_str[:2]
print 'reverse hex string = ' + reverse_hex_str
'''


s = t.ScenarioGen2()
s.add_emitter(1,2,"aa:bb:cc:dd:ee:01")
s.add_emitter(1,2,"aa:bb:cc:dd:ee:02")
s.add_emitter(1,2,"aa:bb:cc:dd:ee:03")
s.add_emitter(1,2,"aa:bb:cc:dd:ee:04")

s.createCSV()