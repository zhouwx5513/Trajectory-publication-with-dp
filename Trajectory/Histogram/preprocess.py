import numpy as np
from Histogram import mygeohash
from matplotlib import pyplot


inputName = "G://data//map1_14_60.txt"

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

usertupledict = {}


# max = 0
# j = ""
dicts_set = {}
dicts_sets = {}
with open(inputName) as fr:
    for line in fr.readlines():
        lines = line.strip('\n').split(",")
        tuples = (lines[0],lines[1],lines[2],lines[3])
        if lines[2] not in usertupledict:
            usertupledict[lines[2]] = []
        usertupledict[lines[2]].append(tuples)


for i in usertupledict.keys():
    dicts_set[i] = clean(usertupledict[i])

for i in dicts_set.keys():
    locationSet = set()
    for j in dicts_set[i]:
        locationSet.add(mygeohash.encode(float(j[1]), float(j[0]), 2))
    dicts_sets[i] = locationSet




counts = {}
lists = []
for i in dicts_sets.values():
    for j in i:
        if j[0] in mygeohash.neighbors('d').values():
            lists.append(j)
print("len:",len(lists))
for i in lists:
    if not i in counts:
        counts[i]= 0
    counts[i] = counts[i]+1
print(counts)
print(len(counts.keys()))

sum=0
for i in counts.values():
    sum+=i
print("sum",sum)

zoneCounts = {}
for i in counts.values():
    if not i in zoneCounts:
        zoneCounts[i]=0
    zoneCounts[i] = zoneCounts[i]+1
# print(zoneCounts)
# print(len(zoneCounts.keys()))
a = sorted(zoneCounts.items(), key=lambda x: x[0], reverse=False)
print(a)
for i in a:
    print(i)


# sums = 0
# sumss = 0
# sumsss = 0
# for i in a:
#     sumsss+=1
#     tamp = i[0]*i[1]
#     sums+=tamp
#     sumss+=i[1]
# print(sums,sumss,sumsss)
# print("总记录数,总区域数,总bins")
# b = []
# for i in range(100):
#     b.append((i,i))
#
# def neigh(a,i):
#     neighs = []
#     if i>=10 and i<len(a)-10:
#         for j in range(i-10,i+11):
#             neighs.append(a[j])
#     if i<10:
#         if i==0:
#             neighs.append(a[0])
#             neighs.append(a[1])
#         else:
#             for j in range(i*2+1):
#                 neighs.append(a[j])
#     if i>=len(a)-10:
#         if i==len(a)-1:
#             neighs.append(a[len(a)-1])
#             neighs.append(a[len(a)-2])
#         else:
#             for j in range(len(a)-(len(a)-i)*2+1,len(a)):
#                 neighs.append(a[j])
#
#     print(neighs)
#     return neighs
#
#
# def densitycount(list,tuple):
#
#     sum = 0
#     for i in list:
#         tamp = float(abs(tuple[1]-i[1]))
#         sum+=tamp
#
#     print(tuple[0],sum/(len(list)))
#     return sum/(len(list))

# density = {}
#
# print("---------")
# for i in range(len(a)):
#     neighs = neigh(a,i)
#     den = densitycount(neighs,a[i])
#     density[a[i][0]] = den
#
# print(density)
#
# c = sorted(density.items(), key=lambda x: x[1], reverse=True)
# print(c)






# def neigh(a,i):
#     neighs = []
#     if i>=10 and i<len(a)-10:
#         for j in range(i-10,i+11):
#             neighs.append(a[j])
#     if i<10:
#         for j in range(21):
#             neighs.append(a[j])
#     if i>=len(a)-10:
#         for j in range(len(a)-21,len(a)):
#             neighs.append(a[j])
#     print(neighs)
#     return neighs
#
#
# def densitycount(list,tuple):
#
#     sum = 0
#     for i in list:
#         tamp = abs(tuple[1]-i[1])
#         sum+=tamp
#
#     print(tuple[0],sum)
#     return sum
#
# density = {}
#
# print("---------")
# for i in range(len(a)):
#     neighs = neigh(a,i)
#     den = densitycount(neighs,a[i])
#     density[a[i][0]] = den
#
# print(density)
#
# c = sorted(density.items(), key=lambda x: x[1], reverse=True)
# print(c)

x = []
y = []
y_noise = []
z = []
z_noise = []
for i in a:
    x.append(i[0])
    y.append(i[1])
    k_sum = 0
    for k in range(20):
        loc, scale = 0., 120.
        s = np.random.laplace(loc, scale, 1)
        ss = s[0]
        k_sum+=ss
        print(k_sum/20)
    hehe  = k_sum/20+i[1]
    if hehe <0:
        hehe = 0
    y_noise.append(hehe)

    tamp = 0
    for j in range(len(y)):
        tamp+=y[j]
    z.append(tamp)
    hehe = k_sum / 10 + tamp
    if hehe < 0:
        hehe = 0
    z_noise.append(hehe)
# print(y)
fig1 = pyplot.figure()#初始化一个空白画布

l_origin = pyplot.plot(x, y, '-', color="b")#生成一个折线图，X轴，Y轴，图形样式
l_noise = pyplot.plot(x, y_noise,'-', color="r")

# l_origin = pyplot.plot(x, z, '-', color="b")#生成一个折线图，X轴，Y轴，图形样式
# l_noise = pyplot.plot(x, z_noise,'-', color="r")

pyplot.legend(labels=["Origin", "Add_noise",], loc='best')

# pyplot.title('First Plot - Random integers')

pyplot.xlabel('visitor count')

pyplot.ylabel('region number')

pyplot.show()
