import numpy as np
import pandas as pd
import matplotlib as plt

correction = 0

plt.interactive(False)

df = pd.read_csv("output_reader.csv")
'''
print df.head(10)
print df.describe()
'''
df1 = pd.read_csv("output_writer.csv")
'''
print df1.head(10)
print df1.describe()
'''
# df['count'].hist(bins=50)

df['read_latency']=df['afterread']-df['beforeread']
'''
print 'here is the data frame with read_latency'
print df.describe()
print df.head(10)
'''
# df.boxplot(column='read_latency', by='datacount')

print "Now try to concatenate/join..."

x = pd.merge(df, df1,on='datacount',how='right')

print x

# plt.pyplot.show()
# don't really need this for the time being, it's just a distraction