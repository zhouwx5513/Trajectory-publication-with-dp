import time
import datetime
import mzgeohash

inputFileName = "J:\\DataSetForExp\\release\\test_output\\e.txt"

def getDataFlow(inputFileName):
    allTupleList = []
    with open(inputFileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            if (float(lines[0]) > 116.2075579685 and float(lines[0]) < 116.5632212466 and float(lines[1]) > 39.8333472137 and float(lines[1]) < 40.0326836503):
                allTupleList.append(tuple)
    print("allTupleListSize = "+str(len(allTupleList)))
    return allTupleList

def neigh(a,b):
    if b in mzgeohash.neighbors(a).values():
        return 1
    else:
        return 0

def dealWin(tamp, param):
    print(len(tamp),param)
    list2 = []
    dicts = {}
    users = {}
    com = {}
    for i in tamp:
        code = mzgeohash.encode((float(i[0]), float(i[1])), 7)
        user = i[2]
        coms = code+user

        tuples = (i[2], code, i[3])
        list2.append(tuples)
        dicts[code] = dicts.get(code, 0) + 1
        users[user] = users.get(user,0) +1
        com[coms] = com.get(coms,0)+1
    print(users)
    userss = sorted(com.items(), key=lambda x: x[1], reverse=True)
    print(dicts)
    print(com)
    print(userss)
    print(len(dicts.keys()),len(users.keys()),len(com.keys()))
    # print(dicts.keys())
    iindiff = {}
    for i in users.keys():
        for j in com.keys():
            if i == j[7:]:
                iindiff[i] = iindiff.get(i,0)+1
    # print(iindiff)
    iindiff = sorted(iindiff.items(), key=lambda x: x[1], reverse=True)
    print(iindiff)



    print("============================================================================")


    for i in users.keys():
        ii=[]
        T = True
        for j in tamp:
            if j[2]==i:
                ii.append(mzgeohash.encode((float(j[0]), float(j[1])), 7))
        if len(ii)>=2:
            co = ii[0]
            for jj in range(1,len(ii)):
                # ju = neigh(co,ii[jj])
                if neigh(co,ii[jj])==0:
                    T=False
                    break
                co = ii[jj]
        print(i,T,end="  ")









def dealPerMin(allTupleList):
    start = int(int(allTupleList[0][3])/30)*30
    sta = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(start))
    end = int(int(allTupleList[0][3])/30)*30+30
    sta1 = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(end))
    # print(sta,sta1)
    index = 0

    while True :
        tamp = []
        end = start+30
        while True:
            if int(allTupleList[index][3])>=start and int(allTupleList[index][3])<end:
                tamp.append(allTupleList[index])
                index+=1
            else:
                break

        dealWin(tamp,time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(end)))
        time.sleep(5)
        start = end








dealPerMin(getDataFlow(inputFileName))
