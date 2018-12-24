from Histogram import L11
import numpy as np
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
    plt.bar(a - 3, f, width=3, facecolor='red', edgecolor='white')
    plt.bar(a, b, width=3, facecolor='lightskyblue', edgecolor='white')
    # width:柱的宽度
    plt.bar(a + 3, d, width=3, facecolor='yellowgreen', edgecolor='white')
    plt.legend(labels=["epsilon=0.5", "epsilon=1", "epsilon=2", ], loc='best')
    plt.xlabel('k')
    plt.ylabel('L1')
    plt.show()
    # plt.show()


a1 = L11.getL1(20,2)
a2 = L11.getL1(20,1)
a3 = L11.getL1(20,0.5)
a4 = L11.getL1(40,2)
a5 = L11.getL1(40,1)
a6 = L11.getL1(40,0.5)
a7 = L11.getL1(60,2)
a8 = L11.getL1(60,1)
a9 = L11.getL1(60,0.5)

a = [20,40,60]
f = [a3,a6,a9]
b = [a2,a5,a8]
d = [a1,a4,a7]

drawdistributions(a,b,d,f)