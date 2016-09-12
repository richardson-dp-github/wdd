import numpy as np
import pandas as pd
import matplotlib as plt
import statsmodels.api as sm

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
df1['write_latency']=-df1['timebeforewrite']+df1['timeafterwrite']
'''
print 'here is the data frame with read_latency'
print df.describe()
print df.head(10)
'''
# df.boxplot(column='read_latency', by='datacount')

print "Now try to merge..."

x = pd.merge(df, df1,on='datacount',how='inner')

# Total time waited
x['total_latency']=x['afterread']-x['timebeforewrite']

print x

mod = sm.OLS(x['total_latency'],x['datacount'])
res = mod.fit()
print res.summary()

x.boxplot(column='total_latency', by='datacount')
# plt.axes.Axes.set_ylabel('total latency (s)')
plt.pyplot.show()
# don't really need this for the time being, it's just a distraction