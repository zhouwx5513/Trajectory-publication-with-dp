from TDrive import ReadFromDirectory
import matplotlib.pyplot as plt
import  mzgeohash
from  TDrive import  Updatesample

# t = mzgeohash.encode((116.4036519233,39.9238241903),4)
# print(t)

print(mzgeohash.decode("wx4g"))

t = mzgeohash.encode((116.4406325205,39.9543963732),6)
print(t)

zone =[]
for i in mzgeohash.neighbors(mzgeohash.encode((116.4406325205,39.9543963732),6)).values():
    zone.append(i)
print(zone)
print(mzgeohash.neighbors(mzgeohash.encode((116.4406325205,39.9543963732),6)))

datas = ReadFromDirectory.FromDireGetData("J:\\DataSetForExp\\release\\test")
transDatas = ReadFromDirectory.CleanDataSet(datas)
transDatas.sort(key = lambda x:x[3],reverse = False)

transData = []
for ii in transDatas:
    # if(float(ii[0]) > 116.2075579685 and float(ii[0]) < 116.5632212466 and float(ii[1]) > 39.8333472137 and float(ii[1]) < 40.0326836503):
    transData.append(ii)
print(len(transData))
dicts = {}
target = ""
target = "wx4g3"
# for i in transData:
#     t = (float(i[0]),float(i[1]))
#     dicts[mzgeohash.encode(t,5)] = dicts.get(mzgeohash.encode(t,5), 0) + 1
#     if dicts.get(mzgeohash.encode(t,5))==1000:
#         target = mzgeohash.encode(t,5)
#         break
#
# print(dicts)
# print(target)
targetdata = []

for j in transData:
    t = (float(j[0]),float(j[1]))
    if  mzgeohash.encode(t,5)==target:
        targetdata.append(j)
        # if (len(targetdata)==1000):
        #     break
print(len(targetdata))








Updatesample.updateSample.upexams(targetdata)


x_values = []
y_values = []

# yes = 0
# no = 0

for i in targetdata:
    #
    # if (float(i[0]) > 116.2075579685 and float(i[0]) < 116.5632212466 and float(i[1]) > 39.8333472137 and float(i[1]) < 40.0326836503 ):
    #     yes+=1
    x_values.append(i[0])
    y_values.append(i[1])
    # else:
    #     print(i)
    #     no+=1
# print("yes:"+str(yes)+"  no:"+str(no)+"  total="+str(len(transData)))

plt.scatter(x_values, y_values, s=50)
# plt.scatter()
# 绘制散点图
plt.scatter(x_values, y_values)
# 设置图表标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=20)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
