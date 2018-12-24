from TDrive import ss
import mzgeohash

def calculatorRange(list):
    left=[]
    right=[]
    top=[]
    down=[]
    total = []

    # longMax = 0.
    # longMin = 0.
    # latiMax = 0.
    # latiMin = 0.

    lenList = len(list)
    index = 0
    for i in list:
        index+=1
        if index==1:
            longMax = i[0]
            latiMax = i[1]
            longMin = i[0]
            latiMin = i[1]
            left.clear()
            left.append(i[0])
            left.append(i[1])

            right.clear()
            right.append(i[0])
            right.append(i[1])

            top.clear()
            top.append(i[0])
            top.append(i[1])

            down.clear()
            down.append(i[0])
            down.append(i[1])


        else:
            if i[0]>longMax:
                longMax = i[0]
                right.clear()
                right.append(i[0])
                right.append(i[1])
            if i[1]>latiMax:
                latiMax = i[1]
                top.clear()
                top.append(i[0])
                top.append(i[1])
            if i[0]<longMin:
                longMin = i[0]
                left.clear()
                left.append(i[0])
                left.append(i[1])
            if i[1]<latiMin:
                latiMin = i[1]
                down.clear()
                down.append(i[0])
                down.append(i[1])
        # print(str(i)+" 右"+str(longMax)+" 上"+str(latiMax)+" 左"+str(longMin)+" 下"+str(latiMin))

    total.append(left)
    total.append(right)
    total.append(top)
    total.append(down)
    print("range down")
    print("东西跨度："+str(ss.getDistances(left,right)))
    print("南北跨度："+str(ss.getDistances(top, down)))

    return total



# list = [[2.5,5.5],[2,6],[1,1],[3,5]]
#
# print(calculatorRange(list))
# # 左右上下
def calculatorZone(list1):

    # print(mzgeohash.encode((116.40957280303152, 39.9190363799492),5))
    dicts= {}
    for i in list1:
        t = (float(i[0]),float(i[1]))
        word = mzgeohash.encode(t,5)
        print(word)
        dicts[word] = dicts.get(word,0)+1

    # print(type(dicts))
    dicts = sorted(dicts.items(),key = lambda x:x[1],reverse = True)
    print(dicts)
    print(str(len(dicts)))


