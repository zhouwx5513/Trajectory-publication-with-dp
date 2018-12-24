from  TDrive import  ReadFromDirectory
from  TDrive import  Updatesample
import time

import numpy as np
import matplotlib.pyplot as plt
import datetime

starttime = datetime.datetime.now()
print(str(starttime))
#long running


# datas = ReadFromDirectory.FromDireGetData("J:\\DataSetForExp\\release\\test1")
# transDatas = ReadFromDirectory.CleanDataSet(datas)

transDatas = ReadFromDirectory.FromDireGetData("J:\\DataSetForExp\\release\\test1")


transDatas.sort(key = lambda x:x[3],reverse = False)

fileName = "J:\\DataSetForExp\\release\\test_output\\f.txt"

index = 0
with open(fileName, 'w') as f:
    for i in transDatas:
        ss = ""
        for j in i:
            ss=ss+str(j)+","
        ss = ss[:-1]+"\n"
        index += 1
        f.write(ss)

    f.close()
print("over!")

endtime = datetime.datetime.now()
print(str(endtime))

print (str((endtime - starttime).seconds))
# transData = []
# for ii in transDatas:
#     if(float(ii[0]) > 116.2075579685 and float(ii[0]) < 116.5632212466 and float(ii[1]) > 39.8333472137 and float(ii[1]) < 40.0326836503):
#         transData.append(ii)
#
#
# dataSize = 5000
#
# Updatesample.updateSample.upexams(transData[:dataSize])
#
#
# x_values = []
# y_values = []
#
# yes = 0
# no = 0
#
# for i in transData[:dataSize]:
#     #
#     if (float(i[0]) > 116.2075579685 and float(i[0]) < 116.5632212466 and float(i[1]) > 39.8333472137 and float(i[1]) < 40.0326836503 ):
#         yes+=1
#         x_values.append(i[0])
#         y_values.append(i[1])
#     else:
#         print(i)
#         no+=1
# print("yes:"+str(yes)+"  no:"+str(no)+"  total="+str(len(transData)))
#
# plt.scatter(x_values, y_values, s=50)
# # plt.scatter()
# # 绘制散点图
# plt.scatter(x_values, y_values)
# # 设置图表标题并给坐标轴加上标签
# plt.title('Square Numbers', fontsize=20)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()