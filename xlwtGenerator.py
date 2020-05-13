import xlwt,time,random

def snoRand():
    sno=random.randint(1912049,1912308)
    if random.randint(1,500)==1: #随机错误
        return 0
    else:
        return sno

def dateRand():
    global start
    global end
    t=random.randint(start,end)
    dateTouple=time.localtime(t)
    date=time.strftime('%Y-%m-%d %A',dateTouple)
    if random.randint(1,500)==1: #随机错误
        return 0
    else:
        return date

def spendRand(q):
    price=random.randint(12,42)/2 #出现0.5的价格
    if random.randint(1,500)==1: #随机错误
        return 0
    else:
        return price*q

#dateRand初始数据组
a1=(2019,9,1,0,0,0,0,0,0)
a2=(2019,12,31,0,0,0,0,0,0)
start=time.mktime(a1)
end=time.mktime(a2)
#建表
formTitle=['StudentNo','Date','GoodNo','GoodName','Quantity','Spend']
goodList=['拉面','石锅饭','咖喱饭','米线','刀削面','麻辣香锅','重庆小面','黄焖鸡米饭','砂锅','小笼包','大锅菜','粥','麻辣烫','炒饭','家常菜','奶茶','水饺','意面','烤鱼','方便面']
xls = xlwt.Workbook()
sht1 = xls.add_sheet('Sheet1')
#写表头
for i in range(len(formTitle)):
    sht1.write(0,i,formTitle[i])
#写数据
maxNum=random.randint(8000,10000)
n=1
while n <= maxNum:
    good=random.randint(1,len(goodList))
    quantity=random.randint(1,4)
    formData=[snoRand(),dateRand(),str(1000+good),goodList[good-1],quantity,spendRand(quantity)]
    
    for m in range(len(formTitle)):
        sht1.write(n,m,formData[m])
    
    n+=1

xls.save('./mydata.xls')
print('Complete.')