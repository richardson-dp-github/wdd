import pr_pcapgen as t

p = t.ProbeRequest()

print p.get_header()
print p.tagssidparametersetitem0
print 'header length = ' + p.headerlength
p.recalculate_and_reset_headerlength()
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


# reverse_hex_str = hex_str[6:] + hex_str[4:6] + hex_str[2:4] + hex_str[:2]
reverse_hex_str = hex_str[2:4] + hex_str[:2]
print 'reverse hex string = ' + reverse_hex_str