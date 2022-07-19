the_count = [1, 2, 3, 4] #this is a list or array
fruits = ['apples', 'oranges', 'pears', 'apricots'] #this is a list or array
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] #this is a list

# this 1st kind of FOR-LOOP goes through a list
# this for-loop will step through each element of the list
# 'number' reperesents the 1st element in list 'the_count'
# 'number' can have any name we want.
for number in the_count:
    print(f"This is count {number}")


# same as above FOR-LOOP; this is the 2nd kind of for-loop
# this for-loop will step through each element of the list
# 'fruit' reperesents the 1st element in list 'fruits'
# 'fruit' can have any name we want. Prints as a string due to f "string {fruit}"
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed list too
# notice we have to use {} since we don't know what is in it
# this is the 3rd kind of for-loop;
# 'i' reperesents the 1st element in list 'change'
# 'i' and 'x' are the most common names.
# prints as a string due to f "string {i}"
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    # range(start, stop) where 'start' number is inclusive
    # but 'stop' number is exclusive (6 items -stops at 5);
    # 0 (zero) is the default number of the list; we can use only range(6)
    print(f"Adding {i} to the list.")
    # append is a function that lists understands
    # add elements to the list using .append method
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
