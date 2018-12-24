import numpy as np
from Histogram import mygeohash
from matplotlib import pyplot

# N = 20
# inputName = "G://data//map1_14_40.txt"

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


def noisyCount(sensitivety, epsilon):
    beta = sensitivety / epsilon
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        n_value = -beta * np.log(1. - u2)
    else:
        n_value = beta * np.log(u2)
    return n_value

def noisyCounts(sensitivety, epsilon):
    beta = sensitivety / epsilon
    n_values = []
    for i in range(100):
        u1 = np.random.random()
        u2 = np.random.random()
        if u1 <= 0.5:
            n_value = -beta * np.log(1. - u2)
        else:
            n_value = beta * np.log(u2)
        n_values.append(n_value)
    return np.mean(n_values)


def laplace_mech(data, sensitivety, epsilon):
    datas = list()
    for i in range(len(data)):
        x = data[i] + noisyCounts(sensitivety, epsilon)
        datas.append(x)
    return datas


def countL1(H1,H2):
    sum = 0
    for i in range(len(H1)):
        sum+=abs(H1[i]-H2[i])
        print(H1[i],H2[i],sum)
    print("----------------")
    return sum

def countKS(H1,H2):
    print(H1)
    print(H2)

    lists = []

    allH1 = 0
    allH2 = 0
    for i in range(len(H1)):
        allH1+=H1[i]
        allH2+=H2[i]




    for i in range(len(H1)):
        tamp = 0
        tamp1 = 0
        tamp2 = 0
        for j in range(i+1):
            tamp1 += H1[j]
            tamp2 += H2[j]
            # tamp = tamp+abs(H1[j]-H2[j])
        print(tamp1,allH1,tamp2,allH2,tamp1/allH1,tamp2/allH2)
        tamp = abs(tamp1/allH1-tamp2/allH2)
        lists.append(tamp)

    return max(lists)

def getKS(k,e):
    N = 20
    # inputName = "G://data//map1_14_40.txt"
    inputName = "G://data//map1_14_"
    inputName=inputName+str(k)+".txt"
    usertupledict = {}
    sensitivety = int(2*k)
    epsilon = e

    # max = 0
    # j = ""
    dicts_set = {}
    dicts_sets = {}
    with open(inputName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuples = (lines[0], lines[1], lines[2], lines[3])
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

    for i in lists:
        if not i in counts:
            counts[i] = 0
        counts[i] = counts[i] + 1

    sum = 0
    for i in counts.values():
        sum += i

    zoneCounts = {}
    for i in counts.values():
        if not i in zoneCounts:
            zoneCounts[i] = 0
        zoneCounts[i] = zoneCounts[i] + 1

    a = sorted(zoneCounts.items(), key=lambda x: x[0], reverse=False)
    max = a[len(a) - 1][0]
    b = {}
    for i in a:

        b[i[0]] = i[1]
    for i in range(1, max + 1):
        if i not in b:
            b[i] = 0

    c = []
    for i in b.keys():
        c.append((i, b[i]))

    p = []
    p.append(1)
    for i in range(1, N):
        tamp = ((max - 1) * i / N) + 1
        p.append(int(tamp))
    p.append(max)


    g = []
    for i in range(N):
        g.append(0)

    for i in c:
        for j in range(1, N + 1):
            if i[0] >= p[j - 1] and i[0] < p[j]:
                g[j - 1] += i[1]
    g[N - 1] += c[len(c) - 1][1]


    G = []
    for i in range(N):
        G.append((p[i + 1], g[i]))


    x = []
    y = []
    y_noise = []
    z = []
    z_noise = []
    for i in G:
        x.append(i[0])
        y.append(i[1])

        tamp = 0
        for j in range(len(y)):
            tamp += y[j]
        z.append(tamp)

    y_noise = laplace_mech(y, sensitivety, epsilon)
    z_noise = laplace_mech(z, sensitivety, epsilon)
    # for j in range(len(z_noise)):
    #     if z_noise[j] < 0:
    #         z_noise[j] = 0
    # for j in range(len(y_noise)):
    #     if y_noise[j] < 0:
    #         y_noise[j] = 0
    return countKS(y,y_noise)
