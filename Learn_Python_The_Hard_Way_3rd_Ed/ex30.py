people = 30 # var 'people' with its vale of 30 persons
cars = 40 # var 'cars' with its vale of 40 vehicles
trucks = 15 # var 'trucks' with its vale of 15 trucks


if cars > people:   #Checks if cars more numerous than people
    print("We should take cars.") # If cars > people is TRUE print "We should take cars."
elif cars < people:  #Checks if cars less numerous than people
    print("We shouldn't take cars.") # If cars < people is TRUE print "We shouldn't take cars."
else: # if none of the TWO checks are False print ""We can't decide. :(""
    print("We can't decide. :(")


if trucks > cars:  #Checks if truck are more numerous than cars
    print("That's too many trucks.") # If TRUE than print "That's too many trucks."
elif trucks < cars:
    print("Maybe we could take the trucks.") # If FALSE than print ("Maybe we could take the trucks.")
else:
    print("We still can't decide.") # if both conditions are FALSE than print "We still can't decide."


if people > trucks:  #Checks if people are more numerous than trucks
    print("Alright, let's just take the trucks.") # If TRUE than print "Alright, let's just take the trucks."
else:
    print("Fine, let's stay home then.")  #If FALSE than print "Fine, let's stay home then."
