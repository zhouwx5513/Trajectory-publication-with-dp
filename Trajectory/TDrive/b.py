import time
import numpy as np
from TDrive import mygeohash
from TDrive import MyTree



def getDataFlow(inputFileName,time):
    # 1201968000
    allTupleList = []
    with open(inputFileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            if (int(tuple[3]))<time:
                allTupleList.append(tuple)
            else:
                print("allTupleListSize = " + str(len(allTupleList)))
                return allTupleList

    print("allTupleListSize = "+str(len(allTupleList)))
    return  allTupleList

def center(points,user,par,timebegin):
    x =[]
    y= []
    for i in points:
        x.append(float(i[0]))
        y.append(float(i[1]))
    new = (mygeohash.encode(np.mean(y),np.mean(x),par),user,timebegin)
    return new


# def singleposition(lists):
#     pass
#
def dealwin(tamp,start):
    tree = MyTree.tree()
    # for i in tamp:
    users = {}
    use = []
    # usercount = {}
    for i in tamp:
        if users.get(i[2]) == None:
            users[i[2]] = []
            users[i[2]].append(i)
            # usercount[i[3]] = usercount.get(i[3],0)+
        else:
            users[i[2]].append(i)

    for j in users.keys():
        lists = users.get(j)
        points = []
        for k in lists:
            points.append((k[0], k[1]))
        use.append(center(points, j,3,start))
    print(len(use))
    print(use)
    # if str(start)=="1201930920":
    for each in use:
        tree.Insert(each[0])
    print(len(tree.preorder(tree.getHead())))
    print(tree.preorder(tree.getHead()))

    children = tree.getHead().getchildren()

    sum = 0
    for eachs in children:
        sum+=eachs.getcount()
        print(eachs.getdata(),"=",eachs.getcount())
    print(sum)

    print("========")

        # children = tree.getHead().getchildren()

        # sum = 0
        # for eachs in children:
        #     sum+=eachs.getcount()
        #     print(eachs.getdata(),"=",eachs.getcount())
        #
        #
        #
        # print(sum)
        #
        # tree.getNodechildrenCount("y")
        # print("---y")
        # tree.getNodechildrenCount("yh")
        # print("---yh")
        # tree.getNodechildrenCount("yh5")
        # print("---yh5")






    # print(len(users.keys()))
    # for j in users.keys():
    #     print(len(users.get(j)),users.get(j))


def getpermin(all,begin):
    start = int(int(all[0][3]) / 60) * 60
    print(start)

    index = 0
    size = 0

    while True:
        tamp = []
        tamps = []
        end = start + 60
        while True:

            if int(all[index][3]) >= start and int(all[index][3]) < end:
                tamp.append(all[index])
                index += 1
                if index >= len(all):
                    break;
            else:
                break

        print("(", time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(start)), ")->", "(",
              time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(end)), "):", len(tamp))
        dealwin(tamp,start)
        time.sleep(1)
        start = end
        if index >= len(all):
            break;



allTupleList = getDataFlow("J:\\DataSetForExp\\baidumap1.txt",1201968000)
# allTupleList = getDataFlow("J:\\DataSetForExp\\a.txt",1201968000)
getpermin(allTupleList,111)

# 1201933080
# 1201933139
