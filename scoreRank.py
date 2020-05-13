# In[1]
# 读取文件

import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# In[2]
# 导入文件

file_name = './score.xls'
xls = pd.ExcelFile(file_name)
df = xls.parse('Sheet1',dtype='object')
df.head() # 显示前五行数据

# In[3]
# 显示基本信息
print('Data shape is:', df.shape)
print('Data index is:', df.index)
print('Columns title:', df.columns)
print('Sum of column data:')
df.count()

df.dtypes

# In[4]
#统计各科最高分 最低分 平均分

scoredf=df.loc[:,'微分':'领经']
basicData=pd.DataFrame(pd.concat([scoredf.max(),scoredf.min(),scoredf.mean()],axis=1))
basicData.columns=['High','Low','Average']  #替换行索引
basicData

# In[4]
# 绘制某科分数直方图
import matplotlib.pyplot as plt

plt.hist(x=df['微经'],bins=20)
plt.xlabel('score')
plt.ylabel('people')
plt.show()

# In[5]
# 统计各志愿人数
aimLevel=['志愿1','志愿2','志愿3','志愿4']
stock=[]
# series列表/堆栈
for aim in aimLevel:
    stock.append(df.loc[:,aim].value_counts())
# 将series列表/堆栈转换为DataFrame
pd.concat(stock,axis=1)

# In[6]
# 进行专业筛选

aimdf=df.loc[:,'学号':'学分绩']
aimdf.set_index(['学号',],inplace=True)
aimdf=aimdf.sort_values(by='学分绩',ascending=False) #按成绩降序
aimdf.head()

plan={'经济学':400,'国经贸':300,'财政':200,'商经':100} #确定招收名额
# 遍历每个学生的志愿
for a in range(len(aimLevel)):
    for s in range(1000):
        #如果有名额，就将后面的志愿清除
        if plan.get(aimdf.iloc[s,a],0) > 0:
            plan[aimdf.iloc[s,a]] -= 1
            abackup=a
            while a+1 < len(aimLevel):
                aimdf.iloc[s,a+1]=''
                a+=1
            a=abackup
        #如果无名额，将当前阶段志愿清除
        else:
            aimdf.iloc[s,a]=''

aimdf

# In[7]
# 统计按各级志愿录取的人数
stock=[]
for aim in aimLevel:
    stock.append(aimdf.loc[:,aim].value_counts())
result=pd.concat(stock,axis=1)
# 清除空值统计
result=result.drop(index='')
# 将NaN替换为0
result=result.fillna(0)
# 将所有数据类型变为整数型
result=result.astype('int64')

result

# %%
