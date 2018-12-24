import time
import datetime
import mzgeohash
from  TDrive import  Updatesample

inputFileName = "J:\\DataSetForExp\\release\\test_output\\e.txt"

def getDataFlow(inputFileName):
    allTupleList = []
    with open(inputFileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            allTupleList.append(tuple)
    print("allTupleListSize = "+str(len(allTupleList)))
    return allTupleList


def windowDeal(allTupleList):
    # dicts[word] = dicts.get(word, 0) + 1
    # dicts = {"win0":[(1,2)],"win1":[(1,2)],"win2":[(1,2)],"win3":[(1,2)],"win4":[(1,2)],"win5":[(1,2)],"win6":[(1,2)],"win7":[(1,2)],"win8":[(1,2)],"win9":[(1,2)]}
    w1 = []
    w2 = []
    w3 = []
    w4 = []
    w0 = []
    w5 = []
    w6 = []
    w7 = []
    w8 = []
    w9 = []
    dicts = {}
    index = 0
    fina = len(allTupleList)
    while (index<fina):
        time.sleep(0.001)
        end = index + 100
        list1 = allTupleList[index:end]
        for i in list1:
            if(int(i[2])%10==0):
                w0.append(i)
                if(len(w0)==1000):
                    print(str(datetime.datetime.now())+" , w0")
                    dicts["w0"] = dicts.get("w0", 0) + 1
                    id = "w0_"+str(dicts.get("w0", 0))
                    winOperation(w0,id)
                    w0.clear()
            if (int(i[2]) % 10 == 4):
                w4.append(i)
                if(len(w4)==1000):
                    print(str(datetime.datetime.now())+" , w4")
                    w4.clear()
                    dicts["w4"] = dicts.get("w4", 0) + 1
            if (int(i[2]) % 10 == 3):
                w3.append(i)
                if(len(w3)==1000):
                    print(str(datetime.datetime.now())+" , w3")
                    w3.clear()
                    dicts["w3"] = dicts.get("w3", 0) + 1
            if (int(i[2]) % 10 == 2):
                w2.append(i)
                if(len(w2)==1000):
                    print(str(datetime.datetime.now())+" , w2")
                    w2.clear()
                    dicts["w2"] = dicts.get("w2", 0) + 1
            if (int(i[2])% 10 == 1):
                w1.append(i)
                if (len(w1) == 1000):
                    print(str(datetime.datetime.now())+" , w1")
                    w1.clear()
                    dicts["w1"] = dicts.get("w1", 0) + 1
            if (int(i[2]) % 10 == 9):
                w9.append(i)
                if (len(w9) == 1000):
                    print(str(datetime.datetime.now()) + " , w9")
                    w9.clear()
                    dicts["w9"] = dicts.get("w9", 0) + 1
            if (int(i[2]) % 10 == 8):
                w8.append(i)
                if (len(w8) == 1000):
                    print(str(datetime.datetime.now()) + " , w8")
                    w8.clear()
                    dicts["w8"] = dicts.get("w8", 0) + 1
            if (int(i[2]) % 10 == 7):
                w7.append(i)
                if (len(w7) == 1000):
                    print(str(datetime.datetime.now()) + " , w7")
                    w7.clear()
                    dicts["w7"] = dicts.get("w7", 0) + 1
            if (int(i[2]) % 10 == 6):
                w6.append(i)
                if (len(w6) == 1000):
                    print(str(datetime.datetime.now()) + " , w6")
                    w6.clear()
                    dicts["w6"] = dicts.get("w6", 0) + 1
            if (int(i[2]) % 10 == 5):
                w5.append(i)
                if (len(w5) == 1000):
                    print(str(datetime.datetime.now()) + " , w5")
                    www = []


                    for jj in w5:
                        print(jj)
                        if (float(jj[0]) > 116.2075579685 and float(jj[0]) < 116.5632212466 and float(
                            jj[1]) > 39.8333472137 and float(jj[1]) < 40.0326836503):
                            www.append(jj)

                    print(len(www))
                    Updatesample.updateSample.upexams(www)
                    w5.clear()
                    dicts["w5"] = dicts.get("w5", 0) + 1
                    # Updatesample.updateSample.upexams(w5)
                    # for kk in w5:
                    #     print(kk)
                    # w5.clear()
                    return

        index = end
        if(index%10000==0):
            print("index = "+str(index))

    print(dicts)



def winOperation(list1,id):
    list2 = []
    dicts={}
    for i in list1:
        code = mzgeohash.encode((float(i[0]),float(i[1])),5)
        tuples = (i[2],code,i[3])
        list2.append(tuples)
        dicts[code] = dicts.get(code,0) + 1
    print("id : "+id,end="  ")
    print(dicts)





windowDeal(getDataFlow(inputFileName))










# for j in range(1,11):
            #     if(int(i[2])%j==0):
            #         var = "win"+str(j)
            #         print(dicts.get(var))
            #         print(type(dicts.get(var)))
            #         s = dicts.get(var).insert(0,i)
            #         print(s)
            #         print(type(s))
            #         dicts[var] = s.append(i)
            #         print(var)
            #         print(dicts.get(var))
            #         print(dicts[var])
            #         # if(dicts.get(var)==None):
            #         #     dicts[var]=[]
            #         # dicts[var] = dicts.get(var).append(i)
            #         # print(dicts[var])
            #         if(len(dicts.get(var,[]))==1000):
            #             print(str(datetime.datetime.now()) + " , "+var)
            #             dicts[var] = []

