from Histogram import KS_g
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
    plt.ylabel('KS')
    plt.show()
    # plt.show()


a1 = KS_g.getKS(20,2)
print(a1)
a2 = KS_g.getKS(20,1)
print(a2)
a3 = KS_g.getKS(20,0.5)
print(a3)
a4 = KS_g.getKS(40,2)
print(a4)
a5 = KS_g.getKS(40,1)
print(a5)
a6 = KS_g.getKS(40,0.5)
print(a6)
a7 = KS_g.getKS(60,2)
print(a7)
a8 = KS_g.getKS(60,1)
print(a8)
a9 = KS_g.getKS(60,0.5)
print(a9)


A = [a1,a2,a3]
B = [a4,a5,a6]
C = [a7,a8,a9]
A.sort()
B.sort()
C.sort()
print(a1)
a = [20,40,60]
f = [A[2],B[2],C[2]]
b = [A[1],B[1],C[1]]
d = [A[0],B[0],C[0]]
f.sort()
b.sort()
d.sort()

# a = [20,40,60]
# f = [a3,a6,a9]
# b = [a2,a5,a8]
# d = [a1,a4,a7]

drawdistributions(a,b,d,f)