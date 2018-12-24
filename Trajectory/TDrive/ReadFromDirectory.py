from TDrive import Tran
from TDrive import Updateexample
from TDrive import text
from TDrive import calculator
import time
import  os

# class Read:
#
def loadDataSet(fileName):
    data=[]

    cleans = ""

    with open(fileName) as fr:
        for line in fr.readlines():

            lines = line.strip('\n').split(",")
            timeStamp = time.mktime(time.strptime(lines[1], '%Y-%m-%d %H:%M:%S'))
            tamp = str(timeStamp) + str(lines[0])
            if tamp != cleans:
                timeStamp = int(timeStamp)
                t = (lines[2], lines[3],lines[0],timeStamp)
                # data.append(t)
                data.append(Tran.GpsToBaidu.dealtuple(t))
                cleans = tamp

    return data

def FromDireGetData(directory):
    z = 0
    datas=[]
    for maindir, subdir, file_name_list in os.walk(directory):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            t = loadDataSet(apath)
            for i in t:
                datas.append(i)
            z+=1
            print(z,len(t),filename)
            # time.sleep(0.05)
    print(str(len(datas)),z)
    return datas

def CleanDataSet(datas):
    sum = 0
    transResult = []
    for i in datas:
        for j in i:
            sum += 1
            print(sum)
            new = Tran.GpsToBaidu.dealtuple(j)
            transResult.append(new)
    # print(sum)
    return transResult


def writeTuple(fileName,data):
        index = 0
        with open(fileName, 'w') as f:
            for i in data:
                ss = str(i[0])+","+str(i[1])+"\n"
                index += 1
                f.write(ss)
            f.close()
        print("over!!")

















