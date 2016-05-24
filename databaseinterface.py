# Interface between MySQL database and XML file

import MySQLdb
import xml.etree.ElementTree as ET #for XML conversion

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
    cursor.execute('''INSERT into Packets (nodeID) values (1)''')  #This worked, now try the others
    cursor.execute('''INSERT into Packets (nodeID, locTimeStamp) values (2, 1042345000.22)''')
    # Commit your changes in the database
    db.commit()


# Open database connection
db = MySQLdb.connect("localhost",userName,passWord,dbName )

# append a file to the table
## import the file
#f = 'output_msg1.xml'
#for event, elem in ET.iterparse(f, events=('start', 'end', 'start-ns', 'end-ns')):
#   print event, elem

# Test insertRecord
insertRecord(1,45234442,1,'FF:FF:FF:FF:FF:FF','FF:FF:FF:FF:FF:FF')


# disconnect from server
db.close()