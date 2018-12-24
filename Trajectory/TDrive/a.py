import time
import  os

import math



class GpsToBaidu:
    pi = 3.1415926535897932384626
    ee = 0.00669342162296594323
    a = 6378245.0
    lon = 0.0
    lat = 0.0


    def transformLat(x, y):
        ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
        ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
        ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
        return ret

    def gps84_To_Gcj02(i):
        dLat = GpsToBaidu.transformLat(GpsToBaidu.lon - 105.0, GpsToBaidu.lat - 35.0)
        dLon = GpsToBaidu.transformLon(GpsToBaidu.lon - 105.0, GpsToBaidu.lat - 35.0)
        radLat = GpsToBaidu.lat / 180.0 * math.pi
        magic = math.sin(radLat);
        magic = 1 - GpsToBaidu.ee * magic * magic
        sqrtMagic = math.sqrt(magic)
        dLat = (dLat * 180.0) / ((GpsToBaidu.a * (1 - GpsToBaidu.ee)) / (magic * sqrtMagic) * math.pi)
        dLon = (dLon * 180.0) / (GpsToBaidu.a / sqrtMagic * math.cos(radLat) * math.pi)
        GpsToBaidu.lat = GpsToBaidu.lat + dLat
        GpsToBaidu.lon = GpsToBaidu.lon + dLon

    def gcj02_To_Bd09(i) :
        x = GpsToBaidu.lon
        y = GpsToBaidu.lat
        z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * math.pi)
        theta = math.atan2(y, x) + 0.000003 * math.cos(x * math.pi)
        GpsToBaidu.lon = z * math.cos(theta) + 0.0065
        GpsToBaidu.lat = z * math.sin(theta) + 0.006



    def transformLon(x, y):
        ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
        ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
        ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
        return ret

    def wgs2bd(in_lon, in_lat):
        GpsToBaidu.lon = in_lon
        GpsToBaidu.lat = in_lat
        GpsToBaidu.gps84_To_Gcj02(1)
        GpsToBaidu.gcj02_To_Bd09(1)
        gcj2bd = [GpsToBaidu.lon, GpsToBaidu.lat]
        return gcj2bd

    def dealtuple(tuple):
        # print(tuple)
        in_lon = float(tuple[0])
        in_lat = float(tuple[1])
        aaa = GpsToBaidu.wgs2bd(in_lon, in_lat)
        newtuple = (str(aaa[0]), str(aaa[1]), tuple[2], tuple[3])
        return newtuple

def loadDataSet(fileName):
    data=[]

    cleans = ""

    with open(fileName) as fr:
        for line in fr.readlines():
            if len(line)>2:
                lines = line.strip('\n').split(",")
                timeStamp = time.mktime(time.strptime(lines[1], '%Y-%m-%d %H:%M:%S'))
                tamp = str(timeStamp) + str(lines[0])
                if tamp != cleans:
                    timeStamp = int(timeStamp)
                    t = (lines[2], lines[3],lines[0],timeStamp)
                    # data.append(t)
                    data.append(GpsToBaidu.dealtuple(t))
                    cleans = tamp

    return data

def FromDireGetData(directory):
    z = 0
    datas=[]
    for maindir, subdir, file_name_list in os.walk(directory):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            t = loadDataSet(apath)
            for i in t:
                datas.append(i)
            z+=1
            print(z,len(t),filename)
            # time.sleep(0.05)
    print(str(len(datas)),z)
    return datas


transDatas = FromDireGetData("J:\\DataSetForExp\\release\\jjj")

print("ss",len(transDatas))

print(transDatas)

transDatas.sort(key = lambda x:x[3],reverse = False)
fileName = "J:\\DataSetForExp\\release\\test_output\\he.txt"
# fileName = "//home//zhouwx//baiduMap.txt"
index = 0
with open(fileName, 'w') as f:
    for i in transDatas:
        if (float(i[0]) > 116.1117 and float(i[0]) < 116.7225 and float(i[1]) > 39.7213 and float(i[1]) < 40.1277):
            # if (float(i[0]) > 116.2075579685 and float(i[0]) < 116.5632212466 and float(i[1]) > 39.8333472137 and float(i[1]) < 40.0326836503):
            ss = str(i) + "\n"
            index += 1
            f.write(ss)
    f.close()
print("over!",index)