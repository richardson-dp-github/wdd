from cassandra.cluster import Cluster
from scapy.all import *
import uuid
import time
import pr_pcapgen as prgen
import os
import csv

class CSV2CassandraKeyspace:

    def __init__(self, csv_filename='test1.csv', table_name='probes', keyspace='mykeyspace'):
        print "initializing CSV to Cassandra keyspace module..."
        self.csv_filename = csv_filename
        self.table_name = table_name
        self.keyspace = keyspace
        cluster = Cluster()
        self.session = cluster.connect(self.keyspace)
        self.headers = self.extract_headers()

    def create_keyspace(self):
        print "creating keyspace..."
        # Now, the simplest way is to take the headers and make them all

    def create_table(self):
        x = "CREATE TABLE "
        x += self.table_name
        x += "("
        # Temporarily create all to be varchars
        # x += "record_name varchar PRIMARY KEY,"

        # Add the headers
        hh = self.headers
        for h in hh:
            h = h + " " + "varchar"
        hhh = ', '.join(h)
        x += hhh

        x += ");"

        self.session.execute(x)

    def keyspace_exists(self):
        print "checking if keyspace exists..."

    def append_records(self):
        print "appending records..."

    def delete_existing_keyspace(self):
        print "deleting existing keyspace..."


    def ccleartable(session):
        session.execute("delete from probes where 1;")

    def overwrite_keyspace(self):
        print "overwriting existing keyspace..."

    def extract_headers(self):
        print "extracting headers..."
        # This is just reading the first row
        headers = self.read_into_list()
        return headers

    def generate_append_command(self):
        headers='prb_id, prb_time, prb_addr1, prb_ssid'
        numheaders=len(headers.split())
        values=', '.join(['%s']*numheaders)
        cmd='insert into probes ('+headers+') values ('+values+');'
        return cmd

    # This function will scan the imported CSV data and determine what kind of data type is appropriate.
    def determine_data_types(self):
        print "determining data types..."


    # This will read the
    def read_into_list(self):
        print "reading row..."
        x = []
        with open(self.csv_filename, 'r') as csvfile:
            data0 = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data0:
                x.append(', '.join(row))
        return x

