# Interface between MySQL database and XML file

import MySQLdb
import xml.etree.ElementTree as ET #for XML conversion
import time

#parameters

userName = 'wifipi'
passWord = 'wifipi'
dbName = 'wifipi'

def runCommand(s):
    cursor = db.cursor()
    cursor.execute(s)
    data = cursor.fetchone()
    print data

def requestCommand():
    s='this is a string'
    while (s != 'q'):
        try:
            s = input('Enter Command, q to quit: ')
            print '\n'
            runCommand(s)
        except:
            print 'That did not work, try again...'

def dictionaryToTupleValues(d):
    x = ()
    for vals in d.itervalues():
        x = x + (vals,)
    return x

def test_dictionaryToTupleValues():
    x = {'species': 'hippo', 'status': 'hungry hungry'}
    print x, type(x)
    y = dictionaryToTupleValues(x)
    print y, type(y)

def displayList(l, withQuotes=False):
    ds = ''
    for s in l:
        if not withQuotes:
            ds = ds + str(s) + ','
        else:
            ds = ds + "'" + str(s) + "'" + ','
    ds = ds.rstrip(',')    # Remove the trailing comma
    return ds

# xmlfile is the name of a file
def xmlFileToCentralDB(xmlfile):
    f = ET.parse(xmlfile)
    for item in f.iterfind('Packet'):
        addPacketDictToCentralTable(translateValsAndFieldNamesIntoCentralDBPreferredTerms(singleXMLElementToDictionary(item)))

def test_xmlFileToCentralDB():
    xmlFileToCentralDB('output_msg1.xml')

# p is a dictionary
def addPacketDictToCentralTable(p):
    fieldlist = []
    valuelist = []
    for field, value in p.iteritems():
        fieldlist.append(field)
        valuelist.append(value)

    strSQLCmd = 'INSERT into Packets (' + displayList(fieldlist, False) +  ') values (' + displayList(valuelist, True) + ')'
    print strSQLCmd
    cursor = db.cursor()
    cursor.execute(strSQLCmd)
    db.commit()


def test_addPacketDictToCentralTable():
    x = {'nodeID': 5, 'locTimeStamp': '1987-04-20 03:54:32', 'wifipackettype': 'ProbeRequest','addr1': 'ff:ff:ff:ff:ff:ff', 'addr2': 'ff:ff:ff:ff:ff:ff'}
    print x, type(x)
    addPacketDictToCentralTable(x)

# x = single XML
def singleXMLElementToDictionary(x):
    xx = {}
    for i in x:
        # print 'Tag: ' + i.tag
        # print 'Text: ' + i.text
        xx[i.tag] = i.text
    return xx

# Test
def test_signalXMLElementToDictionary():
    f = ET.parse('output_msg1.xml')
    for item in f.iterfind('Packet'):
        print singleXMLElementToDictionary(item)

# d is a dictionary
# This function will evolve over time
def translateValsAndFieldNamesIntoCentralDBPreferredTerms(d):
    valTranslationDict = {"<class 'scapy.layers.dot11.Dot11ProbeReq'>": 'ProbeRequest',
                          "<class 'scapy.layers.dot11.Dot11ProbeResp'>": 'ProbeResponse'}

    # First, the field names
    if 'Time' in d:
        d['locTimeStamp'] = time.strftime('%Y-%m-%d %H:%M:%S',  time.gmtime(float(d.pop('Time'))))
    if 'Type' in d:
        d['wifipackettype'] = d.pop('Type')

    # Now, the values
    for key, value in d.iteritems():
        if value in valTranslationDict:
            d[key] = valTranslationDict[value]    # Make the translation (d is passed by value)


    return d

def test_translateValsAndFieldNamesIntoCentralDBPreferredTerms():
    f = ET.parse('output_msg1.xml')
    for item in f.iterfind('Packet'):
        print translateValsAndFieldNamesIntoCentralDBPreferredTerms(singleXMLElementToDictionary(item))

# Open database connection
db = MySQLdb.connect("localhost",userName,passWord,dbName )




# append a file to the table
## import the file

#for event, elem in ET.iterparse(f, events=('start', 'end', 'start-ns', 'end-ns')):
#   print event, elem



# test_translateValsAndFieldNamesIntoCentralDBPreferredTerms()
test_xmlFileToCentralDB()


# disconnect from server
db.close()