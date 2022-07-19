i = 0 # variable i starts at zero
list1 = [] # empty list called 'numbers'

# while loops are similar as for loops; i is variable and criteria "< "
# it will print 'i' is .... and then is going to append to i, by adding 1 to it.
# it starts with zero and increments it to next step
# 1st step: at the top i = 0 , at the bottom i = 1, 'Numbers now:' is actually a list
while i < 6:
    print(f"At the top: i = {i}")
    #print(f"At the bottom: i = {i}")
    list1.append(i)
    # print(f"At the bottom: i = {i}")
    i = i + 1
    print(f"At the bottom: i = {i}")
    print("The list is: ", list1) # the top number and previous numbers are included in the list 'list1'
    print('*' * 30) # separator (* character printed 30 times)
print ("The numbers in the list are: ") # prints all the numbers in the list as a column (0 ... 5)

for num in list1:
    print(num)
