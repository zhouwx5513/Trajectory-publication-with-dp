from TDrive import MyTree2
import random
from TDrive import Updateexamplesssss
import  math
import  numpy as np
from TDrive import mygeohash
import numpy as np
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt

def getDataFlow(inputFileName):
    # 1201968000
    allTupleList = []
    userlist = set()
    usertimes = {}
    newuserlist = set()


    with open(inputFileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            userlist.add(lines[2])
            if usertimes.get(lines[2])==None:
                usertimes[lines[2]] = 1
            else:
                usertimes[lines[2]] = usertimes.get(lines[2]) + 1


            allTupleList.append(tuple)

            # print("allTupleListSize = " + str(len(allTupleList)))
            # return allTupleList

    print("allTupleListSize = "+str(len(allTupleList)))
    print("userlist = " + str(len(userlist)))
    print(type(usertimes))
    usertimes = sorted(usertimes.items(), key=lambda x: x[1], reverse=True)
    print(type(usertimes))

    print("usertime:", usertimes)
    for i in usertimes:
        if i[1]<=2000 and i[1]>=350:
            newuserlist.add(i[0])
    print(len(newuserlist))
    return  allTupleList,newuserlist
def getBudget(w,u):
    list = []
    for i in range(w):
        u1 = (u/(2*w))+((i*u)/(w*w-w))
        list.append(round(u1,4))
    # aver = float(round(np.mean(list),4))
    aver = list[len(list)-1]
    tuple = (list,aver)

    print(tuple)
    return tuple
def judge(time, begin):
    a = int((time-begin)/3600)
    return a
def creatTree(allList,currenttime):
    tree = MyTree2.tree()

    print("over!!",currenttime)
    print(allList[0])
    for i in allList:
        if i!=None:
            # tuples = (i[0],i[1],i[3])
            list0 = [i[0],i[1],i[3]]
            tree.Insert(str(i[2]),list0)
    print("over!",currenttime)
    return  tree
    # print(tree.getNodechildrenCount("14"))
    # print("over!!!")
    # data = tree.search("142")

    # datas = []
    # p = (math.exp(0.3) -1)/(math.exp(0.6)-1)
    # for i in data:
    #     if random.random()<p:
    #         datas.append(i)
    # print(len(datas),p,len(datas)/len(data))
    #
    # alls = []
    # alls.append(datas)
    # alls.append(data)
    # return alls
def creatTrees(allList,begin,end): #1201968000 1202054399 1201975200

    dicts = {}
    list1 = []
    currenttime = 0
    for j in allList:
        if judge(int(j[3]),begin)==currenttime:
            # tuple = (j[0], j[1], j[3]) # 经、纬、时间
            list1.append(j)
        else:
            tree = creatTree(list1,currenttime)
            dicts[currenttime] = tree
            currenttime = judge(int(j[3]), begin)
            list1=[]
            list1.append(j)
    if len(list1)>0:
        tree = creatTree(list1, currenttime)
        dicts[currenttime] = tree
        list1=[]

    return dicts
def query(dicts,id,time_k,e):

    allList = []

    for j in range(time_k):  #23 22 ...
        tree = dicts[len(dicts.keys())-j-1]
        list_tree = tree.search(str(id))
        allList.append(list_tree)

    tuple = getBudget(time_k,e)
    list = tuple[0]
    aver = tuple[1]
    list_p = []
    for i in range(time_k):
        p = (math.exp(float(list[i])) - 1) / (math.exp(float(aver)) - 1)
        list_p.append(p)

    newList = []
    for k in range(time_k):
        new_list = []
        for kk in allList[k]:
            if random.random()<list_p[k]:
                new_list.append(kk)
        print(k,"原：",len(allList[k]),"现：",len(new_list))
        newList.append(new_list)

    return newList,allList
def sample(lists, e, k):



    list_e = []
    list_p = []

    allList = []

    newLists = []

    t = (3*e)/(2*k)
    # t = 0.3
    for i in range(1,k+1):
        newList = []

        sum0 = len(lists[i-1])
        sum1 = 0
        ei = math.log(1+math.sqrt(  (math.exp(e*(k+2*i-3)/(2*k*(k-1)))-1 ) *  ( math.exp(t)-1 )         ))
        list_e.append(ei)
        pi = (math.exp(ei)-1)/(math.exp(t)-1)
        list_p.append(pi)
        # print(pi,ei)
        for each in lists[i-1]:
            if random.random()<pi:
                newList.append(each)
        sum1 = len(newList)

        print(sum0,sum1,sum1/sum0,pi)
        newLists.append(newList)


    return newLists, list_e
    # return  allList
def selectLargeRegion(countRegion, e):
    probability = {}
    probabilitys = {}
    sumofpro = 0
    sumofpros = 0
    # print("y",countRegion)
    for key in countRegion:
        num = round(math.exp(countRegion[key] * e / 2),5)
        probability[key] = num
        sumofpro+=num
    tamp = ""
    for i in probability.keys():
        probabilitys[i] = round(probability[i] / sumofpro, 5)
        sumofpros += probabilitys[i]
        tamp = i
        # print("ss",sumofpros ,probabilitys[i])

    probabilitys[tamp] = round(1.0 - round(sumofpros - probabilitys[tamp], 5), 5)
    # print(probabilitys)
    prolist = []
    prolists = []
    for i in probabilitys.keys():
        prolist.append(i)
        prolists.append(probabilitys[i])
    # print(prolist)
    # print(sum(prolists))
    a = np.random.choice(prolist, 1, prolists)
    return mygeohash.decode(a[0])
def selectRegion(score, e):

    probability={}
    probabilitys = {}
    sumofpro = 0
    sumofpros = 0
    for i in score.keys():
        num = round(math.exp(e*score[i]/2),5)
        probability[i] = num
        # print(probability[i])
        sumofpro += num

    tamp = ""
    for i in probability.keys():
        probabilitys[i] = round(probability[i]/sumofpro,5)
        sumofpros += probabilitys[i]
        tamp = i
        # print("ss",sumofpros ,probabilitys[i])
    probabilitys[tamp] = round(1.0 - round(sumofpros - probabilitys[tamp],5),5)

    # print(sumofpros,probabilitys)
    prolist = []
    prolists = []



    for i in probabilitys.keys():
        prolist.append(i)
        prolists.append(probabilitys[i])
    # print(prolist)
    # print(sum(prolists))
    a = np.random.choice(prolist, 1, prolists)

    return mygeohash.decode(a[0])
def TupleGeneralize(list,e):
    dicts ={}
    newList = []

    for each in list:
        dict = mygeohash.neighbors(mygeohash.encode(float(each[1]),float(each[0]),3))
        for eachjrregion in dict.values():
                if not eachjrregion in dicts:
                    dicts[eachjrregion] = 1
                else:
                    dicts[eachjrregion] = dicts[eachjrregion] + 1
    # print(dicts)
    # sum = 0
    # for kkk in dicts.values():
    #     sum+=kkk
    # print(sum)
    for each in list:
        score={}
        dict = mygeohash.neighbors(mygeohash.encode(float(each[1]), float(each[0]), 3))
        for eachjrregion in dict.values():
            score[eachjrregion] = dicts.get(eachjrregion)
        # print(score)
        position = selectRegion(score,e)
        neweach = (str(position[1]),str(position[0]),each[2],each[3])
        # print(position)
        newList.append(neweach)
        # print(newList)
    return newList



            #     if lists.get(j[2]) == None:
            # # lists[j[2]] = []
            # #         lists[j[2]].append(j)
def TupleMerge(listi,e):
    tupleSet = set()
    largeRegionDict = {}
    newLists = []

    print("sss",listi)

    for i in listi:
        # print(float(i[1]),float(i[0]),i[3])
        large = mygeohash.encode(float(i[1]),float(i[0]),2)
        tupleSet.add(large)
        if large not in largeRegionDict:
            largeRegionDict[large] = []
            largeRegionDict[large].append(i)
        else:
            largeRegionDict[large].append(i)
    for each in tupleSet:
        # newList = []
        countRegion = {}
        candidate = mygeohash.subregions(each)
        listtuple = largeRegionDict[each]
        for i in listtuple:
            lists = mygeohash.neighbors(mygeohash.encode(float(i[1]),float(i[0]),3))
            for k in lists.values():
                if k in candidate:
                    if k not in countRegion:
                        countRegion[k] = 0
                    countRegion[k] = countRegion[k]+1
        print(each,countRegion)
        position = selectLargeRegion(countRegion,1)
        for i in listtuple:
            neweach = (str(position[1]), str(position[0]), i[2], i[3])
            # print(position)
            newLists.append(neweach)
    # print("-------------------------------")
    # for i in newLists:
    #     print(i)
    newLists.sort(key=lambda x: x[3], reverse=False)
    # print("-------------------------------")
    # for i in newLists:
    #     print(i)
    return newLists
def getthecenter(list1):
    x = []
    y = []
    z = []
    for all in list1:
        x.append(float(all[0]))
        y.append(float(all[1]))
        z.append(int(all[3]))
    xi = np.mean(x)
    yi = np.mean(y)
    zi = int(np.mean(z))
    tuple = (str(xi),str(yi),list1[0][2],zi)
    print("++++++++")
    print(list1)
    print(tuple)
    print("+++++++++++++")


    return tuple
def clean(list):
    i = 0
    minbegin = int(int(list[0][3])/60)
    currentmin = minbegin
    list1=[]
    listall = []
    for each in list:
        if int(int(each[3])/60) == currentmin:
            list1.append(each)
        else:
            listall.append(getthecenter(list1))
            list1=[]
            currentmin = int(int(each[3])/60)
            list1.append(each)
    if len(list1)>0:
        listall.append(getthecenter(list1))
    return listall
def TupleSampling(userid,e,k,when,ta):

    # e1 = e*0.2
    e1 = 0.5
    e2 = e-e1
    # e2 = 0.5

    #1201968000
    start = 1201968000
    # start = 1239120000
    # start =1240502400
    # start = 1237392000
    fileName = "J:\\DataSetForExp\\2008_0203\\"+userid+".txt"
    # fileName = "J:\\Touch\\part5\\input\\035\\" + userid + ".txtx"
    tupleList = []

    Ni = []

    with open(fileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            tupleList.append(tuple)
    dicts = {}
    list1 = []
    currenttime = 0
    for j in tupleList:
        if judge(int(j[3]), start) == currenttime:
            list1.append(j)
        else:
            dicts[currenttime] = list1
            currenttime = judge(int(j[3]), start)
            list1 = []
            list1.append(j)
    if len(list1) > 0:
        dicts[currenttime] = list1
        list1 = []
    print(len(dicts.keys()))

    sum = 0
    for j in dicts.keys():
        sum +=len(dicts.get(j))
        print(j,len(dicts.get(j)))
    print("sum=",sum)

    lists = []
    listsdeal = []
    fartime = when - k  # 比如17点整发起查询的话，就是 17-5 = 12
    begintime = when -1
    for i in range(fartime, when):
        lists.append(dicts.get(i))
        Ni.append(len(dicts.get(i)))
    lists.reverse()

    # print("haha",clean(lists[0]))
    for jjj in lists:
        listsdeal.append(clean(jjj))


    Ni.reverse()
    # for k in lists:
    #     print(len(k))
    listsc,list_e= sample(listsdeal,e1,k)  #抽后44444444444444444

    # listsc,list_e= sample(lists,e,k)  #抽后44444444444444444

    print("list_e",list_e)
    allLists  = []                      #抽前
    allList = []
    allListdeal = []

    secretlist = []

    # print(listsc)


    tampSecret =[]
    for each in listsdeal:
        each.reverse()
        secretlist.append(each)
        secretlist.reverse()
    for each in secretlist:
        for i in each:
            tampSecret.append(i)
    print("hasq",len(tampSecret))




    for each in lists:
        each.reverse()
        for eachi in each:
            allLists.append(eachi)

    for each in listsdeal:
        each.reverse()
        for eachi in each:
            allListdeal.append(eachi)

    for each in listsc:
        each.reverse()
        for eachi in each:
            allList.append(eachi)


    allList.reverse()
    allLists.reverse()
    allListdeal.reverse()

    if(ta=="s"):
        print("hasq",len(secretlist))
        a,b = secretpass(secretlist,tampSecret,e2)
        return a,b

    Updateexamplesssss.updateExam.upexams(allLists,2)  #抽前
    Updateexamplesssss.updateExam.upexams(allList,1)  #抽后
    Updateexamplesssss.updateExam.upexams(allListdeal,5)
    # for i in allLists:
    #     print(i)


    # print("len : ",len(listsc[0]))

    trackByTSG = []
    tracksByTSG = []

    # print("hehe0", TupleGeneralize(listsc[0], list_e[0]))
    # print("hehe1", TupleGeneralize(listsc[1], list_e[1]))
    # print("hehe2", TupleGeneralize(listsc[2], list_e[2]))

    for i in range(len(listsc)):
        print("using e1 =", e1)
        newlist = TupleGeneralize(listsc[i],list_e[i]/Ni[i])
        # newlist = TupleGeneralize(listsc[i], list_e[i])
        trackByTSG.append(newlist)
    for each in trackByTSG:
        # each.reverse()
        for eachi in each:
            tracksByTSG.append(eachi)
    tracksByTSG.reverse()
    print(tracksByTSG)
    # print("hehe",tracksByTSG[0][0])
    Updateexamplesssss.updateExam.upexams(tracksByTSG, 3)

    finalTrack = []

    for each in range(len(trackByTSG)):
        tracks = TupleMerge(trackByTSG[each],e2)
        print("using e2 =",e2)
        for tr in tracks:
            finalTrack.append(tr)
    finalTrack.sort(key=lambda x: x[3], reverse=False)


    Updateexamplesssss.updateExam.upexams(finalTrack, 4)

    # return allListdeal,finalTrack
    return allListdeal, tracksByTSG
    # drawpic(finalTrack,allListdeal)






def TupleSamplings(userid,e,k,when,ta,pro):

    # e1 = e*0.2
    e1 = 0.5
    e2 = e-e1
    e1 = e*pro
    e2 = e-e1

    # e2 = 0.5

    #1201968000
    start = 1201968000
    # start = 1239120000
    # start =1240502400
    # start = 1237392000
    # fileName = "J:\\DataSetForExp\\2008_0203\\"+userid+".txt"

    fileName = "D:\\"+userid+".txt"

    # fileName = "J:\\Touch\\part5\\input\\035\\" + userid + ".txtx"
    tupleList = []

    Ni = []

    with open(fileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            tupleList.append(tuple)
    dicts = {}
    list1 = []
    currenttime = 0
    for j in tupleList:
        if judge(int(j[3]), start) == currenttime:
            list1.append(j)
        else:
            dicts[currenttime] = list1
            currenttime = judge(int(j[3]), start)
            list1 = []
            list1.append(j)
    if len(list1) > 0:
        dicts[currenttime] = list1
        list1 = []
    print(len(dicts.keys()))

    sum = 0
    for j in dicts.keys():
        sum +=len(dicts.get(j))
        print(j,len(dicts.get(j)))
    print("sum=",sum)

    lists = []
    listsdeal = []
    fartime = when - k  # 比如17点整发起查询的话，就是 17-5 = 12
    begintime = when -1
    for i in range(fartime, when):
        lists.append(dicts.get(i))
        Ni.append(len(dicts.get(i)))
    lists.reverse()

    # print("haha",clean(lists[0]))
    for jjj in lists:
        listsdeal.append(clean(jjj))


    Ni.reverse()
    # for k in lists:
    #     print(len(k))
    listsc,list_e= sample(listsdeal,e1,k)  #抽后44444444444444444

    # listsc,list_e= sample(lists,e,k)  #抽后44444444444444444

    print("list_e",list_e)
    allLists  = []                      #抽前
    allList = []
    allListdeal = []

    secretlist = []

    # print(listsc)


    tampSecret =[]
    for each in listsdeal:
        each.reverse()
        secretlist.append(each)
        secretlist.reverse()
    for each in secretlist:
        for i in each:
            tampSecret.append(i)
    print("hasq",len(tampSecret))




    for each in lists:
        each.reverse()
        for eachi in each:
            allLists.append(eachi)

    for each in listsdeal:
        each.reverse()
        for eachi in each:
            allListdeal.append(eachi)

    for each in listsc:
        each.reverse()
        for eachi in each:
            allList.append(eachi)


    allList.reverse()
    allLists.reverse()
    allListdeal.reverse()

    if(ta=="s"):
        print("hasq",len(secretlist))
        a,b = secretpass(secretlist,tampSecret,e2/k)
        return a,b

    Updateexamplesssss.updateExam.upexams(allLists,2)  #抽前
    Updateexamplesssss.updateExam.upexams(allList,1)  #抽后
    Updateexamplesssss.updateExam.upexams(allListdeal,5)
    # for i in allLists:
    #     print(i)


    # print("len : ",len(listsc[0]))

    trackByTSG = []
    tracksByTSG = []

    # print("hehe0", TupleGeneralize(listsc[0], list_e[0]))
    # print("hehe1", TupleGeneralize(listsc[1], list_e[1]))
    # print("hehe2", TupleGeneralize(listsc[2], list_e[2]))

    for i in range(len(listsc)):
        print("using e1 =", e1)
        newlist = TupleGeneralize(listsc[i],list_e[i]/Ni[i])
        # newlist = TupleGeneralize(listsc[i], list_e[i])
        trackByTSG.append(newlist)
    for each in trackByTSG:
        # each.reverse()
        for eachi in each:
            tracksByTSG.append(eachi)
    tracksByTSG.reverse()
    print(tracksByTSG)
    # print("hehe",tracksByTSG[0][0])
    Updateexamplesssss.updateExam.upexams(tracksByTSG, 3)

    finalTrack = []

    for each in range(len(trackByTSG)):
        tracks = TupleMerge(trackByTSG[each],e2)
        print("using e2 =",e2)
        for tr in tracks:
            finalTrack.append(tr)
    finalTrack.sort(key=lambda x: x[3], reverse=False)


    Updateexamplesssss.updateExam.upexams(finalTrack, 4)

    # return allListdeal,finalTrack
    return allListdeal, tracksByTSG
    # drawpic(finalTrack,allListdeal)





def secretpass(trackByTSG,tamp,e2):
    finalTrack = []
    tamp.sort(key=lambda x: x[3], reverse=False)

    for i in tamp:
        print("zzz",i)

    for each in range(len(trackByTSG)):
        tracks = TupleMerge(trackByTSG[each], e2)
        print("using e2 =", e2)
        for tr in tracks:
            finalTrack.append(tr)
    finalTrack.sort(key=lambda x: x[3], reverse=False)

    return tamp, finalTrack


def writeToTxt(all, fileName):
    with open(fileName, 'w') as f:
        for i in all:
            ss = i[0] + "," + i[1] + "," + i[2] + "," + i[3] + "\n"
            f.write(ss)
    f.close()

    # for i in data:
    #     if random.random()<p:
    #         datas.append(i)
def creatTr(allList):
    tree = MyTree2.tree()

    print("over!!")
    for i in allList:
        tuple = (i[0],i[1],i[3])
        tree.Insert(str(i[2]),tuple)
    print("over!")
    print(tree.getNodechildrenCount("14"))
    # print("over!!!")
    # data = tree.search("142")

    # datas = []
    # # p = round((math.exp(0.5) -1)/(math.exp(0.6)-1),3)
    # p = (math.exp(0.3) -1)/(math.exp(0.6)-1)
    # for i in data:
    #     if random.random()<p:
    #         datas.append(i)
    # print(len(datas),p,len(datas)/len(data))
    #
    # alls = []
    # alls.append(datas)
    # alls.append(data)
    # return alls

def drawpic(finalTrack,allListdeal):
    x_values = []
    y_values = []
    x1_values = []
    y1_values= []

    for i in finalTrack:
        x_values.append(float(i[0]))
        y_values.append(float(i[1]))
    for i in allListdeal:
        x1_values.append(float(i[0]))
        y1_values.append(float(i[1]))

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

    # 创建图并命名
    plt.figure('Line fig')
    ax = plt.gca()
    # 设置x轴、y轴名称
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
    # 参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
    ax.plot(x_values, y_values, color='r', linewidth=2, alpha=0.6)
    ax.plot(x1_values, y1_values, color='b', linewidth=2, alpha=0.6)

    plt.show()


# TupleSampling(userid,e,k,when)
# TupleSampling("941",1,3,22)

# TupleSampling("1088",1,3,22)

# TupleSampling("151",1,3,22)

def drawpics(lists):
    x1_values = []
    y1_values = []
    x2_values = []
    y2_values = []
    x3_values = []
    y3_values = []
    x4_values = []
    y4_values = []

    for i in lists[0]:
        x1_values.append(float(i[0]))
        y1_values.append(float(i[1]))
    for i in lists[1]:
        x2_values.append(float(i[0]))
        y2_values.append(float(i[1]))
    for i in lists[2]:
        x3_values.append(float(i[0]))
        y3_values.append(float(i[1]))
    for i in lists[3]:
        x4_values.append(float(i[0]))
        y4_values.append(float(i[1]))

    plt.figure('Line fig')
    ax = plt.gca()
    # 设置x轴、y轴名称
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
    # 参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
    l1, =ax.plot(x1_values, y1_values, color='r', linewidth=2, alpha=0.6)
    l2, =ax.plot(x2_values, y2_values, color='b', linewidth=2, alpha=0.6)
    l3, =ax.plot(x3_values, y3_values, color='y', linewidth=2, alpha=0.6)
    l4, =ax.plot(x4_values, y4_values, color='g', linewidth=2, alpha=0.6)
    plt.legend(handles=[l1, l2, l3, l4], labels=["epsilon=0.8", "epsilon=1.3","epsilon=1.8","original"], loc='best')
    plt.show()


# TupleSampling("405",1,2,13)
#
# TupleSampling("151",2,3,22)
# tuples= query(dicts,"215",5,1)
def TupleSamplingwithdiffere(id, w, when):

    # es = [0.8,1.3,1.8]
    es = []
    for i in range(16):
        es.append(round(0.5 + i * 0.1, 2))
    original = []
    lists = []
    for i in es:
        a,b = TupleSampling(id,i,w,when,"s")
        original = a
        lists.append(b)
    lists.append(original)
    listdtw = []


    for i in range(16):
        listdtw.append(50* DTWS(original[::50], lists[i][::50]))
        print("es:",es[i],listdtw[i])
    listdtw.sort(reverse=True)

    print(listdtw)
    return es,listdtw


    #
    # print("gou",len(original[::50]))
    # print("gous", len(lists[0][::50]))

    # drawpics(lists)



def drawdistributions(a,b,c,d,e,f):
    c = []
    # d = []
    e = []
    # f = []
    for i in a:
        c.append(i-0.02)
    # for i in b:
    #     d.append(i+10)
    for i in a:
        e.append(i+0.02)
    # for i in b:
    #     f.append(i-10)
    l1 =  plt.bar(left=a, height=b, width=0.02, alpha=0.2, color='#6699ff', label="一部门") #紫
    l2 =  plt.bar(left=c, height=d, width=0.02, alpha=0.2, color='r', label="一部门") #红
    l3 =  plt.bar(left=e, height=f, width=0.02, alpha=0.2, color='g', label="一部门")  #绿
    plt.legend(handles=[l2, l1, l3], labels=["k=3", "k=5", "k=7", ], loc='best')
    plt.xlabel('x')
    plt.ylabel('Av_DTW')
    plt.show()

def drawdistribution(a,b):
    # c = []
    # d = []
    # e = []
    # f = []
    # for i in a:
    #     c.append(i-0.02)
    # for i in b:
    #     d.append(i+10)
    # for i in a:
    #     e.append(i+0.02)
    # for i in b:
    #     f.append(i-10)
    plt.bar(left=a, height=b, width=0.02, alpha=0.2, color='#6699ff', label="一部门")
    # plt.bar(left=c, height=d, width=0.02, alpha=0.2, color='r', label="一部门")
    # plt.bar(left=e, height=f, width=0.02, alpha=0.2, color='g', label="一部门")
    plt.show()


def geodistances(p1,p2):
    lng1, lat1, lng2, lat2 = map(radians, [float(p1[0]), float(p1[1]),float(p2[0]), float(p2[1])])
    # print(lng1, lat1, lng2, lat2)
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    dis=2*asin(sqrt(a))*6371*1000
    return dis/1000
def head(A):
    return A[0]
def rest(B):
    return B[1:]
def DTW(A,B):
    if len(A)==0 and len(B)==0:
        return 0
    if len(A)==0 or len(B)==0:
        return float('inf')
    else:
        return geodistances(head(A), head(B)) + min(DTW(A, rest(B)), DTW(rest(A), B), DTW(rest(A), rest(B)))
        # return distance(head(A),head(B)) + min(DTW(A,rest(B)),DTW(rest(A),B),DTW(rest(A),rest(B)))
        # return abs(A[0]-B[0])+ min(DTW(A, rest(B)), DTW(rest(A), B), DTW(rest(A), rest(B)))
def DTWS(A,B):
    return (DTW(A,B)+DTW(B,A))/2

def TupleSamplingwithdifferw(id, e,w, when,flag):

    # es = [0.8,1.3,1.8]
    # w = [3,5,7]
    k = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    original = []
    lists = []
    for i in k:
        a,b = TupleSamplings(id,e,w,when,"s",i)
        original = a
        lists.append(b)
    lists.append(original)
    listdtw = []
    for i in range(9):
        listdtw.append(30* DTWS(original[::50], lists[i][::50]))
        # print("es:",es[i],listdtw[i])
    if flag==1:
        listdtw.sort(reverse=True)
    if flag==-1:
        listdtw.sort(reverse=False)


    # print(listdtw)
    return k,listdtw
def TupleDTWjudge(id, w, when):
    # es = [0., 1.3, 1.8]
    es = []
    for i in range(2):
        es.append(round(0.5+i*0.1,2))
    # print(es)
    original = []
    lists = []
    for i in es:
        a, b = TupleSampling(id, i, w, when, "s")
        original = a
        lists = b
        print("Dt",str(i),end="  :")
        print(50*DTWS(original[:50],lists[:50]))
        # lists.append(b)
    # lists.append(original)
# J:\Touch\part5\input\035
#
# a,b = TupleSamplingwithdiffere("4401",5,19)
# c,d = TupleSamplingwithdiffere("4401",3,19)
# e,f = TupleSamplingwithdiffere("4401",7,19)
# print(a,b)
# drawdistributions(a,b,c,d,e,f)
# drawdistribution(a,b)
# TupleSamplingwithdiffere("23",7,13)
a,b = TupleSamplingwithdifferw("4401",1.5,5,19,0)
c,d = TupleSamplingwithdifferw("4401",1.5,3,19,-1)    #true  down
e,f = TupleSamplingwithdifferw("4401",1.5,7,19,1) #False  raise
# drawdistribution(a,b)
drawdistributions(a,b,c,d,e,f)




# TupleDTWjudge("4401",5,13)





