from sys import argv
script, args = argv[0], argv[1:]

print("The script is called: ", script)
for i, arg in enumerate(args):
    print("Arg {0:d}: {1:s}".format(i, arg))
