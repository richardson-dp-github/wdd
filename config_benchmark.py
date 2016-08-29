acceptable_values = []

# Set what are acceptable values for the row count
#  This has to be coordinated with the writer
for i in range(0,1000,100):
    if not i==0:
        acceptable_values.append(i)