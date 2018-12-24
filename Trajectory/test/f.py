from math import radians, cos, sin, asin, sqrt
def geodistances(p1,p2):
    lng1, lat1, lng2, lat2 = map(radians, [p1[0], p1[1],p2[0], p2[1]])
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    dis=2*asin(sqrt(a))*6371*1000
    return dis/1000

def head(A):
    return A[0]

def rest(B):
    return B[1:]

def DTW(A,B):
    if len(A)==0 and len(B)==0:
        return 0
    if len(A)==0 or len(B)==0:
        return float('inf')
    else:
        return geodistances(head(A), head(B)) + min(DTW(A, rest(B)), DTW(rest(A), B), DTW(rest(A), rest(B)))
        # return distance(head(A),head(B)) + min(DTW(A,rest(B)),DTW(rest(A),B),DTW(rest(A),rest(B)))
        # return abs(A[0]-B[0])+ min(DTW(A, rest(B)), DTW(rest(A), B), DTW(rest(A), rest(B)))
def DTWS(A,B):
    return (DTW(A,B)+DTW(B,A))/2

A=[(116.1117,39.8),(116.4,40.1),(116.4,40.1)]

B=[(116.7225,39.8),(116.4,40.1),(116.4,40.1)]

print(DTWS(A,B))
