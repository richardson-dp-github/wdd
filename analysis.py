import numpy as np
import pandas as pd
import matplotlib as plt


plt.interactive(False)

df = pd.read_csv("output_reader.csv")
print df.head(10)
print df.describe()

# df['count'].hist(bins=50)

df['read_latency']=df['afterread']-df['beforeread']

df.boxplot(column='read_latency', by='count')

plt.pyplot.show()