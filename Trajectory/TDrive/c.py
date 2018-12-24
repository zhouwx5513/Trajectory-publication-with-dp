from TDrive import MyTree2
import random
from TDrive import Updateexamplesssss
import  math
import  numpy as np
def getDataFlow(inputFileName):
    # 1201968000
    allTupleList = []
    with open(inputFileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            allTupleList.append(tuple)
            # print("allTupleListSize = " + str(len(allTupleList)))
            # return allTupleList

    print("allTupleListSize = "+str(len(allTupleList)))
    return  allTupleList

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



a = getDataFlow("J:\\DataSetForExp\\baiduMap2.txt")
# print(len(a))


#
dicts = creatTrees(a,1201968000,1201975199)

tuples= query(dicts,"215",5,1)



newList = tuples[0]
oldList = tuples[1]

hahanewList =[]
for j in newList:
    for jj in j:
        hahanewList.append(jj)
hahaoldList =[]
for k in oldList:
    for kk in k:
        hahaoldList.append(kk)
hahaoldList.reverse()
hahanewList.reverse()

Updateexamplesssss.updateExam.upexams(hahaoldList,2)  #抽前
Updateexamplesssss.updateExam.upexams(hahanewList,1)  #抽后


# print(dicts[0].getNodechildrenCount("14"))
# print(dicts[10].getNodechildrenCount("14"))
# print(dicts[23].getNodechildrenCount("14"))

# a = getDataFlow("J:\\DataSetForExp\\tt.txt")
# creatTr(a)



# print(dicts)
# d = dicts.get(0)
# print(d.getNodechildrenCount("10"))
#
# d = dicts.get(1)
# print(d.getNodechildrenCount("10"))

# alls = creatTree(a,)
# print(len(alls))
# # Updateexample.updateExam(alls[1])
# Updateexamplesssss.updateExam.upexams(alls[1],2)  #抽前
# Updateexamplesssss.updateExam.upexams(alls[0],1)  #抽后

