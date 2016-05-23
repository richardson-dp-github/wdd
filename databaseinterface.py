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


# Open database connection
db = MySQLdb.connect("localhost",userName,passWord,dbName )

# append a file to the table
## import the file
f = 'output_msg1.xml'
for event, elem in ET.iterparse(f, events=('start', 'end', 'start-ns', 'end-ns')):
   print event, elem




# disconnect from server
db.close()