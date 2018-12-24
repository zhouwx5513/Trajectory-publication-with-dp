from Histogram import mygeohash

inputName = "G://data//map1_14_20.txt"
sum = 0

userset = set()
usercount = []
locationset = set()
locationset2 = set()
locationset3 = set()
locationset4 = set()


with open(inputName) as fr:
    for line in fr.readlines():
        sum += 1
        lines = line.strip('\n').split(",")

        locationset2.add(mygeohash.encode(float(lines[1]), float(lines[0]), 2))
        locationset3.add(mygeohash.encode(float(lines[1]), float(lines[0]), 3))
        locationset4.add(mygeohash.encode(float(lines[1]), float(lines[0]), 4))

        userset.add(lines[2])
        usercount.append(lines[2])

print(sum)
print(len(userset))
print(len(usercount))

print("------------------")
print(len(locationset2))
print(len(locationset3))
print(len(locationset4))
