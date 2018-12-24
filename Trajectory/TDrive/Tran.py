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



        # System.err.println(aaa[0] + "," + aaa[1]);
        newtuple = (str(aaa[0]), str(aaa[1]), tuple[2], tuple[3])
        return newtuple


    # def hehe(self):
    #     pass



# GpsToBaidu().man(1)


