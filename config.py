# Test Configuration


# Is this a test, or is this for real?
TestMode = True


# Central Server's Loopback Address
centralServerIPAddress = '127.0.0.1'
centralServerPort = 50000
slaveIPAddress = '127.0.0.1'
slavePort = 50001

# Initialize a sample size
initialPeriodInSeconds = 100

#sample
sampleFile = 'capture1-05.cap'

# Rewrite Any Differences
if TestMode == True:
    centralServerIPAddress = '127.0.0.1'
    centralServerPort = 50000
else:
    centralServerIPAddress = '127.0.0.1'
    centralServerPort = 50000