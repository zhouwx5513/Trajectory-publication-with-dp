import mzgeohash
import math





# test_centroid = [-122.18472385000001, 37.7881345]
# test_points = [
#     (-122.18472385000001, 37.7881345),
# (-122.18472385000002, 37.7881346),
# (-122.18472385000003, 37.7881347),
# (-122.18472385000004, 37.7881348),
# (-122.18472385000005, 37.7881349),
#
# ]

# # expect = '9q9'
# print(mzgeohash.encode([-122.18472385000001, 37.7881345],5))
# print(mzgeohash.neighborsfit(test_centroid, test_points))
# print("--------------------")
# points = map(mzgeohash.encode, test_points)
# for i in points:
#     print(i)



EARTH_RADIUS = 6378.137;
def rad(d):
    return d * math.pi / 180.0
def getDistance(lat1,lng1, lat2,  lng2):

    radLat1 = rad(lat1)

    radLat2 = rad(lat2)

    a = radLat1 - radLat2

    b = rad(lng1) - rad(lng2)

    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2)
                            + math.cos(radLat1) * math.cos(radLat2)
                            * math.pow(math.sin(b / 2), 2)))

    s = s * EARTH_RADIUS;
    # s = math.round(s * 1000)
    s = s*1000
    return s


def getDistances(list1, list2):

    if isinstance(list1[0],str):
       lon1 = float(list1[0])
       lon2 = float(list2[0])
       lat1 = float(list1[1])
       lat2 = float(list2[1])
       radLat1 = rad(lat1)
       radLat2 = rad(lat2)
       a = radLat1 - radLat2
       b = rad(lon1) - rad(lon2)
       s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2)
                                   + math.cos(radLat1) * math.cos(radLat2)
                                   * math.pow(math.sin(b / 2), 2)))

       s = s * EARTH_RADIUS;
       # s = math.round(s * 1000)
       s = s * 1000
    else:
        radLat1 = rad(list1[1])

        radLat2 = rad(list2[1])

        a = radLat1 - radLat2

        b = rad(list1[0]) - rad(list2[0])

        s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2)
                                + math.cos(radLat1) * math.cos(radLat2)
                                * math.pow(math.sin(b / 2), 2)))

        s = s * EARTH_RADIUS;
        # s = math.round(s * 1000)
        s = s*1000
    return int(s)




# print(getDistance(39.92898778580964,116.45723983491926,39.90638170477882,116.41390252697819))
# print(getDistance(39.92157,116.44457,39.89888,116.4012))

# '116.45723983491926,39.92898778580964'
#
# '116.41390252697819,39.90638170477882'
#
# '116.44457', '39.92157'
#
# '116.4012', '39.89888'