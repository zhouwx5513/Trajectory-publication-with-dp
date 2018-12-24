import time
import datetime
import mzgeohash

inputFileName = "J:\\DataSetForExp\\release\\test_output\\e.txt"
fileName = "J:\\DataSetForExp\\release\\test_output\\8525a.txt"
def getDataFlow(inputFileName):
    allTupleList = []
    with open(inputFileName) as fr:
        for line in fr.readlines():
            lines = line.strip('\n').split(",")
            tuple = (lines[0],lines[1],lines[2],lines[3])
            if(lines[2]=="8525"):
                allTupleList.append(tuple)
    print("allTupleListSize = "+str(len(allTupleList)))
    return  allTupleList


def writeToTxt(all,fileName):
    with open(fileName, 'w') as f:
        for i in all:
            ss = i[0] +","+ i[1]+","+i[2]+","+i[3]+"\n"
            f.write(ss)
    f.close()

writeToTxt(getDataFlow(inputFileName),fileName)

