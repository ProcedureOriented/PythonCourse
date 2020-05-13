# coding: utf-8

# In[1]:
# prepare and read file

import numpy as np
from pandas import Series,DataFrame
import pandas as pd


# In[2]:
# show basic info

file_name = './mydata.xls'
xls = pd.ExcelFile(file_name)
mydata = xls.parse('Sheet1',dtype='object')
mydata.head() # the top 5 data

print('Data shape is:', mydata.shape)
print('Data index is:', mydata.index)
print('Columns title:', mydata.columns)
print('Sum of column data:')
mydata.count()

mydata.dtypes


# In[3]:

# rename column title
mydata.rename(columns={'StudentNo':'StuNo'},inplace=True)
print('Rename successful')
mydata.head()


# In[4]:
# data washing

# remove Sunday...
f=lambda x:str(x).split(' ')[0]
mydata['Date']=mydata['Date'].map(f)
mydata.head()
print('Date change successful')


# In[5]:

# change date string to date format
'''
errors='coerce', change to NaT if original data is not match the format
'format' is the original format
'''
mydata.loc[:,'Date'] = pd.to_datetime(mydata.loc[:,'Date'],format='%Y-%m-%d',errors='coerce')
mydata.dtypes
print('Date format change successful')

 
# In[6]:
# change data type: string to float
mydata['Quantity'] = mydata['Quantity'].astype('float')
mydata['Spend'] = mydata['Spend'].astype('float')
mydata.dtypes
print('Data format change successful')


# In[7]:
# invalid data proceeding

print('Before deleting invalid data\n')
mydata.shape
mydata.info()

# dropna, deleting empty data
mydata = mydata.dropna(subset=['Date'],how='any')

# deleting impossible data
# check describe info
mydata.describe()

# delete 0 value
pop = mydata.loc[:,'StuNo'] > 0
mydata = mydata.loc[pop,:]

pop = mydata.loc[:,'Spend'] > 0
mydata = mydata.loc[pop,:]

# check again
mydata.describe()

print('\n\nAfter deleting invalid data\n')
mydata.shape
mydata.info()


# In[8]:

# ascending sort by date 
mydata = mydata.sort_values(by='Date',ascending=True)
mydata.head()

# reset index
mydata = mydata.reset_index(drop=True)
mydata.head()


# In[9]:
# building model and data visible

# index1: consume times per month

# count total consume times
# delete same data
i1 = mydata.drop_duplicates(subset=['StuNo','Date'])
total1 = i1.shape[0]
print('TotalConsumeTimes=',total1)  


# In[10]:
# count months
# ascending sort by Date
i1 = i1.sort_values(by='Date',ascending=True)
# rename row title
i1 = i1.reset_index(drop=True)

# get time range
# minimum time
startTime = i1.loc[0,'Date']
# maximum time
endTime = i1.loc[total1-1,'Date']

# count days
# day
days1 = (endTime-startTime).days
months1 = days1 // 30

print('months: ',months1)


# In[11]:
# count consume times per month
tpm = total1 // months1
print('index1: consume times per month=',tpm)


# In[12]:
# index2: cost per month
# total cost
totalCostSeries = mydata.loc[:,'Spend'].sum()
# cost per month
cpmSeries = totalCostSeries // months1
print('index2: cost per month=', cpmSeries)


# In[13]:
# index3: average price = total cost/total consume time
avgPrice = totalCostSeries / total1
print('index3 average price=',avgPrice)


# In[14]:
# index4: consume trends
import matplotlib.pyplot as plt
import matplotlib

# font setting
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

# backup data
mydataCopy = mydata


# In[15]:
# daily cost
# rename index as Date
mydataCopy.index = mydataCopy['Date']
mydataCopy.head()


# In[16]:
# plot

plt.plot(mydataCopy['Spend'])
plt.title('map on daily cost')
plt.xlabel('time')
plt.ylabel('Spend')
# save picture
plt.savefig('./dailyMap.png')
# show picture
plt.show()


# In[17]:
# cost monthly

# group date by month
monthGroup = mydataCopy.groupby(mydataCopy.index.month)
print(monthGroup)


# In[18]:
# use function to calculate monthly cost

monthlyCost = monthGroup.sum()
print(monthlyCost)


# In[19]:
# plot monthly cost

plt.plot(monthlyCost['Spend'])
plt.title('map on monthly cost')
plt.xlabel('month')
plt.ylabel('Spend')
plt.savefig('./monthlyMap.png')
plt.show()


# In[20]:
# goods sales detail

# count mounts by goods
goods = mydataCopy[['GoodName','Quantity']]
goodGroup = goods.groupby('GoodName')[['Quantity']]
re_goods = goodGroup.sum()

# descending sort
re_goods = re_goods.sort_values(by='Quantity',ascending=False)

re_goods.head()


# In[21]:
# top 10 goods

top_goods = re_goods.iloc[:10,:]
print(top_goods)


# In[22]:
# show top 10 goods by bar charts
top_goods.plot(kind='bar')

plt.title('Top 10 goods')
plt.xlabel('Name')
plt.ylabel('Quantity')
plt.legend(loc=0)
plt.savefig('./goods.png')
plt.show()


# %%
