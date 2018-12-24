import numpy as np
from Histogram import mygeohash
import matplotlib.pyplot as plt

def drawdistributions(a,b,d,f):
    a = np.array(a)
    b = np.array(b)
    d = np.array(d)
    f = np.array(f)
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
    # l1 = plt.bar(x=a, height=b, width=0.02, alpha=0.2, color='#6699ff', label="一部门") #紫
    # l2 = plt.bar(x=c, height=d, width=0.02, alpha=0.2, color='r', label="一部门") #红
    # l3 = plt.bar(x=e, height=f, width=0.02, alpha=0.2, color='g', label="一部门")  #绿
    plt.bar(a - 0.2, f, width=0.2, facecolor='red', edgecolor='white')
    plt.bar(a, b, width=0.2, facecolor='lightskyblue', edgecolor='white')
    # width:柱的宽度
    plt.bar(a + 0.2, d, width=0.2, facecolor='yellowgreen', edgecolor='white')

    plt.show()


    # plt.legend(handles=[l2, l1, l3], labels=["k=3", "k=5", "k=7", ], loc='best')
    # plt.xlabel('x')
    # plt.ylabel('Av_DTW')
    # plt.show()


d = [1,2,3,4,5,6,7,8,9]
e = [11,12,13,14,15,16,17,18,19]
f = [21,22,23,24,25,26,27,28,29]
a = [1,2,3,4,5,6,7,8,9]

drawdistributions(a,d,e,f)