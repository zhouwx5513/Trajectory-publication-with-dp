import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class Show:
    def show(fileName):
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

        x1, y1 = np.loadtxt(fileName, delimiter=',', unpack=True)
        xx = []
        yy = []
        for i in x1:
            xx.append(i)
        for i in y1:
            yy.append(i)
        x = []
        y = []
        x.append(xx)
        y.append(yy)
        for i in range(len(x)):
            plt.plot(x[i], y[i], label='Point', color='red')
            plt.scatter(x[i], y[i], color='blue')

        plt.annotate(r'start',
                     xy=(x[0][0], y[0][0]), xycoords='data',
                     xytext=(0, -20), textcoords='offset points', fontsize=10,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        plt.annotate(r'end',
                     xy=(x[0][-1], y[0][-1]), xycoords='data',
                     xytext=(0, -20), textcoords='offset points', fontsize=10,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Trajectory')
        plt.legend()
        plt.show()
