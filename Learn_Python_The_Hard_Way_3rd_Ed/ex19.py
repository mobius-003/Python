def cheese_and_crackers(cheese_count, boxes_of_crackers): # define function cheese_and_crackers with two arguments (cheese_count & boxes_of_crackers)
    print(f"You have {cheese_count} cheese!") # prints the value of cheese_count argument (given in line 9)
    print(f"You have {boxes_of_crackers} boxes of crackers!")  # prints the value of boxes_of_crackers argument (given in line 9)
    print("Man that's enough for a party!")  # prints just a string value provided in the brakets (i.e. Man that's enough for a party!)
    print("Get a blanket.\n") # prints just a string value provided in the brakets (i.e. Get a blanket) but on the next line due to '\n' character


print("we can just give the function numbers directly:") # prints just a string value provided in the brakets
cheese_and_crackers(20,30) #calling out function 'cheese_and_crackers' with values of 20, 30 (cheese_count of 20 & boxes_of_crackers of 30)


print("OR, we can use variables from our sript:") # prints just a string value provided in the brakets
amount_of_cheese = 10 #variable of cheese getting a value of 10
amount_of_crackers = 50 #variable with a crackers getting a value of 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #calling out the function 'cheese_and_crackers' with variable defined in lines 13 & 14: 'amount_of_cheese' with values of 10 & 'amount of crackers' with a value of 50


print("We can even do math inside too:") # prints just a string value provided in the brakets
cheese_and_crackers(10+20, 5+6) #calling out the function 'cheese_and_crackers' with variable defined with argument1 summation (10+30), & argument2 summation (5+6)


print("And we can combine the two, variables and math:") # prints just a string value provided in the brakets
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers +1000) #calling out the function 'cheese_and_crackers' with  argument1 & argument 2. Argument1 is summation of line13-ammount of cheese and adding a value of 100. Similarly, Argumen2 is defined as a sumamtion of line14 and plus a value of 1000 of crackers.
