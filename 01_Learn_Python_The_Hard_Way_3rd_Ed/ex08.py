formatter = ("{} {} {} {}") #define the formmater variable containing "{} {} {} {}"

#Prints above var formmater using the format '1 2 3 4'
print(formatter.format(1,2,3,4))

#Prints above var formmater structure using the format 'one two three four'
print(formatter.format("one","two","three","four"))

#Prints above var formmater using the format 'True False False True'
print(formatter.format(True,False, False,True))

#Prints above var formmater using the format 4 times of '{} {} {} {}'
print(formatter.format(formatter, formatter, formatter, formatter))

#Prints above var formmater using the string in the tripple qoutes
print(formatter.format(
     "Try your",
     "Own text here",
     "Maybe a poem",
     "Or maybe a song about fear"
))
