from sys import argv

if len(argv) < 4:
    print ("usage: {0:s} <bike> <car> <bus>".format(script))
    raise SystemExit(-1)

script, bike, car, bus = argv

print ("The script is called:", script)
print ("The first variable is:", bike)
print ("The second variable is ", car)
print ("Your third variable is : ", bus)
