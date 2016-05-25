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

def insertRecord(nodeID, locTimeStamp, wifipackettype, addr1, addr2):
    cursor = db.cursor()
    #SQL query to INSERT a record into the table .
    #cursor.execute('''INSERT into Packets (nodeID, locTimeStamp, wifipackettype, addr1, addr2)
                  #values (%d, %f, %s, %s, %s)''',
                  #(nodeID, locTimeStamp, wifipackettype, addr1, addr2))
    cursor.execute('''INSERT into Packets (nodeID, locTimeStamp, wifipackettype, addr1, addr2) values (%s, %s, %s, %s, %s)''', (nodeID, locTimeStamp, wifipackettype, addr1, addr2))
    # Commit your changes in the database
    db.commit()

def displayList(l):
    ds = '';
    for s in l:
        ds = ds + s + ','
    ds = ds.rstrip(',')    # Remove the trailing comma
    return ds

# p is a dictionary
def addPacketToCentralTable(p):
    fieldlist = []
    valuelist = []
    for field, value in p:
        fieldlist.append(field)
        valuelist.append(value)

    strSQLCmd = '''INSERT into Packets (''' + displayList(fieldlist) +  ''') values (%s, %s, %s, %s, %s)'''
    print strSQLCmd


# x = single XML
def singleXMLElementToDictionary(x):
    xx = {}
    for i in x:
        # print 'Tag: ' + i.tag
        # print 'Text: ' + i.text
        xx[i.tag] = i.text
    return xx

# d is a dictionary
def translateValsAndFieldNamesIntoDatabase(d):
    valTranslationDict = {"<class 'scapy.layers.dot11.Dot11ProbeReq'>": 'ProbeRequest',
                          "<class 'scapy.layers.dot11.Dot11ProbeResp'>": 'ProbeResponse'}

    for key, value in d.iteritems():
        if value in valTranslationDict:
            d[key] = valTranslationDict[value]    # Make the translation (d is passed by value)
        if key == 'Time':
            d[key] = time.strftime('%Y-%m-%d %H:%M:%S',  time.gmtime(float(value)))

    return d

def test_translateValsAndFieldNamesIntoDatabase():
    f = ET.parse('output_msg1.xml')
    for item in f.iterfind('Packet'):
        print translateValsAndFieldNamesIntoDatabase(singleXMLElementToDictionary(item))

def test_signalXMLElementToDictionary():
    f = ET.parse('output_msg1.xml')
    for item in f.iterfind('Packet'):
        print singleXMLElementToDictionary(item)


def test_parseAndPrint():
    # Now Test Parsing the XML
    f = ET.parse('output_msg1.xml')
    for item in f.iterfind('Packet'):
        Type = item.findtext('Type')
        Time = item.findtext('Time')
        Addr1 = item.findtext('Addr1')
        Addr2 = item.findtext('Addr2')
        print(item)
        print(Type)
        print(Time)
        print(Addr1)
        print(Addr2)
        print()

        insertRecord(3,Time,Type,Addr1,Addr2)


def test_addPacketToCentralTable():
    f = ET.parse('output_msg1.xml')
    for item in f.iterfind('Packet'):
        addPacketToCentralTable(item)


# Test insertRecord
def test_insertRecord():
    insertRecord(1,'2000-06-22 05:45:00','ProbeRequest','FF:FF:FF:FF:FF:FF','FF:FF:FF:FF:FF:FF')


# Open database connection
db = MySQLdb.connect("localhost",userName,passWord,dbName )

test_translateValsAndFieldNamesIntoDatabase()


# append a file to the table
## import the file

#for event, elem in ET.iterparse(f, events=('start', 'end', 'start-ns', 'end-ns')):
#   print event, elem







# disconnect from server
db.close()