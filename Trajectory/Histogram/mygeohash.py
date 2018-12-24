from math import log10

#  Note: the alphabet in geohash differs from the common base32
#  alphabet described in IETF's RFC 4648
#  (http://tools.ietf.org/html/rfc4648)
__base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
__decodemap = { }
for i in range(len(__base32)):
    __decodemap[__base32[i]] = i

del i

def decode_exactly(geohash):
    """
    Decode the geohash to its exact values, including the error
    margins of the result.  Returns four float values: latitude,
    longitude, the plus/minus error for latitude (as a positive
    number) and the plus/minus error for longitude (as a positive
    number).
    """
    lat_interval, lon_interval = (39.7213, 40.1277), (116.1117, 116.7225)
    # lat_err, lon_err = 90.0, 180.0
    lat_err, lon_err = 0.2032, 0.3054
    is_even = True
    for c in geohash:
        cd = __decodemap[c]
        for mask in [16, 8, 4, 2, 1]:
            if is_even: # adds longitude info
                lon_err /= 2
                if cd & mask:
                    lon_interval = ((lon_interval[0]+lon_interval[1])/2, lon_interval[1])
                else:
                    lon_interval = (lon_interval[0], (lon_interval[0]+lon_interval[1])/2)
            else:      # adds latitude info
                lat_err /= 2
                if cd & mask:
                    lat_interval = ((lat_interval[0]+lat_interval[1])/2, lat_interval[1])
                else:
                    lat_interval = (lat_interval[0], (lat_interval[0]+lat_interval[1])/2)
            is_even = not is_even
    lat = (lat_interval[0] + lat_interval[1]) / 2
    lon = (lon_interval[0] + lon_interval[1]) / 2
    # print(lat, lon, lat_err, lon_err)
    return lat, lon, lat_err, lon_err

def decode(geohash):
    """
    Decode geohash, returning two strings with latitude and longitude
    containing only relevant digits and with trailing zeroes removed.
    """
    # lat, lon, lat_err, lon_err = decode_exactly(geohash)
    # # Format to the number of decimals that are known
    # lats = "%.*f" % (max(1, int(round(-log10(lat_err)))) - 1, lat)
    # lons = "%.*f" % (max(1, int(round(-log10(lon_err)))) - 1, lon)
    # if '.' in lats: lats = lats.rstrip('0')
    # if '.' in lons: lons = lons.rstrip('0')
    # return lats, lons
    lat, lon, lat_err, lon_err = decode_exactly(geohash)
    return lat, lon



def adjacent(geohash, direction):
  """Return the adjacent geohash for a given direction."""
  # Based on an MIT licensed implementation by Chris Veness from:
  #   http://www.movable-type.co.uk/scripts/geohash.html
  assert direction in 'nsew', "Invalid direction: %s"%direction
  assert geohash, "Invalid geohash: %s"%geohash
  neighbor = {
    'n': [ 'p0r21436x8zb9dcf5h7kjnmqesgutwvy', 'bc01fg45238967deuvhjyznpkmstqrwx' ],
    's': [ '14365h7k9dcfesgujnmqp0r2twvyx8zb', '238967debc01fg45kmstqrwxuvhjyznp' ],
    'e': [ 'bc01fg45238967deuvhjyznpkmstqrwx', 'p0r21436x8zb9dcf5h7kjnmqesgutwvy' ],
    'w': [ '238967debc01fg45kmstqrwxuvhjyznp', '14365h7k9dcfesgujnmqp0r2twvyx8zb' ]
  }
  border = {
    'n': [ 'prxz',     'bcfguvyz' ],
    's': [ '028b',     '0145hjnp' ],
    'e': [ 'bcfguvyz', 'prxz'     ],
    'w': [ '0145hjnp', '028b'     ]
  }
  last = geohash[-1]
  parent = geohash[0:-1]
  t = len(geohash) % 2
  # Check for edge cases
  if (last in border[direction][t]) and (parent):
    parent = adjacent(parent, direction)
  return parent + __base32[neighbor[direction][t].index(last)]

def neighbors(geohash):
  """Return all neighboring geohashes."""
  return {
    'n':  adjacent(geohash, 'n'),
    'ne': adjacent(adjacent(geohash, 'n'), 'e'),
    'e':  adjacent(geohash, 'e'),
    'se': adjacent(adjacent(geohash, 's'), 'e'),
    's':  adjacent(geohash, 's'),
    'sw': adjacent(adjacent(geohash, 's'), 'w'),
    'w':  adjacent(geohash, 'w'),
    'nw': adjacent(adjacent(geohash, 'n'), 'w'),
    'c':  geohash
  }



def subregions(geohash):

    list1 = []
    for each in __base32:
        list1.append(geohash+each)

    return list1





def encode(latitude, longitude, precision=12):
    """
    Encode a position given in float arguments latitude, longitude to
    a geohash which will have the character count precision.
    """
    lat_interval, lon_interval = (39.7213, 40.1277), (116.1117, 116.7225)
    geohash = []
    bits = [ 16, 8, 4, 2, 1 ]
    bit = 0
    ch = 0
    even = True
    while len(geohash) < precision:
        if even:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if longitude > mid:
                ch |= bits[bit]
                lon_interval = (mid, lon_interval[1])
            else:
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if latitude > mid:
                ch |= bits[bit]
                lat_interval = (mid, lat_interval[1])
            else:
                lat_interval = (lat_interval[0], mid)
        even = not even
        if bit < 4:
            bit += 1
        else:
            geohash += __base32[ch]
            bit = 0
            ch = 0
    return ''.join(geohash)

# for j in range(1,13):
#     code = encode(39.8212475,116.5222825,j)
#     print(code)
#     a , b = decode(code)
#     print(a,b)
#     print(encode(float(a),float(b),j))
#     print("========")

# code = encode(39.91442699430608,116.47848452407902,3)
# print(code)
# a , b = decode(code)
# print(a,b)
# print(encode(float(a),float(b),3))
# print("========")
# print(neighbors(code))
#
# # code = "wtw37q"
# print(type(neighbors(code)),neighbors(code))
# for i in neighbors(code).values():
#     print(decode(i))
# # type(neighbors(code))
#
# print(subregions("kz"))
# print(len(subregions("kz")))
