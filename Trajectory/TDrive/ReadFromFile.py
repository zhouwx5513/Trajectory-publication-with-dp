from TDrive import Tran
from TDrive import Updateexample
from TDrive import text
from TDrive import calculator
import  os

# class Read:
#
#     def loadDataSet(fileName):
#         data=[]
#         with open(fileName) as fr:
#             for line in fr.readlines()[8:]:
#                 lines = line.strip('\n').split(",")
#                 # t = (lines[0],lines[1],lines[5],lines[6])
#                 timeStamp=lines[5]+"_"+lines[6]
#                 t = (lines[1], lines[0],filename[-7:-4],timeStamp)
#                 # print(t)
#                 data.append(t)
#         return data
#
#     def writeTuple(fileName,data):
#         index = 0
#         with open(fileName, 'w') as f:
#             for i in data:
#                 ss = str(i[0])+","+str(i[1])+"\n"
#                 index += 1
#                 f.write(ss)
#                 # if index%6==1:
#                 #     f.write(ss)
#                 #
#                 if index==20:
#                     break
#             f.close()
#         print("over!")
#     # inputName = 'J:\\data\\000\\Trajectory\\20081023025304.plt'
#
#
#     # def gete(i,inputName,outputName):
#     #     data = Read.loadDataSet(inputName)
#     #     Read.writeTuple(outputName,data)
#     #     text.Show.show(outputName)
#
# # outputName = 'J:\\data\\000\\20081023025304.txt'
#
# # C:\\Users\\Administrator\\Desktop\\dataset\\Geo\\000\\20081024020959.plt
# # inputName = "C:\\Users\\Administrator\\Desktop\\dataset\\Geo\\000\\20081024020959_B.plt"
#
# inputDirection = "J:\\Touch\\part2"
# outputDirection = "J:\\Touch\\part2\\output"
#
# # Read.gete(1,inputName,outputName)
#
# result = []
# transResult=[]
# for maindir, subdir, file_name_list in os.walk(inputDirection):
#     for filename in file_name_list:
#         if ".plt" in filename:
#             apath = os.path.join(maindir, filename)
#             data = Read.loadDataSet(apath)
#             result.append(data)
# sum= 0
# for i in result:
#     for j in i:
#         sum+=1
#         new = Tran.GpsToBaidu.dealtuple(j)
#         print(j)
#         print(new)
#         transResult.append(new)
#         print("-----------------------------------------------"+str(sum))
# print(sum)
#
# special=[]
# d = 0
# for i in transResult:
#     if i[2]=='146'and d<20:
#         d+=1
#         special.append(i)
# print('he'+str(len(special)))
#
# Updateexample.updateExam.upexams(special)

# inputName = "F:\\dataset\\02\\7105.txt"


def writeTuple(fileName,data):
        index = 0
        with open(fileName, 'w') as f:
            for i in data:
                ss = str(i[0])+","+str(i[1])+"\n"
                index += 1
                f.write(ss)
                # if index%6==1:
                #     f.write(ss)
                #
                # if index==20:
                #     break
            f.close()
        print("over!!")


#
# inputName = "J:\\DataSetForExp\\release\\taxi_log_2008_by_id\\2693.txt"
# outputName = "J:\\DataSetForExp\\release\\output\\he.txt"
# data=[]
# index  = 0
# print("hehe")
# with open(inputName) as fr:
#     for line in fr.readlines():
#         if index<60:
#             lines = line.strip('\n').split(",")
#             # t = (lines[0],lines[1],lines[5],lines[6])
#             timeStamp=lines[1]
#             t = (lines[2], lines[3],lines[0],timeStamp)
#             # print(t)
#             data.append(t)
#             index+=1
# print(data)
# sum= 0
# transResult=[]
# for i in data:
#     sum+=1
#     new = Tran.GpsToBaidu.dealtuple(i)
#     print(i)
#     print(new)
#     transResult.append(new)
#     print("-----------------------------------------------"+str(sum))
# print(sum)
#
#
# # Updateexample.updateExam.upexams(data)
# Updateexample.updateExam.upexams(transResult)
# writeTuple(outputName,transResult)
#
# total = calculator.calculatorRange(transResult)
# print(total)
#
# calculator.calculatorZone(transResult)
#
#
#
#
#
#
# text.Show.show(outputName)
def test1():
    inputName = "J:\\DataSetForExp\\release\\taxi_log_2008_by_id\\2693.txt"
    outputName = "J:\\DataSetForExp\\release\\output\\he.txt"
    data = []
    index = 0
    print("hehe")
    with open(inputName) as fr:
        for line in fr.readlines():
            if index < 60:
                lines = line.strip('\n').split(",")
                # t = (lines[0],lines[1],lines[5],lines[6])
                timeStamp = lines[1]
                t = (lines[2], lines[3], lines[0], timeStamp)
                # print(t)
                data.append(t)
                index += 1
    print(data)
    sum = 0
    transResult = []
    for i in data:
        sum += 1
        new = Tran.GpsToBaidu.dealtuple(i)
        print(i)
        print(new)
        transResult.append(new)
        print("-----------------------------------------------" + str(sum))
    print(sum)

    # Updateexample.updateExam.upexams(data)
    Updateexample.updateExam.upexams(transResult)
    writeTuple(outputName, transResult)

    total = calculator.calculatorRange(transResult)
    print(total)

    calculator.calculatorZone(transResult)

    text.Show.show(outputName)







