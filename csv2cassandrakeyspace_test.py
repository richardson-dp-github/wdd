import csv2cassandrakeyspace as c2c

class CSV2CassandraKeyspaceTester:

    def __init__(self, csv_filename='test1.csv'):
        print "initializing CSV to Cassandra keyspace module..."
        self.csv_filename = csv_filename
        self.test_read_row = False
        self.test_generate_append_command = True
        self.s = c2c.CSV2CassandraKeyspace('test1.csv')

    def create_keyspace(self):
        print "creating keyspace..."

    def keyspace_exists(self):
        print "checking if keyspace exists..."

    def append_records(self):
        print "appending records..."

    def delete_existing_keyspace(self):
        print "deleting existing keyspace..."

    def overwrite_keyspace(self):
        print "overwriting existing keyspace..."

    def extract_headers(self):
        print "extracting headers..."

    def generate_append_command_test(self):
        print "Testing the generate append command..."
        print self.s.generate_append_command()

    def read_row_test(self):
        print "Running read_row_test, the test for read_into_list"
        s = c2c.CSV2CassandraKeyspace('test1.csv')
        x = s.read_into_list()
        for row in x:
            print row

    def __main__(self):
        if self.test_read_row:
            self.read_row_test()
        if self.test_generate_append_command:
            self.generate_append_command_test()


def __main__():
    st = CSV2CassandraKeyspaceTester()
    if st.test_read_row:
        st.read_row_test()
    if st.test_generate_append_command:
        st.generate_append_command_test()


__main__()