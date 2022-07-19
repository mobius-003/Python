cars = 100 # vaiable number of total cars
space_in_a_car = 4.0 # variable 'space in a car'
drivers = 30 # variable number of drivers
passengers = 90 # variable number of passengers
cars_not_driven = cars - drivers # variable of undriven cars 
#(diff of var 'cars' & var 'drivers')
cars_driven = drivers # variable of driven cars which is equal to number of drivers
carpool_capacity = cars_driven * space_in_a_car # variable of carpool capacity 
#which is a multiplication of var 'driven cars' & var 'space in a car'
average_passengers_per_car = passengers / cars_driven # varaiable 'avg passengers per car' 
#which equals with division of var 'passengers' to var 'cars diven'

# prints out the total number of available cars
print("There are", cars, "cars available.") 
print("There are only" , drivers, "drivers available.") # prints out only the total 
#number of aviable drivers
print("There will be" , cars_not_driven, "empty cars today.") # prints out the total 
#number of empty cars today
print("We can transport", carpool_capacity, "people today.") # prints out the total number 
#of people that can be transported today
print("We have" , passengers, "to carpool today.") # prints the total number of passengers 
print("We need to put about" , average_passengers_per_car, "in each car") # prints out the avarage number of passenger 

