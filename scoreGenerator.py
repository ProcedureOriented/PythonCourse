# In[1]
import xlwt,random
import numpy as np

def giveScore(avg=85,sigma=5):
    score = -1
    while not 0 <= score <= 100:
        score = int(np.random.normal(avg, sigma))
    else:
        return score

def calcScore(personScore):
    scorePoint=[2.5,2,1,2.5,1,2.5,3,3,3,1]
    t = 0
    for i in range(len(personScore)):
        t += personScore[i] * scorePoint[i]
    return t/sum(scorePoint)

def scoreRand(l):
    ls=[]
    for n in range(l):
        ls.append(giveScore())
    return ls

# 建表
courseName=['微分','积分','体育','英语','军训','思修','计算机','政经','微经','领经']
listTitle=['学号','志愿1','志愿2','志愿3','志愿4','学分绩']+courseName
aimList=['经济学','国经贸','财政','商经']
scoreList = xlwt.Workbook()
sht1 = scoreList.add_sheet('Sheet1')

for i in range(len(listTitle)):
    sht1.write(0,i,listTitle[i])

n=1
while n <= 1000:
    fin=scoreRand(len(courseName))
    fin.insert(0,calcScore(fin))
    random.shuffle(aimList)
    fin=aimList+fin
    fin.insert(0,1910000+n)

    for m in range(len(fin)):
        sht1.write(n,m,fin[m])
    
    n+=1

scoreList.save('./score.xls')
print('Done.')


# %%
