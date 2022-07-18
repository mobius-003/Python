animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print(animals) # prints all elements in the list as depicted in line 1
print ("//" * 15)

for i in animals: # prints all elements in the list in a column
    print (i)
print ("//" * 15)

print(" ")
#print (" 1st, 2nd, 3rd  & 4th are ordinal numbers but we need to count
# by cardinal numbers 0, 1, 2, 3. (Always start at zero(0))

# To access a particular item, put the list name and then add the index
# number in square brackets []

for i in range (len(animals)):
    print (f" Index {i} in the list is {animals[i]} ")

print ("." * 15)
print (animals [3]) # pulls out only the 4th record in the list ['kangaroo']

print ("." * 15)
print (animals [:2]) # pulls out only the first two records [bear, python]

print ("." * 15)
print (animals [1:]) # pulls out all records except the first one 'bear'
#['python', 'peacock', 'kangaroo', 'whale', 'platypus']

print ("." * 15)
print (animals [:-1]) # pulls out all records except the last one 'platypus'
# ['bear', 'python', 'peacock', 'kangaroo', 'whale']
